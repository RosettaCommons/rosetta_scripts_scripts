# -*- coding: utf-8 -*-

# (c) Copyright Rosetta Commons Member Institutions.
# (c) This file is part of the Rosetta software suite and is made available under license.
# (c) The Rosetta software is developed by the contributing members of the Rosetta Commons.
# (c) For more information, see http://www.rosettacommons.org. Questions about this can be
# (c) addressed to University of Washington CoMotion, email: license@uw.edu.

## Authors: David Thieker

################################################################################################
#
# This script prepares input for RosettaScripts that score point mutations (PM) in a protein, often used for site saturation mutagenesis. The script is also useful for analyzing results; however, two Rosetta jobs (RosettaScripts) must be submitted before analysis. Details for submitting these jobs are below, after the documentation for this python script.
#
################################################################################################
#
# Documentation for stabilizing_pm.py:
#
# Generate input or analyze results for point mutations (PM)
#
# stabilizing_pm.py
# -mode is either 'trim' 'build', or 'analyze' [Required]
#     -mode trim: Prepare the PDB file for relax (remove heteroatoms except for MSE and those defined by the user with the -lig option)
#     -mode build: Build the directory tree and jobdefinition file
#     -mode analyze: Analyze the results after PM has been performed (collect best models based on total_score, calculate delta scores to WT, and generate a heatmap of results)
# -pdb is starting structure filename. The starting structure should already be relaxed (original rosetta script used CARTESIAN minimization) [Required]
# -pos is residue positions for PM. Format is a comma-delimited list with chain_ID preceding each residue (e.g. H[1,10-20],L[23]). Insertion codes are allowed. [Required if -sym is not selected]
# -subs is amino acid residues to substitute during PM (must include WT residue for each position selected) [Optional, default is all amino acids]
# -sym allows mutations on multiple chains simultaneously (Format is chains:residues (i.e. ABC[20-30,35,80]) [Required if -pos is not selected]
# -lig allows the user to specify ligand residues to keep when mode==trim. Format is a comma-delimited list with chain_ID preceding each residue (e.g. H[405-408],L[403]) [Optional]
#
# Example of trimming a PDB file:
# python stabilizing_pm.py -mode trim -pdb input_file.pdb 
#
# Example of building PM inputs:
# python stabilizing_pm.py -mode build -pdb input_file.pdb -pos H[1,10-20],L[23] 
#
# Example of building PM inputs while skipping Cys mutations:
# python stabilizing_pm.py -mode build -pdb input_file.pdb -pos H[1,10-20],L[23] -subs ADEFGHIKLMNPQRSTVWY
#
# Example of analyzing PM results from a symmetric run:
# python stabilizing_pm.py -mode analyze -pdb input_file.pdb -sym ABC[20-30,35,80]
#
################################################################################################
#
# After building the input and before analyzing the results, the user will need to submit two RosettaScripts jobs. The following is an example for how to do so, note the version of rosetta_scripts_jd3 will be system-dependent:
#
#   First, relax the input structure: 
#     mpirun rosetta_scripts_jd3.mpiserialization.linuxgccrelease -parser:protocol rs_relax_pm.xml -s trimmed_input_protein.pdb -nstruct 10 -out:file:scorefile score.sc -use_truncated_termini -missing_density_to_jump -jd3:n_archive_nodes 2 -mpi_tracer_to_file mpi -linmem_ig 10 -out:pdb -overwrite
#
#   Second, copy the best-scoring model (total_score) from the relax run (named trim_tree_relaxed.pdb here) and submit the follow-up job:
#     mpirun rosetta_scripts_jd3.mpiserialization.linuxgccrelease -parser:protocol rs_pm.xml -s trim_cart_relaxed.pdb -job_definition_file jobdef.xml -use_truncated_termini -missing_density_to_jump -jd3:n_archive_nodes 2 -mpi_tracer_to_file mpi -linmem_ig 10 -out:pdb -overwrite 
# 
################################################################################################

''' ROSIE stabilize_pm App - tested with Python v3.5 '''

import sys, os, re, shutil
import types, math, numpy, matplotlib
matplotlib.use('Agg') #Command-line only, don't display on screen
import matplotlib.pyplot as plt
import matplotlib.colors as colors

############# Print the RosettaScripts that are required for the PM calculations (rs_relax_pm.xml and rs_pm.xml). #############

xml_relax_pm = '''\
<ROSETTASCRIPTS>
  <SCOREFXNS>
    <ScoreFunction name="sfxn" weights="ref2015"/>  # Score function without constraints
    <ScoreFunction name="sfxn_cc" weights="ref2015">   # Reweight the score function to include coordinate constraints
      <Reweight scoretype="coordinate_constraint" weight="1.0"/>
    </ScoreFunction>
    <ScoreFunction name="sfxn_cart" weights="ref2015_cart"/>    # Score function without constraints
    <ScoreFunction name="sfxn_cart_cc" weights="ref2015_cart"> # Reweight the score function to include coordinate constraints
      <Reweight scoretype="coordinate_constraint" weight="1.0"/>
    </ScoreFunction>
  </SCOREFXNS>
  <RESIDUE_SELECTORS>
  </RESIDUE_SELECTORS>
  <TASKOPERATIONS>
    <InitializeFromCommandline name="ifcl_to"/> # Accept command-line options
    <IncludeCurrent name="incl_curr_to"/> # Include rotamer from input structure during packing
    <RestrictToRepacking name="repack_only" /> # Turn off design at these positions. Only repack and minimize
    <ExtraRotamersGeneric name="ex12_to" ex1="1" ex2="1" extrachi_cutoff="0"/> # Include additional rotamers during repacking
  </TASKOPERATIONS>
  <CONSTRAINT_GENERATORS>
    <CoordinateConstraintGenerator name="all_bb_ca_cc" sd="2" ca_only="true" />       # Add backbone constraints (C_alpha-only) for all residues
  </CONSTRAINT_GENERATORS>
  <MOVERS>
    <VirtualRoot name="vr" />
    <AddConstraints name="cc" constraint_generators="all_bb_ca_cc" />
    <FastRelax name="relax_atomTree" scorefxn="sfxn_cc" repeats="1" relaxscript="MonomerRelax2019" task_operations="ifcl_to,incl_curr_to,repack_only,ex12_to" cartesian="false" />
    <FastRelax name="relax_cart" scorefxn="sfxn_cart" repeats="3" relaxscript="MonomerRelax2019" task_operations="ifcl_to,incl_curr_to,repack_only,ex12_to" cartesian="true" />
  </MOVERS>
  <PROTOCOLS>
    <Add mover="vr"/>
    <Add mover="cc"/>
    <Add mover="relax_atomTree"/>
    <Add mover="relax_cart"/>
  </PROTOCOLS>
  <OUTPUT scorefxn="sfxn"/> # Output score without penalties from constraints (cc/cc2)
</ROSETTASCRIPTS>
'''

xml_pm = '''\
<ROSETTASCRIPTS>

  <SCOREFXNS>
    <ScoreFunction name="sfxn_cc" weights="ref2015_cart"> # Reweight the score function to include coordinate constraints
      <Reweight scoretype="coordinate_constraint" weight="1.0"/>
    </ScoreFunction>
    <ScoreFunction name="sfxn" weights="ref2015_cart"/> # Score function without constraints
  </SCOREFXNS>

  <RESIDUE_SELECTORS>
    <Index name="target_residue_to_mutate" resnums="%%pos1%%" />        # Mutation site
    <PrimarySequenceNeighborhood name="primary_seq_res" selector="target_residue_to_mutate" /> # Residues flanking and including the target_residue (n=3)
    <Not name="not_primary_seq_res" selector="primary_seq_res"/>
    <Neighborhood name="neighbors" selector="target_residue_to_mutate"/> # Residues within 10 A of target_residue
    <Not name="not_neighbor" selector="neighbors"/>
    <And name="soft_sphere" selectors="neighbors,not_primary_seq_res"/>
    <StoredResidueSubset name="neighbors_stored" subset_name="neighbors"/>      # Remember selection (important to select neighbors BEFORE mutation so that neighborhood does not change for Gly, which lacks a CB atom)
    <StoredResidueSubset name="not_neighbor_stored" subset_name="not_neighbor"/>
    <StoredResidueSubset name="soft_sphere_stored" subset_name="soft_sphere"/>
  </RESIDUE_SELECTORS>

  <MOVE_MAP_FACTORIES>
    <MoveMapFactory name="inside_sphere" chi="false" bb="false"> # Disable all degrees of freedom globally (DOFs)
      <Chi residue_selector="neighbors_stored"/> # Allow sidechain DOFs of neighbors_stored
      <Backbone residue_selector="neighbors_stored"/> # Allow backbone DOFs of neighbors_stored
    </MoveMapFactory>
  </MOVE_MAP_FACTORIES>
  <TASKOPERATIONS>
    <OperateOnResidueSubset name="fix" selector="not_neighbor_stored">
      <PreventRepackingRLT/>
    </OperateOnResidueSubset>
    <InitializeFromCommandline name="ifcl_to"/> # Accept command-line options
    <IncludeCurrent name="incl_curr_to"/> # Include rotamer from input structure during packing
    <RestrictToRepacking name="repack_only" /> # Turn off design at these positions. Only repack and minimize
    <ExtraRotamersGeneric name="ex12_to" ex1="1" ex2="1" extrachi_cutoff="0"/> # Include additional rotamers during repacking
  </TASKOPERATIONS>
  <CONSTRAINT_GENERATORS>
    <CoordinateConstraintGenerator name="not_neightbor_cc" sd="1" ca_only="true" residue_selector="not_neighbor_stored" /> # Add strong backbone constraints (C_alpha-only) for residues outside of the sphere around the target residue (residues limited by MoveMap)
    <CoordinateConstraintGenerator name="softsphere_cc" sd="2" ca_only="true" residue_selector="soft_sphere_stored" />       # Add weaker backbone constraints (C_alpha-only) for residues within the sphere around the target residue (excluding primary_seq_res)
  </CONSTRAINT_GENERATORS>

  <MOVERS>
    <VirtualRoot name="vr" />
    <StoreResidueSubset name="store_neighbs" subset_name="neighbors" residue_selector="neighbors"/>
    <StoreResidueSubset name="store_not_neighb" subset_name="not_neighbor" residue_selector="not_neighbor"/>
    <StoreResidueSubset name="store_soft_sphere" subset_name="soft_sphere" residue_selector="soft_sphere"/>
    <AddConstraints name="cc" constraint_generators="not_neightbor_cc" />
    <AddConstraints name="cc2" constraint_generators="softsphere_cc" />
    <MutateResidue name="mutate" residue_selector="target_residue_to_mutate" new_res="%%aa%%" preserve_atom_coords="true"/>
    <FastRelax name="relax" scorefxn="sfxn_cc" repeats="3" relaxscript="MonomerRelax2019" task_operations="fix,ex12_to,ifcl_to,repack_only,ifcl_to" movemap_factory="inside_sphere" cartesian="true" />
  </MOVERS>

  <PROTOCOLS>
    <Add mover="vr"/>
    <Add mover="store_neighbs"/>
    <Add mover="store_not_neighb"/>
    <Add mover="store_soft_sphere"/>
    <Add mover="mutate"/>
    <Add mover="cc"/>
    <Add mover="cc2"/>
    <Add mover="relax"/>
  </PROTOCOLS>

  <OUTPUT scorefxn="sfxn"/> # Output score without penalties from constraints (cc/cc2)

</ROSETTASCRIPTS>
'''

def gen_RScripts(pdb_file):
    # Initial relax with AtomTree minimization (repeats=1). This step is simply to process the pdb file (add hydrogens) so that -use_truncated_termini can be turned on without improperly treating the real N and C-termini.

    if not os.path.exists('./relax'):
        os.makedirs('./relax')
    else:
        print(("Directory ./relax already exists, overwriting the relax RosettaScript file"))

    shutil.copy(pdb_file, './relax')

    xml_file = './relax/rs_relax_pm.xml'
    with open (xml_file, 'w') as xml_file :
        xml_file.write( xml_relax_pm )
    
    # Second RosettaScript for Site Saturation Mutagenesis (repeats=3). Note that this requires a jobdefinition file
    xml_file3 = 'rs_pm.xml'
    with open (xml_file3, 'w') as xml_file3:
        xml_file3.write( xml_pm )

############# This section (~110 lines) is for parsing the PDB file and was extracted from rosetta/tools/pdb_structure.py, written by Andrew Leaver-Fay. #############

# some foundation classes for representing the contents of a PDB
def is_integer( s ) :
    try :
        int(s)
        return True
    except :
        return False

class Residue :
    def __init__( self ) :
        self.resstring = "" # residue index + insertion code -- a string
        self.resname = ""
        self.insertion_code = ""
        self.chain = None #pointer to the containing chain
    # insert this residue into a Chain
    def claim( self, containing_chain ) :
        self.chain = containing_chain
    #return the chain-subsstring tuple for this residue that uniquely identifies it
    #Requires that the residue has already been inserted into a chain
    def resid( self ) :
        assert( self.chain )
        return self.chain.chain_name + " " + self.resstring

class Chain :
    def __init__( self ) :
        self.chain_name = ""
        self.residues = []
        self.resmap = {}
    def add_residue( self, residue ):
        self.residues.append( residue )
        self.resmap[ residue.resstring ] = residue
        residue.claim( self )
    def replace_residue( self, newresidue ):
        # in place replacement; keep the original location of the residue in the self.residues array
        copyres = copy.copy( newresidue )
        copyres.claim( self )
        if newresidue.resstring not in self.resmap :
            print("Could not replace residue", newresidue.resstring)
            print(len( self.resmap ))
        assert( newresidue.resstring in self.resmap )
        for i in range(len( self.residues )) :
            if self.residues[ i ].resstring == newresidue.resstring :
                self.residues[ i ] = copyres
        self.resmap[ newresidue.resstring ] = copyres
    def residue( self, resstring ) :
        return self.resmap[ resstring ]

class PDBStructure :
    def __init__( self ):
        self.chains = []
        self.chainmap = {}

    def residue( self, chnm, resstring ) :
        return self.chainmap[ chnm ].residue( resstring )

    def add_chain( self, chain ) :
        self.chains.append( chain )
        self.chainmap[ chain.chain_name ] = chain

    def read_from_lines( self, lines ):
        last_chain = Chain()
        last_residue = Residue()
        for line in lines :
            if line[0:4] == "ATOM" or line[0:6] == "HETATM" :
                chnm = self.chain_name_from_pdbline( line )
                if last_chain.chain_name != "" and chnm != last_chain.chain_name :
                    last_chain.add_residue( last_residue )
                    last_residue = Residue()
                    if last_chain.chain_name not in self.chainmap : self.add_chain( last_chain )
                    if chnm not in self.chainmap :
                        last_chain = Chain()
                    else :
                        # this chain has already been added, but now we have more residues
                        last_chain = self.chainmap[ chnm ]
                if last_chain.chain_name == "":
                    last_chain.chain_name = chnm
                resstring = self.resstring_from_pdbline( line )
                if last_residue.resname != "" and last_residue.resstring != resstring :
                    last_chain.add_residue( last_residue )
                    last_residue = Residue()
                if last_residue.resname == "" :
                    last_residue.resname = self.resname_from_pdbline( line )
                    last_residue.resstring = resstring
                    #print "Read residue", last_residue.resname, last_chain.chain_name, last_residue.resstring
        if last_residue.resname != "":
            last_chain.add_residue( last_residue )
        if last_chain.chain_name != "" and last_chain.chain_name not in self.chainmap :
            self.add_chain( last_chain )
    def pdb_resname_range( self ) :    return ( 17, 20 )
    def pdb_chain_name_range( self ) : return ( 21, 22 )
    def pdb_resstring_range( self ) :  return ( 22, 27 )
    def pdb_occupancy_range( self ) :  return ( 56, 60 )

    def resname_from_pdbline( self, line ):
        return line[ self.pdb_resname_range()[0]:self.pdb_resname_range()[1] ]
    def chain_name_from_pdbline( self, line ):
        return line[ self.pdb_chain_name_range()[0]:self.pdb_chain_name_range()[1] ]
    def resstring_from_pdbline( self, line ):
        return line[ self.pdb_resstring_range()[0]:self.pdb_resstring_range()[1] ].strip()

def pdbstructure_from_file( fname ) :
    pdb = PDBStructure()
    with open( fname ) as f: pdb.read_from_lines( f.readlines() )
    return pdb

############# End of excerpt from rosetta/tools/pdb_structure.py #############

# The user input format was changed from the first version. This function converts the new format (A[2,3-6]) to the old format (A2,A3-A6) to maintain future residue parsing functions
def parse_brackets_input_resid(bracketed_input):
    # Split input "A[257,258-260]" into "A257,A258-A260"
    chains=[]
    # Pull string preceding '['
    for out_brackets in bracketed_input.split('['):
        chain=out_brackets.split(']')[-1]
        chain=chain.replace(",","")
        chains.append(chain)
    del chains[-1]
    
    positions=[]
    
    # Pul string within brackets ('[]')
    for in_brackets in bracketed_input.split('['):
        position=in_brackets.split(']')[0]
#        print(position)
        positions.append(position)
    del positions[0]
#    print(len(positions))
    
    # Apply chain ID to each number inside of brackets
    combined_list=""
    c=0
    while c < len(chains):
        test=(chains[c]+positions[c])
        test=test.replace(",",","+chains[c])
        test=test.replace("-","-"+chains[c])
        combined_list=combined_list+','+test
        c=c+1
#        print(test)
    combined_list=combined_list[1:]
    return combined_list

def parse_input_resid(pdb_file, input_residues):
    '''Convert user-provided numbers to list of individual residues.
    input_residues should be in format "L30,H40-H42A" where first
    char is chain_id and the remainder is residue number. H42A
    refers to an insertion code for residue 42A on chain H.
    Output is a list of tuples with chain_id, PDB_resid, resname,
    and index, which should be a proxy for Pose Numbering
    i.e. [('L', '30', 'TYR', '1'), ('H', '40', 'ALA', '225')]'''

    pdb=pdbstructure_from_file(pdb_file)

# Create a list of every residue within the PDB. Each tuple contains (chain_id, PDB_Number, ResName, Pose_Number) where Pose Numbering is assumed to be index+1 (starts from 0 in python, 1 in Rosetta)
    all_res_list=[]
    for ch in pdb.chains :
        for res in ch.residues :
            index=len(all_res_list)
            pose_num=len(all_res_list)+1
            #pose_num=index+1
            all_res_list.append( (ch.chain_name, res.resstring, res.resname, str(pose_num) ) )

    mutation_list = []
    mut_groups = re.split(",",input_residues)
#    print(mut_groups)
    for mg in mut_groups:
        '''iterate values over range (Check PDB for insertion codes, i.e. H20-H21A = [H20, H21, H21A]'''
        if "-" in mg :
            bounds = re.split("-",mg)
            start_resid_full=bounds[0]
            end_resid_full=bounds[1]
            chain_id=start_resid_full[0]
            start_resid=start_resid_full[1:]
            end_resid=end_resid_full[1:]
            # Identify the index value of start and end residues
            index_start=[i for i, v in enumerate(all_res_list) if ( (v[0] == chain_id) and (v[1] == start_resid) )].pop() # Should be pose numbering
            index_end=[i for i, v in enumerate(all_res_list) if ( (v[0] == chain_id) and (v[1] == end_resid) )].pop() # Should be pose numbering
            # Create a list of tuples for residues within that range
            mutation_range=[]
            x=index_start
            while (x <= index_end):
                mutation_list.append( ( all_res_list[x] ) )
                x = x + 1
        else : # Parse single residue
            chain_id=mg[0]
            resid=mg[1:]
            index=[i for i, v in enumerate(all_res_list) if ( (v[0] == chain_id) and (v[1] == resid) )].pop() # Should be pose numbering
            resname=( pdb.chainmap[ chain_id ].resmap[ resid ].resname )
            mutation_list.append( ( all_res_list[index] ) )
    for residue_tuple in mutation_list:
        for obj in residue_tuple:
            assert obj.isalnum()
#    print(mutation_list)
    return mutation_list

# Optional
def parse_symmetric_input(symmetric_input):
    resid_list = ""
    initial_groups = symmetric_input.split("[")
    initial_groups[1] = initial_groups[1].replace("]","")
#    print(initial_groups[0])
#    print(initial_groups[1])
    for chain_id in initial_groups[0]:
#        print(chain_id)
        '''parse residues and add chain_id in front'''
        mut_groups = re.split(",",initial_groups[1])
        for mg in mut_groups:
#            print(mg)
            '''treat a range differently (i.e. 20-22 = [A20-A22]'''
            if "-" in mg:
                bounds = re.split("-",mg)
                lower=chain_id+bounds[0]
                upper=chain_id+bounds[1]
                resid_list=resid_list + ',' + lower + '-' + upper
            else:
                resid_list=resid_list + ',' + chain_id + mg
#    print(resid_list[1:])
    return resid_list[1:] # The previous code starts resid_list with a ',' so this returns everything except for that character

''' Create a new list of tuples that matches mutation_list EXCEPT that matching residues from different chains have been combined so that the new tuple is [(chain_ids),(PDB_resid_num),(PDB_resname),(indexes)]'''
def symmetric_grouped_mutations(symmetric_input,mutation_list):
    symmetric_resid_list = []
#    print(symmetric_input)
    initial_groups = symmetric_input.split("[")
    initial_groups[1] = initial_groups[1].replace("]","")
    chains=initial_groups[0]
    # Get a list of residue (PDB numbering)
    all_pdb_num=[]
    for residue_tuple in mutation_list:
        if residue_tuple[0] == chains[0] :
            all_pdb_num.append(residue_tuple[1])
    # Create a new list of tuples that matches mutation_list EXCEPT that matching residues from different chains have been combined so that the new tuple is [(chain_ids),(PDB_resid_num),(PDB_resname),(indexes)]
    all_clustered_indexes=[]
    symmetric_mutation_list=[]
    for each_residue in all_pdb_num :
        clustered_index=""
        resname_three_lett=""
        for residue_tuple in mutation_list:
            if residue_tuple[1] == each_residue :
                clustered_index=clustered_index + ',' + residue_tuple[3]
                resname_three_lett=residue_tuple[2]
        all_clustered_indexes.append( (chains, each_residue, resname_three_lett, clustered_index[1:]) )
    return all_clustered_indexes

# Default to only keeping protein residues (ATOM), but if ligands should be kept, check HETATM lines for specific residues. Only the first two elements of each tuple will be used from keep_ligand_list. That list can be created by using parse_input_resid with input_ligand_residues
def trim_pdb(pdb_file, keep_ligand_list):
    with open('trimmed_input_protein.pdb', 'w') as trimmed_pdb:
        with open( pdb_file ) as f:
            for line in ( f.read() ).split('\n'):
                if line[0:4] == "ATOM" :
                     trimmed_pdb.write(line + '\n')
                elif line[0:6] == "HETATM" and ('MSE' in line[17:20]):
                     trimmed_pdb.write(line + '\n')
                elif keep_ligand_list is not None and line[0:6] == "HETATM" :
                    for keep_ligand in keep_ligand_list :
                        chain_id=keep_ligand[0]
                        resid=keep_ligand[1]
                        if line[21] == chain_id and (keep_ligand[1] in line[22:27]):
                            trimmed_pdb.write(line + '\n')

# Convert amino acid code from 1 letter to 3 letter #
dict_321 = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
           'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N',
           'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
           'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}

dict_123 = {v: k for k,v in list(dict_321.items())}

def aa_3_to_1(x):
    if len(x) % 3 != 0:
        raise ValueError('Input length should be a multiple of three')
    y = ''
    for i in range(len(x)//3):
            y += dict_321[x[3*i:3*i+3]]
    return y

def aa_1_to_3(x):
    if len(x) % 1 != 0:
        raise ValueError('Input length should be a multiple of three')
    y = ''
    for i in range(len(x)//1):
            y += dict_123[x]
    return y

### Build directory tree & create jobdefinition file for site saturation mutagenesis ###

# resname refers to the residues that the amino acid will be replaced with. 
def build_jobdef_directories(list_mutations, resname):

    xml_filename = 'jobdef.xml'
    with open (xml_filename, 'w') as xml_file: 
        xml_file.write("<JobDefinitionFile> \n")

    for current_pos in list_mutations:
        chain_id = current_pos[0]
        pdb_resid = current_pos[1]
        pose_resid = current_pos[3]
        position = chain_id + "[" + pdb_resid + "]"
#        print(chain_id)

        jobdef_template = '''\
  <Job nstruct="5">
    <Output>
      <PDB path="{position}/{mutation}"/>
    </Output>
    <SecondaryOutput>
      <ScoreFile path="{position}/{mutation}" filename="score.sc"/>
    </SecondaryOutput>
    <Options>
      <parser__script_vars value="pos1={pose_resid} aa={three_letter}"/>
    </Options>
  </Job>
'''
        for mutation in resname:
            # Create target directory if it doesn't exist (residue number / resname)
            dirName = '{}/{}'.format(position, mutation)
            if not os.path.exists(dirName):
                os.makedirs(dirName)
                #print(("Directory " , dirName ,  " Created "))
            else:    
                print(("Directory " , dirName ,  " already exists"))
            # Create XML file for RosettaScripts. The MutateResidue Mover requires the residue name in three-letter format.
            three_letter = aa_1_to_3(mutation)
            with open (xml_filename, 'a') as xml_file: 
                xml_file.write( jobdef_template.format(
                    position=position,
                    mutation=mutation,
                    pose_resid=pose_resid,
                    three_letter=three_letter ) )

    with open (xml_filename, 'a') as xml_file: 
        xml_file.write("</JobDefinitionFile> \n")

#### Analysis functions ####

### Running MPI creates multiple score files so combine into one before further analysis. Assumes score files are in current directory
def cat_scores(out_dir, score_file_prefix):
    # Generate a list of score files that match the score_file_prefix
    filenames = [ f for f in os.listdir(out_dir) if f.startswith(score_file_prefix)]
    # Combine all of them into one file
    with open(out_dir + 'mutant_scores.txt', 'w') as outfile:
        with open (out_dir + filenames[0], 'r') as infile:
            outfile.writelines(infile.readlines()[:2]) # Write the header from the first file (first two lines)
    with open(out_dir + 'mutant_scores.txt', 'a') as outfile:
        for fname in filenames:
            with open(out_dir + fname, 'r') as infile:
                outfile.writelines(infile.readlines()[2:]) # Skip the headers (first two lines)

def get_best_model_and_score(score_file):
    ''' select model with lowest total_score '''
    top_n = 1
    # Convert numbers to floats for parsing the score file; however some inputs are meant to be text (pdb names) so the input is returned either way
    def convertFloat(v):
        try: return float(v)
        except ValueError: return v

    score_table = []
    score_table_keys = []
    with open( score_file ) as f:
        lines = ( f.read() ).split('\n')
        score_table_keys = lines[1].split()[1:]  # ignoring first line, ignore first key (it just 'SCORE:')
        if not score_table_keys:
            print('Score table is empty!')
            sys.exit(1)
        score_table_keys[-1] = 'decoy'  # changing description → decoy
        lines = lines[:1] + sorted([l for l in lines[1:] if l and l.split()[0] == 'SCORE:' and l.split()[1] != 'total_score'], key=lambda l: float(l.split()[1]), )   # sorting lines by score, split based on total_score (l.split()[1] but skip the 1st line (Sequence:) and the header line ('total_score')
        score_table = [ dict( list(zip(score_table_keys, list(map(convertFloat, l.split()[1:])))) )  for l in lines[1:]]
        score_table_keys = score_table_keys[-1:] + score_table_keys[:-1]  # making 'decoy' the first column
        best_model = [ m['decoy'] for m in score_table[:top_n] if type(m['decoy'])==str]
    # FROM ROSIEv1:    best_model = [ m['decoy'] for m in score_table[:top_n] if type(m['decoy'])==str  and  '_mut_' in m['decoy'] ]  # we need to check if '_mut_' is in decoy name to avoid rare cases when line is misformed (HPC writing issue?)
        best_score = [ m['total_score'] for m in score_table[:top_n] if type(m['total_score'])==float ]
        return best_model, best_score

### Collect best models and create table of delta_scores (Total score of Mutant - WT)
def analysis(mutation_list, resname, score_file_prefix):
    # Create directory for PDBs
    results_dir = './results/'
    score_files_dir = '{}score_files/'.format(results_dir)
    pdb_models_dir = '{}pdb_models/'.format(results_dir)
    if not os.path.exists(results_dir):
        print(("Created " , results_dir ))
        os.makedirs(results_dir)
        os.makedirs(score_files_dir)
        os.makedirs(pdb_models_dir)
    else:
        print(("Directory " , results_dir , " already exists, placing results in existing directory."))

    with open(results_dir + 'results.csv', 'w') as delta_scores:
        for test in mutation_list: # If symmetric mutations, more than one chain will be provided (i.e. AB mutates residues on both A and B chains). The WT_resnum will be the same for both but the Rosetta_Num will vary based on num of chains 
             num_chains=(len(test[0]))
        start_rosetta_num_string=",Rosetta Number"
        final_rosetta_num_string=start_rosetta_num_string*num_chains # Edit the header based on the number of chains
        delta_scores.write("Mutation Name,Delta Energy (mutant-WT),Chain ID,WT Residue,Position,Mutant Residue" + final_rosetta_num_string + ",Model Name")
        ''' 1) determine the score for the WT residue, 2) Subtract each mutant score from the WT score and move the best scoring models to the results_dir'''
        for current_pos in mutation_list:
            chain_id = current_pos[0]
            resid = current_pos[1]
            position = chain_id + '[' + resid + ']'
            pose_num = current_pos[3] # Rosetta numbering, i.e. resid 1-x regardless of PDB numbering scheme

            ''' Determine the score of the WT residue at the given position '''
            WT_three_lett = current_pos[2]
            WT_one_lett = aa_3_to_1(WT_three_lett)
            out_dir = './{}/{}/'.format(position, WT_one_lett)
            # MPI generates multiple score files, so combine them into a single file
            cat_scores(out_dir, score_file_prefix) # This generates the file named 'mutant_scores.txt' for WT residue
            score_file = out_dir + 'mutant_scores.txt'
            WT_best_model, WT_best_score = get_best_model_and_score(score_file)

            for mutation in resname:
                assert mutation.isalnum()
                '''Calculate delta scores and collect the best models'''
                out_dir = './{}/{}/'.format(position, mutation)
                cat_scores(out_dir, score_file_prefix) # This generates the file named 'mutant_scores.txt'
                score_file = out_dir + 'mutant_scores.txt'
                mut_best_model, mut_best_score = get_best_model_and_score(score_file)
#                print(("Mut_Best_Score"), mut_best_score[0], ("WT_Best_Score"), WT_best_score[0])
                delta_mut_score = mut_best_score[0] - WT_best_score[0]

		# Collect score and pdb files
                mutant_name='{}[{}{}{}]'.format(chain_id, WT_one_lett, resid, mutation)
                escaped_mutant_name='{}\[{}{}{}\]'.format(chain_id, WT_one_lett, resid, mutation)
                best_decoy = out_dir + mut_best_model[0] + '.pdb'
                shutil.copy(best_decoy, pdb_models_dir + mutant_name + '.pdb')
                shutil.copy(score_file, score_files_dir + mutant_name + '_scores.txt')

		# Write to delta_score file. Generating a heatmap reads this file. So if this format changes (rearranging columns), the score_col values should be updated.
                delta_scores.write('\n' + mutant_name + ',' + str( format(delta_mut_score,'.2f')) + ',' + chain_id + ',' + WT_one_lett + ',' + resid + ',' + mutation + ',' + pose_num + ',' + escaped_mutant_name + '.pdb')

################## START HEATMAP SECTION #######################
# set the colormap and centre the colorbar on a midpoint that isn't in the middle
class MidpointNormalize(colors.Normalize):
    """ Normalise the colorbar so that diverging bars work there way either side from a prescribed midpoint value)
        e.g. im=ax1.imshow(array, norm=MidpointNormalize(midpoint=0.,vmin=-40, vmax=100))"""
    def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
        self.midpoint = midpoint
        colors.Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        # I'm ignoring masked values and all kinds of edge cases to make a
        # simple example...
        x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
        return numpy.ma.masked_array(numpy.interp(value, x, y), numpy.isnan(value))

def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw={}, cbarlabel="", **kwargs):
    """Create a heatmap from a numpy array and two lists of labels.
    Parameters
    ----------
    data
        A 2D numpy array of shape (N, M).
    row_labels
        A list or array of length N with the labels for the rows.
    col_labels
        A list or array of length M with the labels for the columns.
    ax
        A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
        not provided, use current axes or create a new one.  Optional.
    cbar_kw
        A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    **kwargs
        All other arguments are forwarded to `imshow`."""
    if not ax:
        ax = plt.gca()
    # Plot the heatmap
    im = ax.imshow(data, **kwargs)
    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")
    # We want to show all ticks...
    ax.set_xticks(numpy.arange(data.shape[1]))
    ax.set_yticks(numpy.arange(data.shape[0]))
    # ... and label them with the respective list entries.
    ax.set_xticklabels(col_labels)
    ax.set_yticklabels(row_labels)
    # Let the horizontal axes labeling appear on bottom.
    ax.tick_params(top=False, bottom=True,
                   labeltop=False, labelbottom=True)
    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=90, ha="left",
             rotation_mode="default")
    # Turn spines off and create white grid.
    for edge, spine in list(ax.spines.items()):
        spine.set_visible(False)
    ax.set_xticks(numpy.arange(data.shape[1])+0.5, minor=True)
    ax.set_yticks(numpy.arange(data.shape[0])+0.5, minor=True)
#    ax.grid(which="minor", color="w", linestyle='-', linewidth=1)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=0.25)
    ax.tick_params(which="both", bottom=False, left=False)
    return im, cbar

def annotate_heatmap(im, data_min, data_max, data=None, valfmt="{x:.2f}",
                     textcolors=["white", "black"],
                     **textkw):
    """A function to annotate a heatmap.
    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.
    valfmt
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        `matplotlib.ticker.Formatter`.  Optional.
    textcolors
        A list or array of two color specifications.  The first is used for
        values below a threshold, the second for those above.
    **kwargs
        All other arguments are forwarded to each call to `text` used to create
        the text labels."""
    if not isinstance(data, (list, numpy.ndarray)):
        data = im.get_array()
    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)
    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)
    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(data[i, j] < (data_max/3) and data[i, j] > (data_min/3))])
            #If WT residue, print "WT" instead of score
            if float(data[i, j]) == 0:
                text = im.axes.text(j, i, "WT", **kw)
            # If positive score, mutations are unfavorable so leave field blank
            elif float(data[i, j]) > 0:
                text = im.axes.text(j, i, " ", **kw)
            # If negative score, print score
            else:
                text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)
    return texts

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            print((data[i, j]))
            if int(data[i, j] > 0):
                data[i, j]=1
                print((data.shape))

def heatmap_gen(mutation_list, resname):
    # Generate a dict of lists that includes x-axis (aa position), y-axis (mutation residue name), and each resname (i.e. A,C,D...) contains the delta_score for each position
    results_dir = './results/'

    mut_scores_dict={}
    mut_scores_dict.setdefault('x_axis', []) # X axis is a list of residue numbers
    mut_scores_dict.setdefault('x_axis_table', []) # X axis is a list of residue numbers
    for current_pos in mutation_list:
        chain_id = current_pos[0]
        resid = current_pos[1]
        WT_three_lett = current_pos[2]
        WT_one_lett = aa_3_to_1(WT_three_lett)
        position_WT = chain_id + '[' + resid + ']  ' + WT_one_lett
        position = chain_id + '[' + resid + ']' 
        mut_scores_dict['x_axis'].append(position_WT)
        mut_scores_dict['x_axis_table'].append(position)
    mut_scores_dict.setdefault('y_axis', []) # Y Axis is a list of residue names
    for mutation in resname:
            mut_scores_dict['y_axis'].append(mutation) # Collect resnames for y-axis

    for current_pos in mutation_list:
        target_chain_id = current_pos[0]
        target_resid = current_pos[1]
        for mutation in resname: # Do this for each resname (i.e. A, C, etc.)
            mut_scores_dict.setdefault(mutation, [])

            all_scores=open(results_dir + 'results.csv', 'r').read()
            for line in all_scores.split('\n'):
                score_col = re.split(",",line)
                if score_col[2] == target_chain_id and score_col[4] == target_resid and score_col[5] == mutation :
                    mut_scores_dict[mutation].append(score_col[1])
                    break # Makes the for loops a little faster for large files, still inefficient though
    # Create a 2D array of the scores based on the dict of lists for each mutation (y-axis = mutation, x-axis = aa position)
    count=1
    for mutation in resname:
        if count == 1 :
            score_2d_array=numpy.array([mut_scores_dict[mutation]]).astype(numpy.float)
        else :
            score_2d_array=numpy.vstack((score_2d_array,mut_scores_dict[mutation])).astype(numpy.float)
        count=count+1

    # Plot the 2d array as a heatmap
    # Scale font size by longest side of heatmap
    max_length=max(len(mutation_list), len(resname))
    if max_length >= 20:
        font_size_var=5
    elif max_length >=15:
        font_size_var=6
    elif max_length >=10:
        font_size_var=8
    elif max_length >=5:
        font_size_var=10
    elif max_length >=1:
        font_size_var=12

    matplotlib.rcParams.update({'font.size': font_size_var})
#    plt.rcParams["font.family"] = "monospace" # To change font styles
    data_min=numpy.amin(score_2d_array)
    data_max=1
#    data_max=numpy.amax(score_2d_array)
    fig, ax = plt.subplots()
    im, cbar = heatmap(score_2d_array, mut_scores_dict['y_axis'], mut_scores_dict['x_axis'], ax=ax, cmap="RdBu", cbarlabel=r'$\Delta$E (REU)', norm=MidpointNormalize(midpoint=0., vmin=data_min, vmax=data_max))
    texts = annotate_heatmap(im, valfmt="{x:.1f}", data_min=data_min, data_max=data_max)
    #ax.set_title("Site Saturation Mutagenesis Delta Scores (WT-Mutant Total Scores)")
    fig.tight_layout()
    plt.savefig(results_dir + 'heatmap_image.pdf', dpi=300, bbox_inches='tight')

    x=numpy.array([mut_scores_dict['x_axis_table']])
    y=numpy.array([mut_scores_dict['y_axis']])
    full_2d_array=numpy.vstack((x.astype(numpy.str),score_2d_array.astype(numpy.str)))
    y2_axis=numpy.insert(y,[0],[['_']], axis=1)
    full_2d_array=numpy.concatenate((y2_axis.T.astype(numpy.str), full_2d_array), axis=1)
    numpy.savetxt(results_dir + 'heatmap_table.txt',full_2d_array, fmt='%8s')
    print("HEATMAP GENERATED")

################################# Validators #################################

def input_position_validator(string_input):
    allowed_chars = set('[]ABCDEFGHIJKLMNOPQRSTUVWXYZ-,:1234567890')
    for c in string_input:
        if c not in allowed_chars:
            error = ' illegal characters, should only be a range of positions (i.e. H[1,10-20],L[23]).'
            return error

def upper_alpha_validator(string_input):
    # Must be a string with only capitalized letters
    input_string = string_input
    check_letters = input_string.isalpha()
    check_upper = input_string.isupper()

    if not (check_letters and check_upper):
        error = ' should only contain upper-case letters.'
        return error

def aa_validator(string_input):
    # Must be a string with only amino acid letters
    for c in string_input:
        if c not in 'ACDEFGHIKLMNPQRSTVWY':
            print('The amino acid substitutions should only contain upper-case letters that represent amino acids (ACDEFGHIKLMNPQRSTVWY).')
            sys.exit(1)

def symmetric_validator(symmetric_option):
    initial_groups = symmetric_option.split("[")
    initial_groups[1] = initial_groups[1].replace("]","")
    error = upper_alpha_validator(initial_groups[0])
    if error:
        error = 'The input for symmetric mutations is incorrect. Outside of the brackets' + error
        return error
    if len(initial_groups[0]) <= 1:
        error_message = 'The input for symmetric mutations must designate more than one chain.'
        return error_message
    try:
        symmetric_mutations = parse_symmetric_input(symmetric_option)
    except:
        error_message = 'Error parsing input for symmetric mutations.' # This is a catch-all for other input errors
        return error_message

def check_path_validator(filename):
    #assert '..' not in filename # Avoid malicious redirects #ROSIE-only
    #allowed_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ-abcdefghijklmnopqrstuvwxyz_1234567890.')
    #for c in filename:
    #    if c not in allowed_chars:
    #        print('Invalid path to file.')
    #        sys.exit(1)

    if os.path.isfile('./' + filename):
        pass
    else:
        error = 'Error locating PDB file: ./' + filename + '\n Is the filename correct?' # This is a catch-all in case the PDB file doesn't exist
        print(error)
        sys.exit(1)

def check_wt_res(mutation_list, resname):
    for current_pos in mutation_list:
        WT_three_lett = current_pos[2]
        WT_one_lett = aa_3_to_1(WT_three_lett)
        if (WT_one_lett not in resname):
            error = 'If amino acids substitutions are designated, the WT residue for each position must be represented to calculate delta_scores.'
            print(error)
            sys.exit(1)
        else:
            wt_check = 1
    return wt_check

def validate_build_and_analyze(pdb_file, input_resnum, aa_subs_option, symmetric_option):

    check_path_validator(pdb_file)

    if input_resnum != '' :
        error = input_position_validator(input_resnum)
        if error:
            error = 'The input positions for mutagenesis contains' + error
            print(error)
            sys.exit(1)
        # Check the PDB file for the specified positions
        try:
            input_resnum=parse_brackets_input_resid(input_resnum)
            list_mutations=parse_input_resid(pdb_file, input_resnum)
        except:
            error = 'One of the positions was not found in the provided PDB file. Please check your input, you may be using an incorrect numbering scheme.'
            print(error)
            sys.exit(1)
    else :
        input_resnum = ''

    # Optional, symmetric mutations
    if symmetric_option != '' :
        error = input_position_validator(symmetric_option)
        if error:
            error = 'The input for symmetric mutations contains' + error
            print(error)
            sys.exit(1)
        error = symmetric_validator(symmetric_option) # Format check
        if error:
            print(error)
            sys.exit(1)
        # Check that the user-provided input is in the proper format AND each residue is present within the PDB file
        sym_mutation_list=parse_symmetric_input(symmetric_option)
        try:
            list_mutations=parse_input_resid(pdb_file, sym_mutation_list)
        except:
            error = 'One of the positions in the symmetric input was not found in the provided PDB file. Please check your input, you may be using an incorrect numbering scheme.'
            print(error)
            sys.exit(1)
    else :
        symmetric_option = ''

    # Optional, user decides which aa substitutions to make
    if aa_subs_option != '' :
        aa_validator(aa_subs_option) # Format check
        check_wt_res(list_mutations, aa_subs_option)
    else :
        aa_subs_option = ''

#    return pdb_file, input_resnum, aa_subs_option, symmetric_option

def parse_build_analyze_inputs(pdb_file, input_resnum, aa_subs_option, symmetric_option):

    # Optional, user decides which aa substitutions to make
    if aa_subs_option is not '':
        resname = [char for char in aa_subs_option]
    else:
        # Can exclude mutations for saturation mutagenesis here (i.e. to save speed, skip Pro, etc.)
        #resname = [ "A", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y" ]  # These are sorted alphabetically, exclude Cys
        resname = [ "G", "P", "C", "A", "V", "I", "L", "M", "F", "Y", "W", "S", "T", "N", "Q", "H", "K", "R", "D", "E" ] # These are sorted by type (special, hydrophobic, hydrophbilic, charge), default includes all amino acids
    # Optional, symmetric mutations
    if symmetric_option is not "":
        sym_mutation_list=parse_symmetric_input(symmetric_option)
        mutation_list=parse_input_resid(pdb_file, sym_mutation_list)
        sym_mutation_string=parse_symmetric_input(symmetric_option) #(i.e. AB:257-261 becomes A257-A261,B257-B261)
        sym_mutation_list=parse_input_resid(pdb_file, sym_mutation_string) # (i.e. complete tuple list of all residues on all chains(
        list_mutations=symmetric_grouped_mutations(symmetric_option,sym_mutation_list)
    # If symmetric_option is off, check input_mutations for proper formatting AND whether each residue is present within the PDB file
    else:
        input_resnum=parse_brackets_input_resid(input_resnum)
        list_mutations=parse_input_resid(pdb_file, input_resnum)

#    for residue_tuple in list_mutations:
#        for obj in residue_tuple:
#            assert obj.isalnum() # This assertion fails on symmetric inputs which have a comma
    for letter in resname:
        assert letter.isalpha()
    return list_mutations, resname

################################# Primary Functions ########################################

##### Mode 1: Prepare pdb file for relax by removing all hetero atoms except for any specified by ligand_option #####
def trim(pdb_file, ligand_option):

    check_path_validator(pdb_file)

    if ligand_option != '' :
        error=input_position_validator(ligand_option)
        if error:
            error = 'The ligand position contains' + error
            print(error)
            sys.exit(1)
        # Check the PDB file for the specified positions
        try:
            ligand_option=parse_brackets_input_resid(ligand_option)
            keep_ligand_list = parse_input_resid(pdb_file, ligand_option)
        except:
             error = 'One of the LIGAND positions was not found in the provided PDB file. Please check your input, you may be using an incorrect numbering scheme.'
             print(error)
             sys.exit(1)
    else :
        keep_ligand_list = ""

    trim_pdb(pdb_file, keep_ligand_list) # Creates the file 'trimmed_input_protein.pdb' in the current directory

##### Mode 2: Build PM inputs (directory tree and jobdefinition file) #####
def build(pdb_file, input_resnum, aa_subs_option, symmetric_option):
    # To avoid code duplication, a separate function for validating both build and analyze was created
    validate_build_and_analyze(pdb_file, input_resnum, aa_subs_option, symmetric_option)
    list_mutations, resname = parse_build_analyze_inputs(pdb_file, input_resnum, aa_subs_option, symmetric_option)
    gen_RScripts(pdb_file)
    build_jobdef_directories(list_mutations, resname)

##### Mode 3: Analyze results (calculate delta_scores, collect best models, and generate heatmap) #####
def analyze(pdb_file, input_resnum, aa_subs_option, symmetric_option):
    score_file_prefix = "score"
    # To avoid code duplication, a separate function for validating both build and analyze was created
    validate_build_and_analyze(pdb_file, input_resnum, aa_subs_option, symmetric_option)
    list_mutations, resname = parse_build_analyze_inputs(pdb_file, input_resnum, aa_subs_option, symmetric_option)
    analysis(list_mutations, resname, score_file_prefix)
    heatmap_gen(list_mutations, resname)

############################### Define Inputs ####################################

mode = ''
pdb_file = ''
input_resnum = ''
aa_subs_option = ''
symmetric_option = ''
ligand_option = ''

score_file_prefix = "score"

CommandArgs = sys.argv[1:]

for arg in CommandArgs:
    if arg == '-mode':
        mode = CommandArgs[CommandArgs.index(arg)+1]
    elif arg == '-pdb':
        pdb_file = CommandArgs[CommandArgs.index(arg)+1]
    elif arg == '-pos':
        input_resnum = CommandArgs[CommandArgs.index(arg)+1]
    elif arg == '-subs':
        aa_subs_option = CommandArgs[CommandArgs.index(arg)+1]
    elif arg == '-sym':
        symmetric_option = CommandArgs[CommandArgs.index(arg)+1]
    elif arg == '-lig':
        ligand_option = CommandArgs[CommandArgs.index(arg)+1]

if ( not mode ):
    error_message = """
############################## ERROR ##############################

Error: Must include -mode

############################## ERROR ##############################

Usage Example 1: python stabilizing_pm.py -mode trim -pdb input_file.pdb
Usage Example 2: python stabilizing_pm.py -mode build -pdb input_file.pdb -pos H[1,10-20],L[23] -subs ADEFGHIKLMNQRSTVWY
Usage Example 3: python stabilizing_pm.py -mode analyze -pdb input_file.pdb -pos H[1,10-20],L[23] -subs ADEFGHIKLMNQRSTVWY

"""
    print(error_message)
    raise SystemExit

if ( not pdb_file ):
    error_message = """
############################## ERROR ##############################

Error: Must include -pdb 

############################## ERROR ##############################

Usage Example 1: python stabilizing_pm.py -mode trim -pdb input_file.pdb
Usage Example 2: python stabilizing_pm.py -mode build -pdb input_file.pdb -pos H[1,10-20],L[23] -subs ADEFGHIKLMNQRSTVWY
Usage Example 3: python stabilizing_pm.py -mode analyze -pdb input_file.pdb -pos H[1,10-20],L[23] -subs ADEFGHIKLMNQRSTVWY

"""
    print(error_message)
    raise SystemExit

if ( ( (mode == "build") or (mode == "analyze") ) and ( (not input_resnum) and (not symmetric_option) ) ):
    error_message = """
############################## ERROR ##############################

Error: Which positions do you want to mutate?

If mode = 'build'/'analyze', then either '-pos' or '-sym' are required

############################## ERROR ##############################

Usage Example: python stabilizing_pm.py -mode build -pdb input_file.pdb -pos H[1,10-20],L[23] -subs ADEFGHIKLMNQRSTVWY

"""
    print(error_message)
    raise SystemExit

################################# Execute Functions ########################################

### Mode 1: Prepare pdb file for relax by removing all hetero atoms except for any specified by ligand_option
elif mode == "trim":
    trim(pdb_file, ligand_option)
### Mode 2: Build PM inputs (directory tree and jobdefinition file)
elif mode == "build":
    build(pdb_file, input_resnum, aa_subs_option, symmetric_option)
### Mode 3: Analyze results (calculate delta_scores, collect best models, and generate heatmap)
elif mode == "analyze":
    analyze(pdb_file, input_resnum, aa_subs_option, symmetric_option)

Please cite ...

These simulations maintain sequence symmetry across the GCN4 homodimer. Note: To run symmetric mutations with the RosettaScripts for Mutation Clusters (MC), the chains must be identical (same length, as well). For that reason, residues 32 and 33 were removed from chain B of PDB ID: 4dmd before simulations.

# Clean pdb file (removes ligands by default, check options to keep). Also deleted residues B[32,33] with a text editor
python3.5 ../stabilizing_mc.py -mode trim -pdb 4dmd.pdb

# Build directory tree and input files
python3.5 ../stabilizing_mc.py -mode build -sym AB[3,17,21] -fav 0,5 -pdb trimmed_input_protein.pdb

# Relax the structure - must end with Cartesian minimization (check rs_pm.xml to see)
cp trimmed_input_protein.pdb relax/

# Generate a job submission file in the relax directory, then submit the job. The provided run.sh file is made for our local SLURM cluster but you will probably need a different file for submitting the RosettaScripts
sbatch relax/run.sh

# Identify the best scoring pdb file and copy it to current directory
cp relax/trimmed_input_protein_0002.pdb ./trim_tree_relaxed.pdb

# Generate a job submission file in the relax directory, then submit the job. The provided run.sh file is made for our local SLURM cluster but you will probably need a different file for submitting the RosettaScripts
sbatch run.sh

# Analyze the results, check the results/ directory for scores and a heatmap (negative is favorable)
python3.5 ../stabilizing_mc.py -mode analyze -sym AB[3,17,21] -fav 0,5 -pdb trim_tree_relaxed.pdb


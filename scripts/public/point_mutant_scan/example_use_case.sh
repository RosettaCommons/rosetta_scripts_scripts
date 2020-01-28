#!/bin/bash

# Say we have a protein with 2 chains (A and B), each with 50 residues labeled 10-59 in the PDB

pose="TODO.pdb"

for chain in A B; do
    for seqpos in {10..59}; do
	for aa in ALA ARG ASN ASP CYS GLU GLN GLY HIS ILE LEU LYS MET PHE PRO SER THR TRP TYR VAL; do
	    rosetta_scripts.default.linuxgccrelease -s $pose -parser:protocol point_mutant_scan.xml -parser:script_vars focused_res=$seqpos focused_chain=$chain target_aa=$aa -out:prefix ${chain}${seqpos}_${aa}
	done
    done
done

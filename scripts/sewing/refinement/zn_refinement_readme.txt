This script is intended to be used for refinement after the zn_append.xml script. It constrains zinc binding sites to their ideal geometries, constrains loop residues to their native identities, and 
performs FastDesign using LayerDesign and with all zinc binding and hydrogen bonding residues held fixed. Before FastDesign, we perform an initial sidechain design step to remove large clashes and 
a cartesian minimization step to fix bad bond lengths/angles at chimerization points.
Between zn_append and zn_refinement, I ran the backside_hbond_finder app (currently found in apps/pilot/guffysl) to place backside hydrogen bonds for all zinc binding residues and to fix any
problems with the tautomeric state of the histidines before refinement.
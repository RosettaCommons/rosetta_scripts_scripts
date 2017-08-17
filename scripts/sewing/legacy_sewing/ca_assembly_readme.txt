These scripts use legacy SEWING to design an assembly around an EF hand calcium binding site.
Since legacy SEWING has no knowledge of ligands, the calcium-binding residues of each input site
must be preserved individually using the -keep_model_residues flag. Users must also define the 
beginnings and ends of each secondary structure element using the -pose_segment_starts and -pose_segment_ends
flags.
The model and score file names refer to legacy SEWING model and score files generated using the sewing_hasher application.
The calcium_motif_score option sets the weight of the CalciumMotifScore in legacy SEWING forces packing of all segments of the starting site with other parts of the assembly. This effectively forces AppendAssemblyMover to build off both ends of the starting structure. By default this weight is zero. Note that scoring weights are not accessible through RosettaScripts in legacy SEWING.

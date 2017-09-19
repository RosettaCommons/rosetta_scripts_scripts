# List all .xml files in all subdirectories of the scripts/ directory that should be run through
# the validator test: these tests will then be guaranteed by the testing server not to go out of
# date. If someone changes the underlying Mover/Filter used by one of these scripts, they will
# have to update the scripts that rely on them.


scripts_to_be_validated = [
    "scripts/pilot/example/an_example_for_testing_purposes/example_valid.xml",
    "scripts/pilot/fold_and_dock_membrane_single_spanning_homodimers/fnd_homo.xml",
    "scripts/public/sewing/refinement/zn_refinement.xml",
    "scripts/public/rotamer_recovery/ex1ex2_repack_t4400lt200_betaNov15_npdhb/rotamer_recovery_via_feature_analysis.xml",
    "scripts/public/feature_analysis/interface_feature_analysis/interface_features.xml",
    "scripts/public/feature_analysis/hbond_features_from_relaxed_decoys_npdhb_potential/hbond_feature_extraction.xml",
    "scripts/public/sewing/refinement/HR1B_refinement.xml",
    "scripts/public/sewing/refinement/HR1B_refinement_remove_partner.xml"
]
#note - do not put a trailing comma on the closing ] if you are doing multiline editing to add the trailing commas to the 10 scripts you just added - it will convert the list to a tuple and blow up the world

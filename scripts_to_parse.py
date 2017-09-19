# List all .xml files in all subdirectories of the scripts/ directory that should be run
# through the "parse-my-tag" test. These scripts can be placed into the same a directory
# as a flags file of the same name (e.g. "example.xml" could be paired with "example.flags")
# if additional flags are needed in order for the script to successfully make it through a
# complete parsing.

scripts_to_be_parsed = [
"scripts/pilot/example/an_example_for_testing_purposes/example_valid.xml",
"scripts/public/protein_interface_design/single_sided_dock_design_minimize_interface_protocol/ddmi.xml",
"scripts/public/enzymedesign/enzdes_bookchapter_example.xml",
"scripts/public/docking/lrf_docking.xml",
"scripts/public/analysis/interface/analyze_electrostatics_in_helix_trimer.xml",
"scripts/public/analysis/interface/custom_interface_filter1.xml",
"scripts/public/analysis/interface/custom_interface_filter2.xml",
"scripts/public/analysis/interface/delete_chain_then_interface_analyzer.xml",
"scripts/public/docking/lrf_docking_with_autointerfacecst.xml",
"scripts/public/docking/lrf_docking_with_usersuppliedconstraints.xml",
"scripts/public/docking/terrible_analyze_mutations_at_interface.xml",
"scripts/public/homology_modeling/hybridize_example.xml",
"scripts/public/loop_modeling/loop_grower.xml",
"scripts/public/protein_hacking/helix_extend_with_threading.xml",
"scripts/public/protein_hacking/helix_extender.xml",
]
#note - do not put a trailing comma on the closing ] if you are doing multiline editing to add the trailing commas to the 10 scripts you just added - it will convert the list to a tuple and blow up the world

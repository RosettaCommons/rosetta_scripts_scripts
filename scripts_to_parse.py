# List all .xml files in all subdirectories of the scripts/ directory that should be run
# through the "parse-my-tag" test. These scripts can be placed into the same a directory
# as a flags file of the same name (e.g. "example.xml" could be paired with "example.flags")
# if additional flags are needed in order for the script to successfully make it through a
# complete parsing.

scripts_to_be_parsed = [
    "scripts/pilot/example/an_example_for_testing_purposes/example_valid.xml",
    "scripts/public/protein_interface_design/single_sided_dock_design_minimize_interface_protodocol/ddmi.xml",
    "scripts/public/enzymedesign/enzdes_bookchapter_example.xml",
    "scripts/public/docking/lrf_docking.xml",
]

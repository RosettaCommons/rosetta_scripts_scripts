# List all .xml files in all subdirectories of the scripts/ directory that should not
# be tested either in the validation- or parse-my-tag tests here.
# There are three classes of XML files that belong in this list.
# 1. Files that should just not be tested because they are out of date with the XSD
# and cannot readily be made up to date using the rewriter (perhaps one of the
# movers has changed significantly since the script was used)
# 2. Files that are xi:included from other (tested) XML files, but that do not start
# with <RosettaScripts> and so would not pass a validation test on their own, and
# 3. Files that are symlinked from some subdirectory of the main/tests/integration_tests
# directory, and that are thus fully tested in a different system.
#
# This script defines a large list that will be imported by other scripts

scripts_not_tested = [
    "scripts/pilot/example/an_example_for_testing_purposes/example_invalid.xml",
    "scripts/public/sewing/append/GTPase_inhibitors/HR1A_RhoA_LOV_cage/HR1A_RhoA_LOV_cage.xml",
    "scripts/public/sewing/append/GTPase_inhibitors/HR1B_Rac1_LOV_cage/HR1B_Rac1_LOV_cage.xml",
    "scripts/public/sewing/append/GTPase_inhibitors/Kalirin_zLock_2/Kalirin_zLock_2.xml",
    "scripts/public/sewing/refinement/HEM_refinement.xml",
    "scripts/public/sewing/legacy_sewing/ca_assembly.xml",
    "scripts/public/sewing/append/HEM_append.xml",
    "scripts/public/sewing/append/zn_append_script.xml",
    "scripts/public/sewing/ligand_contacts/zn_tetra_script.xml",
    "scripts/public/sewing/ligand_contacts/zn_sewing_script.xml",
]

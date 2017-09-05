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
]

# List all .xml files in all subdirectories of the scripts/ directory that should be run through
# the validator test: these tests will then be guaranteed by the testing server not to go out of
# date. If someone changes the underlying Mover/Filter used by one of these scripts, they will
# have to update the scripts that rely on them.


scripts_to_be_validated = [
   "scripts/pilot/example/an_example_for_testing_purposes/example_valid.xml",
]

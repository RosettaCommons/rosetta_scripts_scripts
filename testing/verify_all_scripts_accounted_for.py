# This script, when run in the rosetta_scripts_scripts/ base directory, will recursively search
# through the scripts/ directory for all .xml files that it can find and then compare these against
# the lists of xmls in the three files in the base directory:
# untested_scripts.py
# scripts_to_validate.py
# scripts_to_parse.py
# This script will return 0 iff
# 1. all scripts listed in the three files above are found in the source directory, and
# 2. all the xml files that are found have been listed in at least one of the above scripts

import os, sys

from untested_scripts import *
from scripts_to_validate import *
from scripts_to_parse import *

all_listed_scripts = set( scripts_to_be_validated + scripts_to_be_parsed + scripts_not_tested )
all_found_files = set( filter( lambda x : len(x) >= 4 and x[-4:] == ".xml", [ os.path.join( x[0], y ) for x in os.walk( "scripts" ) for y in x[2] ] ))

for x in all_found_files :
    print( "Found: " + x )


all_good = True
for script in all_listed_scripts :
    if script not in all_found_files :
        all_good = False
        print( "Script '" + script + "' was not found in the source tree" )

for script in all_found_files :
    if script not in all_listed_scripts :
        all_good = False
        print( "Script '" + script + "' was not listed in any of the three files listing what scripts to test and how" )

if all_good : sys.exit(0)
else :        sys.exit(1)


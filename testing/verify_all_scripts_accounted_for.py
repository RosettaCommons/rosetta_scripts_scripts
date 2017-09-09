#!/usr/bin/env python
# -*- coding: utf-8 -*-
# :noTabs=true:

# (c) Copyright Rosetta Commons Member Institutions.
# (c) This file is part of the Rosetta software suite and is made available under license.
# (c) The Rosetta software is developed by the contributing members of the Rosetta Commons.
# (c) For more information, see http://www.rosettacommons.org. Questions about this can be
# (c) addressed to University of Washington CoMotion, email: license@uw.edu.


# This script, when run in the rosetta_scripts_scripts/ base directory, will recursively search
# through the scripts/ directory for all .xml files that it can find and then compare these against
# the lists of xmls in the three files in the base directory:
# untested_scripts.py
# scripts_to_validate.py
# scripts_to_parse.py
# This script will return 0 iff
# 1. all scripts listed in the three files above are found in the source directory, and
# 2. all the xml files that are found have been listed in at least one of the above scripts

import os, sys, subprocess

from untested_scripts import *
from scripts_to_validate import *
from scripts_to_parse import *

import json

all_listed_scripts = set( scripts_to_be_validated + scripts_to_be_parsed + scripts_not_tested )
all_found_files = set( filter( lambda x : len(x) >= 4 and x[-4:] == ".xml", [ os.path.join( x[0], y ) for x in os.walk( "scripts" ) for y in x[2] ] ))

#for x in all_found_files :
#    print( "Found: " + x )

scripts_not_found = []
scripts_not_listed = {}

all_good = True
for script in all_listed_scripts :
    if script not in all_found_files :
        all_good = False
        scripts_not_found.append( script )

for script in all_found_files :
    if script not in all_listed_scripts :
        all_good = False
        blame_command = ( "git blame " + script ).split()
        child = subprocess.Popen( blame_command, stdout=subprocess.PIPE )
        blame_out, blame_err = child.communicate()
        blame_lines = blame_out.split("\n")
        last_line = blame_lines[-2]

        author = last_line[ (last_line.find("(")+1) : last_line.find( ")") ].split("20")[0] # Y3K Bug here!
        #print( last_line )
        #print( author )
        scripts_not_listed[ script ] = author

json.dump(
    { "success" : all_good, "scripts_not_found" : scripts_not_found, "scripts_not_listed" : scripts_not_listed },
    open( "verify_all_scripts_accounted_for_result.json", 'w' ),
    sort_keys = True )

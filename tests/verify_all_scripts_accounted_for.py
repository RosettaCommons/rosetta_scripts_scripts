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

from __future__ import print_function

import os, sys, imp, json, subprocess
import validate_all_scripts
from argparse import ArgumentParser


def execute(message, command_line, return_='status', until_successes=False, terminate_on_failure=True, silent=False, silence_output=False):
    if not silent: print(message);  print(command_line); sys.stdout.flush();
    while True:

        p = subprocess.Popen(command_line, bufsize=0, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, errors = p.communicate()

        output = output + errors

        output = output.decode(encoding="utf-8", errors="replace")

        exit_code = p.returncode

        if exit_code  or  not (silent or silence_output): print(output); sys.stdout.flush();

        if exit_code and until_successes: pass  # Thats right - redability COUNT!
        else: break

        print( "Error while executing {}: {}\n".format(message, output) )
        print("Sleeping 60s... then I will retry...")
        sys.stdout.flush();
        time.sleep(60)

    if return_ == 'tuple': return(exit_code, output)

    if exit_code and terminate_on_failure:
        print("\nEncounter error while executing: " + command_line)
        if return_==True: return True
        else: print("\nEncounter error while executing: " + command_line + '\n' + output); sys.exit(1)

    if return_ == 'output': return output
    else: return False

def find_all_xml_scripts_in_repo() :
    return { os.path.join( x[0], y )[len('./../'):] for x in os.walk('./../scripts/') for y in x[2] if y.endswith('.xml') }



def main(command_line_args):

    parser = ArgumentParser( description=main.__doc__ )

    parser.add_argument( "-r", "--rosetta", default=None, help="Path to Rosetta/main, default is ./../../" )
    parser.add_argument( "--output-file", default="verify_all_scripts_accounted_for_result.json" )
    parser.add_argument( "--working-dir", default=".", help="directory to which temporary results are written" )  # we do not use this option here but we need it so this script have the same minimal set of options as other scripts
    parser.add_argument( "--keep-intermediate-files", default=False, help="delete intermediate test files", action='store_true' ) # we do not use this option here but we need it so this script have the same minimal set of options as other scripts
    validate_all_scripts.add_rosetta_executable_arguments(parser)

    args = parser.parse_args()

    scripts_to_parse    = imp.load_source('scripts_to_parse',    './../scripts_to_parse.py')
    scripts_to_validate = imp.load_source('scripts_to_validate', './../scripts_to_validate.py')
    untested_scripts    = imp.load_source('untested_scripts',    './../untested_scripts.py')



    all_listed_scripts = set( scripts_to_validate.scripts_to_be_validated + scripts_to_parse.scripts_to_be_parsed + untested_scripts.scripts_not_tested )
    all_found_files = find_all_xml_scripts_in_repo()

    # for x in all_found_files :
    #    print( "Found: " + x )

    scripts_not_found = []
    scripts_not_listed = {}
    tests = {}

    all_good = True
    for script in all_listed_scripts :
        if script not in all_found_files :
            all_good = False
            scripts_not_found.append( script )
            tests[script] = dict(state='failed', log='Script was not found!\n')

    for script in all_found_files :
        if script not in all_listed_scripts :
            all_good = False
            blame_lines = execute('Running Git blame to get author information', 'git blame ./../{}'.format(script), return_='output').split('\n')

            last_line = blame_lines[-2]

            author = last_line[ (last_line.find("(")+1) : last_line.find( ")") ].split("20")[0] # Y3K Bug here!
            #print( last_line )
            #print( author )
            scripts_not_listed[ script ] = author

            log = tests.get(script, dict(log='') )['log']
            tests[script] = dict(state = 'failed', log = log + 'Script file was found on disk but it is not listed!\nAuthor: {}\nGit blame output: {}\n'.format(author, last_line))


    results = {
        'state' : 'passed' if all_good else 'failed',
        'log'   : 'scripts_not_found:\n{not_found}\nscripts_not_listed:\n{not_listed}'.format(not_found = '\n'.join(scripts_not_found), not_listed='\n'.join(scripts_not_listed)),
        'tests' : tests,
    }

    with open( args.output_file, 'w' ) as f: json.dump(results, f, sort_keys=True, indent=2)

    if sys.stdout.isatty():
        print(results['log'])
        print('Result:', results['state'])


if __name__ == "__main__" :
    main( sys.argv )

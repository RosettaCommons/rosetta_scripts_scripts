#!/usr/bin/env python
# -*- coding: utf-8 -*-
# :noTabs=true:

# (c) Copyright Rosetta Commons Member Institutions.
# (c) This file is part of the Rosetta software suite and is made available under license.
# (c) The Rosetta software is developed by the contributing members of the Rosetta Commons.
# (c) For more information, see http://www.rosettacommons.org. Questions about this can be
# (c) addressed to University of Washington CoMotion, email: license@uw.edu.

from __future__ import print_function

from argparse import ArgumentParser
import os as opsys
import sys, subprocess
import json
import imp
import validate_all_scripts as vas

def main( input_args ) :
    '''
    Test all of the XML files listed in the python file "rosetta_scripts_scripts/scripts_to_parse.py"
    for whether they are valid according to Rosetta's internally-generated XML Schema Definition (XSD),
    and for whether the objects that are described within it can be fully created and initialized.
    Output from this test is written to a .json file -- by default, parsing_results.json, but controllable
    by the user. This script can be run in parallel using the -j/--jobs flag.
    '''

    parser = ArgumentParser( description=main.__doc__ )

    parser.add_argument( "-j", "--jobs", default=1, type=int, help="Number of processors to use when running tests" )
    parser.add_argument( "-r", "--rosetta", default=None, help="Path to Rosetta/main, default is ./../../" )
    parser.add_argument( "--output-file", default="parsing_results.json" )
    parser.add_argument( "--working-dir", default=".", help="directory to which temporary results are written" )
    parser.add_argument( "-q", "--quiet", help="supress output messages", action='store_true' )
    parser.add_argument( "-Q", "--silent", help="supress all output", action='store_true' )
    parser.add_argument( "--keep-intermediate-files", default=False, help="delete intermediate test files", action='store_true' )
    parser.add_argument( "--test", default="", help="Test a particular script only, if `option` in full xml-file-name; do test; else skip" )
    vas.add_rosetta_executable_arguments( parser )

    args = parser.parse_args()

    rosetta = opsys.path.abspath('./../..') if args.rosetta is None else args.rosetta

    parallel_source = rosetta + '/tests/benchmark/util/parallel.py'

    if not opsys.path.isfile(parallel_source): print('Could not guess Rosetta/main location (was trying {}), exiting...'.format(rosetta) ); sys.exit(1)

    if args.rosetta is None: print( 'Found Rosetta/main at {}, going to use it...'.format(rosetta) )


    rosetta_executable = vas.rosetta_executable_abspath( rosetta, "parse_rosetta_script", args )

    #from scripts_to_parse import scripts_to_be_parsed
    #work = { fname.replace("/",".") : vas.test_script_file_commands( rosetta_executable, fname ) for fname in scripts_to_be_parsed }

    scripts_to_parse = imp.load_source('scripts_to_parse', './../scripts_to_parse.py')
    work = { fname.replace("/",".") : vas.test_script_file_commands( rosetta_executable, fname ) for fname in scripts_to_parse.scripts_to_be_parsed }
    if args.test:
        for key, res in work.items():
            if args.test not in key:
                del work[key]

    parallel = imp.load_source('parallel', parallel_source)
    runner = parallel.Runner( args.jobs, args.quiet, args.silent)
    parallel_results = runner.run_commands_lines( 'parsing', commands_lines = work, working_dir = args.working_dir, delete_intermediate_files = not args.keep_intermediate_files)

    results = {}
    state = 'passed'
    for test in parallel_results:
        key = test[:-len('.xml')] if test.endswith('.xml') else test
        key = key[len('scripts.'):]

        results[key] = dict( state = 'failed' if parallel_results[test]['result'] else 'passed',
                             log = parallel_results[test]['output'],
        )

        if parallel_results[test]['result']: state = 'failed'

    results = dict(tests=results, state=state, log='')

    with open( args.output_file, 'w' ) as f: json.dump(results, f, sort_keys = True, indent = 2 )

if __name__ == "__main__" :
    main( sys.argv )

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
import subprocess
import json
import imp
import sys
import uuid

def test_script_file_commands( rosetta_executable, filename ) :
    assert filename.endswith('.xml')
    parts = filename.rpartition( "/" )
    dirname = parts[0]
    commands = []
    commands.append( "cd ./../%s && " % dirname )

    flags_fname = "../" + parts[0] + "/" + parts[2][:-4] + ".flags"
    #print( "possible flags name? ", flags_fname, opsys.path.isfile( flags_fname ) )
    flags_exist = opsys.path.isfile( flags_fname )

    rosetta_command = rosetta_executable + " -parser:protocol " + parts[2]
    if flags_exist : rosetta_command = rosetta_command + " @ " + parts[2][:-4] + ".flags"

    commands.append( rosetta_command )
    #print( "--".join( commands ) )
    return "".join( commands )


def add_rosetta_executable_arguments( parser ) :
    parser.add_argument( "-c", "--compiler", default="gcc",
        help="Which compiler did you use?" )
    parser.add_argument( "-o", "--os", default="linux",
        help="Which operating system are you using? (linux or macos)" )
    parser.add_argument( "-x", "--extras", default="default",
        help="Which extras flags did you use to build? (none==>'default', otherwise, 'mpi' or 'cxx11thread', etc.)" )
    parser.add_argument( "-d", "--debug", action="store_true",
        help="Use the debug version instead of the release version?" )

def rosetta_executable_abspath( path_to_rosetta_main, executable_name, args ) :
    rosetta_executable = path_to_rosetta_main + "/source/bin/" + \
        executable_name + "." + \
        args.extras + "." + \
        args.os + args.compiler + ( "debug" if args.debug else "release" )

    # get absolute path if we were given a relative path
    if len( rosetta_executable ) != 0 and rosetta_executable[0] != "/" :
        rosetta_executable = opsys.getcwd() + "/" + rosetta_executable

    if not opsys.path.isfile( rosetta_executable ) :
        print( "Error: executable '" + rosetta_executable + "' not found." )
        sys.exit(1)

    return rosetta_executable

def main( input_args ):
    '''
    Test all of the XML files listed in the python file "rosetta_scripts_scripts/scripts_to_validate.py"
    for whether they are valid according to Rosetta's internally-generated XML Schema Definition (XSD).
    Output from this test is written to a .json file -- by default, validation_results.json, but controllable
    by the user. This script can be run in parallel using the -j/--jobs flag.
    '''

    parser = ArgumentParser( description=main.__doc__ )

    parser.add_argument( "-j", "--jobs", default=1, type=int, help="Number of processors to use when running tests" )
    parser.add_argument( "-r", "--rosetta", default=None, help="Path to Rosetta/main, default is ./../../" )
    parser.add_argument( "--output-file", default="validation_results.json" )
    parser.add_argument( "--working-dir", default=".", help="directory to which temporary results are written" )
    parser.add_argument( "-q", "--quiet", help="supress output messages", action='store_true' )
    parser.add_argument( "-Q", "--silent", help="supress all output", action='store_true' )
    parser.add_argument( "--keep-intermediate-files", default=False, help="delete intermediate test files", action='store_true' )
    parser.add_argument( "--test", default="", help="Test a particular script only, if `option` in full xml-file-name; do test; else skip" )
    add_rosetta_executable_arguments( parser )

    args = parser.parse_args()

    rosetta = opsys.path.abspath('./../..') if args.rosetta is None else args.rosetta
    parallel_source = rosetta + '/tests/benchmark/util/parallel.py'
    if not opsys.path.isfile(parallel_source): print('Could not guess Rosetta/main location (was trying {}), exiting...'.format(rosetta) ); sys.exit(1)
    if args.rosetta is None: print( 'Found Rosetta/main at {}, going to use it...'.format(rosetta) )

    rosetta_executable = rosetta_executable_abspath(rosetta, "validate_rosetta_script", args )

    scripts_to_validate = imp.load_source('scripts_to_validate', './../scripts_to_validate.py')

    work_uuids = { fname.replace( "/", "." ) : fname.replace( "/", "." ) if len( fname ) < 200 else fname[:50].replace( "/", "." ) + str( uuid.uuid4() )[0:10] + fname[-100:].replace( "/", "." ) for fname in scripts_to_validate.scripts_to_be_validated }
    work = { work_uuids[ fname.replace( "/", "." ) ] : test_script_file_commands( rosetta_executable, fname ) for fname in scripts_to_validate.scripts_to_be_validated }
    if args.test:
        for key, res in work.items():
            if args.test not in key:
                del work[key]

    parallel = imp.load_source('parallel', parallel_source)
    runner = parallel.Runner( args.jobs, args.quiet, args.silent )
    parallel_results = runner.run_commands_lines( 'validation', commands_lines = work, working_dir = args.working_dir, delete_intermediate_files = not args.keep_intermediate_files )

    results = {}
    state = 'passed'
    for fname in work_uuids:
        fname_uuid = work_uuids[ fname ]
        key = fname[:-len('.xml')] if fname.endswith('.xml') else test
        key = key[len('scripts.'):]

        results[key] = dict( state = 'failed' if parallel_results[fname_uuid]['result'] else 'passed',
                             log = parallel_results[fname_uuid]['output'],
        )

        if parallel_results[fname_uuid]['result']: state = 'failed'

    results = dict(tests=results, state=state, log='')

    with open( args.output_file, 'w' ) as f: json.dump(results, f, sort_keys = True, indent = 2 )


if __name__ == "__main__" :
    main( sys.argv )

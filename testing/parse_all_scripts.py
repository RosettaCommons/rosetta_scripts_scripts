from __future__ import print_function

from argparse import ArgumentParser
from fork_manager import *
import os as opsys
import subprocess
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

    parser.add_argument( "-j", "--jobs", default=1, type=int,
        help="Number of processors to use when running tests" )
    parser.add_argument( "-r", "--rosetta", required=True,
        help="Required argument: path to Rosetta/main" )
    parser.add_argument( "--output-file", default="parsing_results.json" )
    parser.add_argument( "--working_dir", default=".", help="directory to which temporary results are written" )
    parser.add_argument( "-q", "--quiet", help="supress output messages", action='store_true' )
    parser.add_argument( "-Q", "--silent", help="supress all output", action='store_true' )
    vas.add_rosetta_executable_arguments( parser )

    args = parser.parse_args( input_args[1:] )

    rosetta_executable = vas.rosetta_executable_abspath( args.rosetta, "parse_rosetta_script", args )

    from scripts_to_parse import scripts_to_be_parsed

    work = { fname.replace("/",".") : vas.test_script_file_commands( rosetta_executable, fname ) for fname in scripts_to_be_parsed }

    parallel = imp.load_source('parallel', args.rosetta + '/tests/benchmark/util/parallel.py')
    runner = parallel.Runner( args.jobs, args.quiet, args.silent )
    results = runner.run_commands_lines( 'parsing', commands_lines = work, working_dir = args.working_dir, delete_intermediate_files = True )
    json.dump( results, open( args.output_file, 'w' ), sort_keys = True, indent = 2 )

if __name__ == "__main__" :
    main( sys.argv )

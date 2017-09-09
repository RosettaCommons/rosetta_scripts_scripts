from __future__ import print_function

from argparse import ArgumentParser
import os as opsys
import subprocess
import json
import imp
import sys


def test_script_file_commands( rosetta_executable, filename ) :
    assert( filename[-4:] == ".xml" )
    parts = filename.rpartition( "/" )
    dirname = parts[0]
    commands = []
    commands.append( "cd %s; " % dirname )

    flags_fname = parts[0] + "/" + parts[2][:-4] + ".flags"
    flags_exist = opsys.path.isfile( flags_fname )

    rosetta_command = rosetta_executable + " -parser:protocol " + parts[2]
    if flags_exist : rosetta_command = rosetta_command + " @ " + flags_fname

    commands.append( rosetta_command )
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
    rosetta_executable = path_to_rosetta_main + "source/bin/" + \
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

def main( input_args ) :
    '''
    Test all of the XML files listed in the python file "rosetta_scripts_scripts/scripts_to_validate.py"
    for whether they are valid according to Rosetta's internally-generated XML Schema Definition (XSD).
    Output from this test is written to a .json file -- by default, validation_results.json, but controllable
    by the user. This script can be run in parallel using the -j/--jobs flag.
    '''

    parser = ArgumentParser( description=main.__doc__ )

    parser.add_argument( "-j", "--jobs", default=1, type=int,
        help="Number of processors to use when running tests" )
    parser.add_argument( "-r", "--rosetta", required=True,
        help="Required argument: path to Rosetta/main" )
    parser.add_argument( "--output_file", default="validation_results.json" )
    parser.add_argument( "--working_dir", default=".", help="directory to which temporary results are written" )
    parser.add_argument( "-q", "--quiet", help="supress output messages", action='store_true' )
    parser.add_argument( "-Q", "--silent", help="supress all output", action='store_true' )
    add_rosetta_executable_arguments( parser )

    args = parser.parse_args( input_args[1:] )
    rosetta_executable = rosetta_executable_abspath( args.rosetta, "validate_rosetta_script", args )

    from scripts_to_validate import scripts_to_be_validated

    work = { fname.replace( "/", "." ) : test_script_file_commands( rosetta_executable, fname ) for fname in scripts_to_be_validated }

    parallel = imp.load_source('parallel', args.rosetta + '/tests/benchmark/util/parallel.py')
    runner = parallel.Runner( args.jobs, args.quiet, args.silent )
    results = runner.run_commands_lines( 'validation', commands_lines = work, working_dir = args.working_dir, delete_intermediate_files = True )
    json.dump( results, open( args.output_file, 'w' ), sort_keys = True, indent = 2 )


if __name__ == "__main__" :
    main( sys.argv )

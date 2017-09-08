from argparse import ArgumentParser
from fork_manager import *
import os as opsys
import subprocess
import validate_all_scripts as vas
import json

def main( input_args ) :
    '''
    Test all of the XML files listed in the python file "rosetta_scripts_scripts/scripts_to_parse.py"
    for whether they are valid according to Rosetta's internally-generated XML Schema Definition (XSD),
    and for whether the objects that are described within it can be fully created and initialized.
    Output from this test is written to a .json file -- by default, parsing_results.json, but controllable
    by the user. This script can be run in parallel using the -j/--jobs flag.
    '''

    #with blargs.Parser(locals()) as p :
    #    p.int( "ncpu" ).shorthand("j")
    #    p.str( "rosetta" ).required().described_as( "Required argument: path to Rosetta/main/" )
    #    p.str( "compiler" ).default("gcc")
    #    p.str( "os" ).default("linux")
    #    p.

    parser = ArgumentParser( description=main.__doc__ )

    parser.add_argument( "-j", "--jobs", default=1, type=int,
        help="Number of processors to use when running tests" )
    parser.add_argument( "-r", "--rosetta", required=True,
        help="Required argument: path to Rosetta/main" )
    parser.add_argument( "--output-file", default="parsing_results.json" )
    # parser.add_argument( "-q", "--quiet", help="supress output messages", action='store_true' )
    # parser.add_argument( "-s", "--silent", help="supress all output", action='store_true' )
    vas.add_rosetta_executable_arguments( parser )

    args = parser.parse_args( input_args[1:] )

    rosetta_executable = vas.rosetta_executable_abspath( args.rosetta, "parse_rosetta_script", args )

    from scripts_to_parse import scripts_to_be_parsed

    work = { fname.replace("/",".") : vas.test_script_file_commands( rosetta_executable, fname ) for fname in scripts_to_be_parsed }

    json.dump( work, file( "parsing_work.json", 'w' ), sort_keys=True, indent=2 )
    sub_command = []
    sub_command.append( args.rosetta + "/tests/benchmark/util/parallel.py" )
    sub_command.append( "--jobs" )
    sub_command.append( str( args.jobs ))
    sub_command.append( "--prefix" )
    sub_command.append( args.output_file )
    # if args.silent :
    #     sub_command.append( "-Q" )
    # elif args.quiet :
    #     sub_command.append( "-q" )
    sub_command.append( "parsing_work.json" )

    child = subprocess.Popen( sub_command, stdout=subprocess.PIPE )
    streamdata = child.communicate()[0]
    if ( child.returncode != 0 ) :
        print( streamdata )

    print( child.returncode )
    sys.exit( child.returncode )



if __name__ == "__main__" :
    main( sys.argv )

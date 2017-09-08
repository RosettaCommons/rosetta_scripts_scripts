from argparse import ArgumentParser
from fork_manager import *
import os as opsys
import subprocess
import json

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

# class RSScriptTestManager :
#     def __init__( self, json_outfilename ) :
#         self.file_for_job = {}
#         self.all_files_validated = True
#         self.files_that_failed = []
#         self.json_outfilename = "default.json"
#     def handle_successful_file_validation( self, fm, pid ) :
#         if pid not in self.file_for_job :
#             print( "Critical error. Could not find file assigned to process", pid )
#             for pid in self.file_for_job :
#                 print( "Process ", pid, "responsible for", self.file_for_job[pid] )
#             sys.exit(1)
#         else :
#             del self.file_for_job[pid]
#     def handle_failed_file_validation( self, fm, pid ) :
#         if pid not in self.file_for_job :
#             print( "Critical error. Could not find file assigned to process", pid )
#             for pid in self.file_for_job :
#                 print( "Process ", pid, "responsible for", self.file_for_job[pid] )
#             sys.exit(1)
#         else :
#             self.files_that_failed.append( self.file_for_job[ pid ] )
#             self.all_files_validated = False
#             del self.file_for_job[ pid ]

def main( input_args ) :
    '''
    Test all of the XML files listed in the python file "rosetta_scripts_scripts/scripts_to_validate.py"
    for whether they are valid according to Rosetta's internally-generated XML Schema Definition (XSD).
    Output from this test is written to a .json file -- by default, validation_results.json, but controllable
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
    parser.add_argument( "--output-file", default="validation_results.json" )
    # parser.add_argument( "-q", "--quiet", help="supress output messages", action='store_true' )
    # parser.add_argument( "-s", "--silent", help="supress all output", action='store_true' )
    add_rosetta_executable_arguments( parser )

    args = parser.parse_args( input_args[1:] )

    rosetta_executable = rosetta_executable_abspath( args.rosetta, "validate_rosetta_script", args )

    # tm = RSScriptTestManager()
    # fm = ForkManager( ncpu )
    # fm.error_callback = tm.handle_failed_file_validation
    # fm.success_callback = tm.handle_successful_file_validation

    from scripts_to_validate import scripts_to_be_validated

    work = { fname.replace( "/", "." ) : test_script_file_commands( rosetta_executable, fname ) for fname in scripts_to_be_validated }

    json.dump( work, file( "validation_work.json", 'w' ), sort_keys=True, indent=2 )
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
    sub_command.append( "validation_work.json" )

    child = subprocess.Popen( sub_command, stdout=subprocess.PIPE )
    streamdata = child.communicate()[0]
    if ( child.returncode != 0 ) :
        print( streamdata )

    sys.exit( child.returncode )

if __name__ == "__main__" :
    main( sys.argv )


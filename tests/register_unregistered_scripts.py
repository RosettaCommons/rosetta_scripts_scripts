#!/usr/bin/env python
# -*- coding: utf-8 -*-
# :noTabs=true:

# (c) Copyright Rosetta Commons Member Institutions.
# (c) This file is part of the Rosetta software suite and is made available under license.
# (c) The Rosetta software is developed by the contributing members of the Rosetta Commons.
# (c) For more information, see http://www.rosettacommons.org. Questions about this can be
# (c) addressed to University of Washington CoMotion, email: license@uw.edu.

# The purpose of this script is to identify newly-added scrpts and to add them to either
# the scripts_to_verify.py list or to the untested_scripts.py list.

from __future__ import print_function

from argparse import ArgumentParser
import os as opsys
import subprocess
import json
import imp
import sys
import uuid
from verify_all_scripts_accounted_for import *
from validate_all_scripts import *

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
        #print( "Error: executable '" + rosetta_executable + "' not found." )
        sys.exit(1)

    return rosetta_executable

def add_files_to_python_list_script( lines, new_files ) :
    if len(new_files) == 0 : return lines
    newlines = []
    started = False
    done = False
    for line in lines :
        if done or len( line ) == 0 or line[0] == "#" :
            newlines.append( line )
            continue
        if started :
            if ( line == "]\n" ) :
                # last line needs a trailing comma:
                looking_for_last_element = True
                line_ind = -1
                while ( looking_for_last_element ) :
                    #print( line_ind )
                    lastline = newlines[ line_ind ]
                    #print( lastline )
                    #find the position of the last " before a comment
                    comment_pos = lastline.find( "#" )
                    if comment_pos == -1 : comment_pos = len(lastline)
                    #print( "comment_pos", comment_pos )
                    last_quote_pos = lastline.rfind( '"', 0, comment_pos )
                    if last_quote_pos == -1 :
                        #print( "didn't find \"" )
                        last_quote_pos = lastline.rfind( "'" , 0, comment_pos )
                    if last_quote_pos == -1 :
                        line_ind -= 1
                        #print( "didnt find'" )
                        continue
                    comma_pos = lastline.find( ",", last_quote_pos, comment_pos )
                    if comma_pos == -1 :
                        newline = lastline[:last_quote_pos+1] + "," + lastline[(last_quote_pos+1):]
                        newlines[ line_ind ] = newline 
                    looking_for_last_element = False
                # now we should put the new file names in
                for fname in new_files :
                    newlines.append( "    \"" + fname + "\",\n" )
                # remove the comma from the last line
                newlines[-1] = newlines[-1][:-2] + "\n"
                newlines.append( line )
                done = True
            else :
                newlines.append( line )
        else :
            #print( line )
            comment_pos = line.find( "#" )
            lbracket_pos = line.find( "[", 0, comment_pos if comment_pos != -1 else len(line) )
            if lbracket_pos >= 0  :
                started = True
            newlines.append( line )
    return newlines

def main( input_args ):
    """Look for all of the not-yet registered scripts and add them to eitehr
    rosetta_scripts_scripts/untested_scripts.py or
    rosetta_scripts_scripts/scripts_to_validate.py depending on whether
    the script is valid according to the XSD"""

    parser = ArgumentParser( description=main.__doc__ )

    parser.add_argument( "-j", "--jobs", default=1, type=int, help="Number of processors to use when running tests" )
    parser.add_argument( "-r", "--rosetta", default=None, help="Path to Rosetta/main, default is ./../../" )
    parser.add_argument( "-q", "--quiet", help="supress output messages", action='store_true' )
    parser.add_argument( "-Q", "--silent", help="supress all output", action='store_true' )
    add_rosetta_executable_arguments( parser )

    args = parser.parse_args()

    rosetta = opsys.path.abspath('./../../main') if args.rosetta is None else args.rosetta
    parallel_source = rosetta + '/tests/benchmark/util/parallel.py'
    if not opsys.path.isfile(parallel_source): print('Could not guess Rosetta/main location (was trying {}), exiting...'.format(rosetta) ); sys.exit(1)
    if args.rosetta is None: print( 'Found Rosetta/main at {}, going to use it...'.format(rosetta) )

    rosetta_executable = rosetta_executable_abspath(rosetta, "validate_rosetta_script", args )


    import validate_all_scripts
    scripts_to_parse    = imp.load_source('scripts_to_parse',    './../scripts_to_parse.py')
    scripts_to_validate = imp.load_source('scripts_to_validate', './../scripts_to_validate.py')
    untested_scripts    = imp.load_source('untested_scripts',    './../untested_scripts.py')


    all_listed_scripts = set( scripts_to_validate.scripts_to_be_validated + scripts_to_parse.scripts_to_be_parsed + untested_scripts.scripts_not_tested )
    all_found_files = find_all_xml_scripts_in_repo()

    scripts_not_listed = []
    for script in all_found_files :
        if script not in all_listed_scripts :
            scripts_not_listed.append( script ) 

    print( "Unregistered scripts:", scripts_not_listed )

    worknames = { fname :  fname.replace( "/", "." ) for fname in scripts_not_listed }
    work_uuids = { fname.replace( "/", "." ) : fname.replace( "/", "." ) if len( fname ) < 200 else fname[:50].replace( "/", "." ) + str( uuid.uuid4() )[0:10] + fname[-100:].replace( "/", "." ) for fname in scripts_not_listed }
    work = { work_uuids[ worknames[ fname ] ] : test_script_file_commands( rosetta_executable, fname ) for fname in scripts_not_listed }


    parallel = imp.load_source('parallel', parallel_source)
    runner = parallel.Runner( args.jobs, args.quiet, args.silent )
    parallel_results = runner.run_commands_lines( 'validation', commands_lines = work, working_dir =  "./", delete_intermediate_files = False )

    new_files_that_validate = []
    new_files_that_dont_validate = []
    for fname, fname_munged in worknames.iteritems():
        testname = work_uuids[ fname_munged ]
        if parallel_results[ testname ][ 'result' ] :
            new_files_that_dont_validate.append( fname )
        else :
            new_files_that_validate.append( fname )

    for fname in new_files_that_dont_validate :
        print( "File does not validate:", fname )
    for fname in new_files_that_validate :
        print( "File validates:", fname )

    validation_list_lines = open( "../scripts_to_validate.py" ).readlines()
    newlines = add_files_to_python_list_script( validation_list_lines, new_files_that_validate )
    open ( "../scripts_to_validate.py", "w" ).writelines( newlines )

    untested_scripts_lines = open( "../untested_scripts.py" ).readlines()
    newlines = add_files_to_python_list_script( untested_scripts_lines, new_files_that_dont_validate )
    open ( "../untested_scripts.py", "w" ).writelines( newlines )
    

if __name__ == "__main__" :
    main( sys.argv )

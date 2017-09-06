# 

import blargs
from fork_manager import *
import os as opsys
import subprocess


def test_script_file( rosetta_executable, filename ) :
    assert( filename[-4:] == ".xml" )
    parts = filename.rpartition( "/" )
    dirname = parts[0]
    opsys.chdir( dirname )

    flags_fname = parts[2][:-4] + ".flags"
    flags_exist = opsys.path.isfile( flags_fname )

    command = rosetta_executable + " -parser:protocol " + parts[2]
    if flags_exist : command = command + " @ " + flags_fname

    print( "--".join( command.split() ) )

    child = subprocess.Popen( command.split(), stdout=subprocess.PIPE )
    streamdata = child.communicate()[0]
    return child.returncode
              

class RSScriptTestManager :
    def __init__( self ) :
        self.file_for_job = {}
        self.all_files_validated = True
        self.files_that_failed = []
    def handle_successful_file_validation( self, fm, pid ) :
        if pid not in self.file_for_job :
            print( "Critical error. Could not find file assigned to process", pid )
            for pid in self.file_for_job :
                print( "Process ", pid, "responsible for", self.file_for_job[pid] )
            sys.exit(1)
        else :
            del self.file_for_job[pid]
    def handle_failed_file_validation( self, fm, pid ) :
        if pid not in self.file_for_job :
            print( "Critical error. Could not find file assigned to process", pid )
            for pid in self.file_for_job :
                print( "Process ", pid, "responsible for", self.file_for_job[pid] )
            sys.exit(1)
        else :
            self.files_that_failed.append( self.file_for_job[ pid ] )
            self.all_files_validated = False
            del self.file_for_job[ pid ]

if __name__ == "__main__" :
    with blargs.Parser(locals()) as p :
        p.int( "ncpu" ).shorthand("j")
        p.str( "rosetta" ).required() # path to Rosetta/main/source
        p.str( "compiler" ).default("gcc")
        p.str( "os" ).default("linux")

    rosetta_executable = rosetta + "/bin/validate_rosetta_script.default." + os + compiler + "release"
    if len( rosetta_executable ) != 0 and rosetta_executable[0] != "/" :
        rosetta_executable = opsys.getcwd() + "/" + rosetta_executable

    if not opsys.path.isfile( rosetta_executable ) :
        print( "Error: executable '" + rosetta_executable + "' not found." )
        sys.exit(1)

    tm = RSScriptTestManager()
    fm = ForkManager( ncpu )
    fm.error_callback = tm.handle_failed_file_validation
    fm.success_callback = tm.handle_successful_file_validation

    from scripts_to_validate import *

    for fname in scripts_to_be_validated :
        pid = fm.mfork()
        if pid == 0 :
            # print( "Validating", fname )
            return_code = test_script_file( rosetta_executable, fname )
            sys.exit( return_code )
        else :
            tm.file_for_job[pid] = fname

    fm.wait_for_remaining_jobs()
    if tm.all_files_validated :
        sys.exit(0)
    else :
        for fname in tm.files_that_failed :
            print( "File '" + fname + "' could not be validated against the XSD" )
            sys.exit(1)

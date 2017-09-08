# 

import blargs
from fork_manager import *
import os as opsys
import subprocess
import validate_all_scripts as vas


if __name__ == "__main__" :
    with blargs.Parser(locals()) as p :
        p.int( "ncpu" ).shorthand("j")
        p.str( "rosetta" ).required() # path to Rosetta/main/source
        p.str( "compiler" ).default("gcc")
        p.str( "os" ).default("linux")

    rosetta_executable = rosetta + "/bin/parse_rosetta_script.default." + os + compiler + "release"
    if len( rosetta_executable ) != 0 and rosetta_executable[0] != "/" :
        rosetta_executable = opsys.getcwd() + "/" + rosetta_executable

    if not opsys.path.isfile( rosetta_executable ) :
        print( "Error: executable '" + rosetta_executable + "' not found." )
        sys.exit(1)

    tm = vas.RSScriptTestManager()
    fm = ForkManager( ncpu )
    fm.error_callback = tm.handle_failed_file_validation
    fm.success_callback = tm.handle_successful_file_validation

    from scripts_to_parse import *

    for fname in scripts_to_be_parsed :
        pid = fm.mfork()
        if pid == 0 :
            # print( "Parsing", fname )
            return_code = vas.test_script_file( rosetta_executable, fname )
            sys.exit( return_code )
        else :
            tm.file_for_job[pid] = fname

    fm.wait_for_remaining_jobs()
    if tm.all_files_validated :
        sys.exit(0)
    else :
        for fname in tm.files_that_failed :
            print( "File '" + fname + "' could either not be validated against the XSD or could not be parsed" )
        sys.exit(1)

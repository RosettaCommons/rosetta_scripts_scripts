#!/bin/bash

#This script is to run the three rosetta_scripts_scripts testing scripts in one command.
#The -j and -r flags are passed through to validate_all_scripts.py and parse_all_scripts.py.
#All other test script options remain as the default values.
#If -j and -r are not specified, they will also retain their default values.

#Set default processors to use to 1.
jflag=1

#Option processing.  Options j: and r: require arguments.  h displays help.
while getopts 'j:r:h' opts; do
	case ${opts} in
		#Number of processors to use, if specified.
		j )
			jflag=$OPTARG
			;;
		#Path to Rosetta/main, if specified.
		r )
			rflag=$OPTARG
			;;
		#Help message
		h )
			echo "Run the three rosetta_scripts_scripts testing scripts consecutively:"
			echo "verify_all_scripts_accounted_for.py, validate_all_scripts.py, parse_all_scripts.py"
			echo
			echo "Usage: run_all_tests.sh [-j JOBS] [-r ROSETTA]"
			echo "optional arguments:"
			echo "   -j JOBS: Number of processors to use when running tests.  Default is 1."
			echo "   -r ROSETTA: Path to Rosetta/main, default is ./../.."
			exit 0
			;;
		#Error handling.
		\? )
			echo "Invalid option: $OPTARG"
			echo "Usage: run_all_tests.sh [-j JOBS] [-r ROSETTA]"
			echo "optional arguments:"
			echo "   -j JOBS: Number of processors to use when running tests.  Default is 1."
			echo "   -r ROSETTA: Path to Rosetta/main, default is ./../.."
			exit 1
			;;
	esac
done

#Run the verify test
./verify_all_scripts_accounted_for.py

#Check if the rflag has been set.  Run the other two scripts accordingly.
if [ -z ${rflag+x} ]; then
	#rflag is not set
	./validate_all_scripts.py -j $jflag
	./parse_all_scripts.py -j $jflag
else
	#rflag was set.  Use it.
	./validate_all_scripts.py -j $jflag -r $rflag
	./parse_all_scripts.py -j $jflag -r $rflag
fi

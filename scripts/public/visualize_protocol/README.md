Visualizing Protocols in rosetta_scripts
========================================

KEYWORDS: PyMol mover, pymol_observer

Author: Sinduja K. Marx (skmarx@uw.edu) and Jason Klima (klimaj@uw.edu)
Corresponding PI: David Baker
Last Updated: October 2017

Steps to set this up
--------------------
Configuration: Using rosetta_scripts API, running rosetta locally, outputs sent to pymol locally

1.	Edit "PyMOL-RosettaServer.py"
    At the very bottom of this script is the input for IP address. It is currently set to 0.0.0.0 with port 65000.
2.	Open PyMol
    * Run PyMOL-RosettaServer.py
    * example ouput in pymol:
        * PyMOL>run PyMOL-RosettaServer.py
        * PyMOL <---> PyRosetta link started!
        * at 0.0.0.0 port 65000
3.	Check your inputs
    * .xml file with pymol mover defined and called
    * .flags file for your command line options
    * .pdb for your input pdb file
4. 	Command line Executable
    * ~/Rosetta/main/source/bin/rosetta_scripts.default.macosclangrelease -database ~/Rosetta/main/database/ -s crambin.pdb -parser:protocol template_pymol_mover.xml
        * Expected outputs: Two pdbs will be output corresponding to the location in the protocol where you called pymol mover
5.  Command line Executable, scenario #2
    * ~/Rosetta/main/source/bin/rosetta_scripts.default.macosclangrelease -database ~/Rosetta/main/database/ -s crambin.pdb -parser:protocol test_pmm.xml -show_simulation_in_pymol 0 -keep_pymol_simulation_history 1
        * Turning on pymol_observer options. Now, you will have every state of the pdb loaded into pymol available for you to make a movie!

Flags | descriptions
----- | ------------
-show_simulation_in_pymol 0 | Use the PyMOL viewer to visualize simulation
-keep_pymol_simulation_history 1 | Keep pymol frames for making movies/replaying simulations (optional, defaults to false)

References
-----------

1. Baugh EH, Lyskov S, Weitzner BD, Gray JJ (2011) Real-Time PyMOL Visualization for Rosetta and PyRosetta. PLoS ONE 6: e21931.

2. Rosetta Scripts documentation!

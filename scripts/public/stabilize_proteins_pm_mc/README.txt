
The Kuhlman lab has developed two RosettaScripts protocols for predicting mutations that stabilize proteins. The first protocol characterizes point mutations (PM) while the second assesses mutation clusters (MC) in a local, combinatorial manner. The best variants predicted by the PM and MC protocols improved melting temperatures by 6°C and 11°C, respectively. After experimental assessment, mutations are often combined to generate the most stable variant possible. This approach enhanced the stability by more than 20°C for each of the three proteins our lab evaluated using these protein engineering techniques.

PLEASE checkout the tutorial directory, as there are python scripts that both generate the required inputs and analyze the outputs for these two RosettaScripts protocols. Both python scripts have documentation at the top of the file, and an example run is provided (check the README_py.txt for more info).

The mutation clusters script requires significant changes to maintain sequence symmetry, so a separate script has been provided as an example; however, I highly recommend using the python scripts to generate the RosettaScripts.

A publication describing these protocols in more detail, and introducing a ROSIE2 app, is in preparation. Please cite it if you find these tools useful (it will also have additional details on how the scripts function). The author list is David F. Thieker, Jack Maguire, Stephan T. Kudlacek, Andrew Leaver-Fay, Sergey Lyskov, Jeffrey J. Gray, & Brian Kuhlman, probably early 2022 publication.

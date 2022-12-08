
The Kuhlman lab has developed two RosettaScripts protocols for predicting mutations that stabilize proteins. The first protocol characterizes point mutations (PM) while the second assesses mutation clusters (MC) in a local, combinatorial manner. The best variants predicted by the PM and MC protocols improved melting temperatures by 6°C and 11°C, respectively. After experimental assessment, mutations are often combined to generate the most stable variant possible. This approach enhanced the stability by more than 20°C for each of the three proteins our lab evaluated using these protein engineering techniques.

PLEASE checkout the tutorial directory, as there are python scripts that both generate the required inputs and analyze the outputs for these two RosettaScripts protocols. Both python scripts have documentation at the top of the file, and an example run is provided (check the README_py.txt for more info).

The mutation clusters script requires significant changes to maintain sequence symmetry, so a separate script has been provided as an example; however, I highly recommend using the python scripts to generate the RosettaScripts.

Please cite the following article if you find these tools useful. There are also additional details, including figures, that describe how these scripts function.
Thieker, D. F., Maguire, J. B., Kudlacek, S. T., Leaver‐Fay, A., Lyskov, S., & Kuhlman, B. (2022). Stabilizing proteins, simplified: A Rosetta‐based webtool for predicting favorable mutations. Protein Science, 31(10), e4428.

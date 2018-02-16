Purpose:
Design second shell interactions around metal binding residues. 
Requires binding residue to be in the correct position, and to have a roughly designed backbone

hbnet.xml will:
    1)minimize the backbone with constraints on the binding residues using FastRelax
    2)find hydrogen bond networks that stabilize binding residues in position
    3)pass networks found to min.xml

min.xml will:
    1)repack around the networks
    2)refine the design with more stringent filters
    3)relax the pose without constraints

Once done, you should filter through designs for ones where the binding site does not break apart

# List all .xml files in all subdirectories of the scripts/ directory that should be run
# through the "parse-my-tag" test. These scripts can be placed into the same a directory
# as a flags file of the same name (e.g. "example.xml" could be paired with "example.flags")
# if additional flags are needed in order for the script to successfully make it through a
# complete parsing.

scripts_to_be_parsed = [
    "scripts/public/protein_interface_design/single_sided_dock_design_minimize_interface_protocol/ddmi.xml",
    "scripts/public/enzymedesign/enzdes_bookchapter_example.xml",
    "scripts/public/analysis/interface/analyze_electrostatics_in_helix_trimer.xml",
    "scripts/public/analysis/interface/custom_interface_filter1.xml",
    "scripts/public/analysis/interface/delete_chain_then_interface_analyzer.xml",
    "scripts/public/docking/terrible_analyze_mutations_at_interface.xml",
    "scripts/public/protein_hacking/helix_extend_with_threading.xml",
    "scripts/public/loop_modeling/simple_loop_grower/simple_loop_grower.xml",
    "scripts/public/protein_hacking/helix_extender.xml",
    "scripts/pilot/symmetry/symm.xml",
    "scripts/public/homology_modeling/relax_into_density/relax_into_density.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/working_example/symm_design.xml",
    "scripts/pilot/crystal_refine/reciprocal_refinement.xml",
    "scripts/pilot/energy_optimization/liquid_simulation.xml",
    "scripts/pilot/energy_optimization/rotamer_recovery.xml",
    "scripts/pilot/homology_modeling/hybridize/iterhybrid.cross.xml",
    "scripts/pilot/homology_modeling/hybridize/iterhybrid.mut.xml",
    "scripts/pilot/homology_modeling/hybridize/refine.hires.xml"
]
#note - do not put a trailing comma on the closing ] if you are doing multiline editing to add the trailing commas to the 10 scripts you just added - it will convert the list to a tuple and blow up the world

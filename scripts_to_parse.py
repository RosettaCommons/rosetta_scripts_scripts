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
    "scripts/pilot/enzymedesign/proenzyme_design/cpg2_proenzyme_prodomain_energylandscape.xml",
    "scripts/pilot/enzymedesign/design_threading/relax_deimm_designs.xml",
	"scripts/pilot/cyclic_peptide_design/cis_peptide_design_backbone_generation/KIC.xml",
	"scripts/pilot/metal_binding/zinc_dependent_hydrolase/05_symmetrize_matcheZn_rb_min.xml",
	"scripts/pilot/metal_binding/zinc_dependent_hydrolase/05_symmetrize_matchechi_min_match.xml",
	"scripts/pilot/metal_binding/zinc_dependent_hydrolase/15_relax_w_zadd_zn.xml",
	"scripts/pilot/protein_binding_energy_estimation/h3h4_designs/fastrelax3x_h3h4_fullrelax.xml",
	"scripts/pilot/protein_design/backrub_disulfidize_monte_carlo/backrub_disulfidize_monte_carlo.xml",
	"scripts/pilot/protein_design/de_novo_heterodimers/heterodimer_LSAS_final_design_close_loops_only.xml",
	"scripts/pilot/protein_design/scotts_scripts/invrot_rem_itest.xml",
	"scripts/pilot/protein_design/scotts_scripts/mutate_minimize_w_cst.xml",
	"scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/multidomain_1_bpb.xml",
	"scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/multidomain_1_sel_bpb.xml",
	"scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_extend_cter_bpb.xml",
	"scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_motif15aa_l3_off-1_rosman_2kpo_renumber.xml",
	"scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_bulge_processed_renumber.xml",
	"scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_large_sheet_bulge_bulge_processed_renumber.xml",
	"scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/rif_rifdock_HHHscafs_sel_designs_bpb.xml",
	"scripts/pilot/scoring/fast_relax_and_score/fast_relax_and_score.xml",
	"scripts/public/sewing/refinement/HR1B_refinement.xml",
    "scripts/public/sewing/refinement/HR1B_refinement_remove_partner.xml",
	"scripts/public/sewing/refinement/refine_C-terminal_binding_helix.xml",
	"scripts/public/visualize_protocol/template_pymol_mover.xml",
	"scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_bpb2_csts.xml",
	"scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_ba.bp_pass__20161129210609.pdb.bp_20161219173455_0001_0002_bpb2.xml",
	"scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210254.pdb.bp_20161219172548_0001_0003_bpb2.xml",
	"scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210726.pdb.bp_20161219173002_0001_0001_bpb2.xml",
	"scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210228.pdb.bp_20161219172446_0001_0001_bpb2.xml",
	"scripts/pilot/enzymedesign/proenzyme_design/cpg2_proenzyme_disulfidize.xml",
        "scripts/pilot/enzymedesign/proenzyme_design/cpg2_proenzyme_interface_saltbridges.xml"
]
#note - do not put a trailing comma on the closing ] if you are doing multiline editing to add the trailing commas to the 10 scripts you just added - it will convert the list to a tuple and blow up the world

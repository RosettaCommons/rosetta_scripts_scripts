# List all .xml files in all subdirectories of the scripts/ directory that should be run through
# the validator test: these tests will then be guaranteed by the testing server not to go out of
# date. If someone changes the underlying Mover/Filter used by one of these scripts, they will
# have to update the scripts that rely on them.


scripts_to_be_validated = [
    "scripts/pilot/example/an_example_for_testing_purposes/example_valid.xml",
    "scripts/public/sewing/refinement/zn_refinement.xml",
    "scripts/public/rotamer_recovery/ex1ex2_repack_t4400lt200_betaNov15_npdhb/rotamer_recovery_via_feature_analysis.xml",
    "scripts/public/feature_analysis/interface_feature_analysis/interface_features.xml",
    "scripts/public/feature_analysis/hbond_features_from_relaxed_decoys_npdhb_potential/hbond_feature_extraction.xml",
    "scripts/public/homology_modeling/RosettaCM_basic/cm_basic.xml",
    "scripts/public/homology_modeling/RosettaCM_with_constraints/cm_with_constraints.xml",
    "scripts/public/homology_modeling/RosettaCM_with_density/cm_with_density.xml",
    "scripts/public/sewing/refinement/gaq_binder_refinement.xml",
    "scripts/public/analysis/interface/custom_interface_filter2.xml",
    "scripts/public/docking/ancient_lrf_docking.xml",
    "scripts/public/docking/lrf_docking_with_autointerfacecst.xml",
    "scripts/public/docking/lrf_docking_with_usersuppliedconstraints.xml",
    "scripts/public/homology_modeling/hybridize_example.xml",
    "scripts/pilot/mutation_scanning/filterscan_score_all/filterscan-nopssm.xml",
    "scripts/pilot/enzymedesign/proenzyme_design/cpg2_proenzyme_prodomain_fixedbbdesign.xml",
    "scripts/pilot/enzymedesign/proenzyme_design/cpg2_proenzyme_rebuildlinker.xml",
    "scripts/pilot/enzymedesign/proenzyme_design_SEWING/cpg2_proenzyme_postsewing.xml",
    "scripts/pilot/enzymedesign/proenzyme_design/cpg2_proenzyme_prodomain_hbnetdesign.xml",
    "scripts/pilot/protein_design/bundle_tools/extend_bundle.xml",
    "scripts/pilot/protein_design/bundle_tools/graft_bundle_Nterm.xml",
    "scripts/pilot/protein_design/bundle_tools/graft_bundle_Cterm.xml",
    "scripts/pilot/protein_design/TERM_decoy_design/pose_comp.xml",
    "scripts/pilot/protein_interface_design/motifgrafting/180212_small_motif.xml",
    "scripts/pilot/denovo_smallmolecule_binding_design/beta_barrel_design/hbi_p2_rectBarrel_aacomp.xml",
    "scripts/pilot/denovo_smallmolecule_binding_design/beta_barrel_design/hbi_p2_rectBarrel_aacomp_releaserif.xml",
    "scripts/pilot/metal_binding/second_shell_interactions/hbnet.xml",
    "scripts/pilot/protein_design/scotts_scripts/monomer_fil.xml",
    "scripts/pilot/protein_design/scotts_scripts/david_nohbnet.xml",
    "scripts/pilot/protein_design/scotts_scripts/packing_filter.xml",
    "scripts/pilot/protein_design/scotts_scripts/c3.xml",
    "scripts/pilot/protein_design/scotts_scripts/david_nohbnet_polar_layer.xml",
    "scripts/pilot/protein_design/scotts_scripts/post_hbnet_min_repack_filter.xml",
    "scripts/pilot/protein_design/scotts_scripts/makePolyAla.xml",
    "scripts/pilot/protein_design/scotts_scripts/all_interface_filters.xml",
    "scripts/pilot/protein_design/scotts_scripts/bgs_hbnet_MPM.xml",
    "scripts/pilot/protein_design/scotts_scripts/CDB_build_HHH_backbone_disulfides_and_design.xml",
    "scripts/pilot/cyclic_peptide_design/membrane_permeable_peptide_design/cyclic_aromatic_permeable_design.xml",
    "scripts/pilot/homology_modeling/hybridize/cm.xml",
    "scripts/pilot/mutation_scanning/singlemutation_symrescore/mutalyze.xml",
    "scripts/pilot/mutation_scanning/singlemutation_symrescore/1c_mutalyze.xml",
    "scripts/pilot/protein_design/membrane_design_3helical_tetramer/design.xml",
    "scripts/pilot/protein_design/membrane_design_3helical_tetramer/filter.xml", 
    "scripts/pilot/homology_modeling/map_align/PF14912.5.xml",
    "scripts/pilot/protein_design/membrane_design_3helical_tetramer/filter.xml",
    "scripts/pilot/protein_design/RGD_loop_remodeling/Hyak_scripts_blueprint_builder.xml",
    "scripts/pilot/protein_design/RGD_loop_remodeling/Hyak_scripts_blueprint_builder_unformatted.xml",
    "scripts/pilot/protein_design/RGD_loop_remodeling/Hyak_scripts_blueprint_builder_fixed.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/14_filter_for_holeholes_filter.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/21_remove_thsymm_design.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/17_strong_cst_NCS_relafrelax.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/22_design_w_zn_after_thr_removaZn_rb_min.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/12_close_looclose_loop.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/13_design_loosymm_design_loop.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/17_NCS_relafrelax.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/13_design_loosymm_design_loop_new.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/12_close_loosymm_design.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/09_minimize_matcheZn_rb_min.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/55_break_symmetrhbnet_only.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/49_filter_parametric_bundleworst9mer_filter.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/22_design_w_zn_after_thr_removaNCS_design.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/36_new_scaffolds_from_remodel_filtering_steworst9mer_filter.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/35_NCS_design_fragment_flowerNCS_design.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/15_relax_w_zZn_rb_min.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/39_alternative_sitZn_cst_score.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/55_break_symmetrasymm_design.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/12_close_loosymm_design_after_loop.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/10_symmetric_desigsymm_design.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/16_design_w_zNCS_design.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/30_script_for_HH_blueprinworst9mer_filter.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210726.pdb.bp_20161219173002_0001_0001_selected_input2.bp_pass_20170207172929.pdb.bp_pass_20170207202003_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/rif_rifdock_norif.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210726.pdb.bp_20161219173002_0001_0001_selected_input2.bp_pass_20170207172909.pdb.bp_pass_20170207203033_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_agba.bp_pass__20161129211044.pdb.bp_20161219173042_0001_0002_option1_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_nobackhelix_yet_cc_scaf_c_II_0001.pdb.bp_pass__20161124211103_0001_0001_1helix_bpb2.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210726.pdb.bp_20161219173002_0001_0001_selected_input2.bp_pass_20170207172929.pdb.bp_pass_20170207203622_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210228.pdb.bp_20161219172446_0001_0001_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210726.pdb.bp_20161219173002_0001_0001_selected_input2.bp_pass_20170207172909.pdb.bp_pass_20170207203340_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210726.pdb.bp_20161219173002_0001_0001_selected_input2.bp_pass_20170207172909.pdb.bp_pass_20170207202741_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210726.pdb.bp_20161219173002_0001_0001_selected_input2.bp_pass_20170207172909.pdb.bp_pass_20170207201758_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_agba.bp_pass__20161129211044.pdb.bp_20161219173042_0001_0002_selected_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210726.pdb.bp_20161219173002_0001_0001_selected_input2.bp_pass_20170207172929.pdb.bp_pass_20170207201053_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_long_ferrodoxins_like_jump_PPIdes.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210726.pdb.bp_20161219173002_0001_0001_selected_input2.bp_pass_20170207172929.pdb.bp_pass_20170207203553_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_ba.bp_pass__20161129210609.pdb.bp_20161219173455_0001_0002_selected_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210726.pdb.bp_20161219173002_0001_0001_selected_input2.bp_pass_20170207172909.pdb.bp_pass_20170207201811_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210726.pdb.bp_20161219173002_0001_0001_selected_input2.bp_pass_20170207172909.pdb.bp_pass_20170207202033_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210726.pdb.bp_20161219173002_0001_0001_selected_input2.bp_pass_20170207172929.pdb.bp_pass_20170207202032_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210726.pdb.bp_20161219173002_0001_0001_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_long_ferrodoxins_like_extend_strand_and_relax_again_bpb.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210254.pdb.bp_20161219172548_0001_0003_selected_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210726.pdb.bp_20161219173002_0001_0001_selected_input2.bp_pass_20170207172909.pdb.bp_pass_20170207203228_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_agba.bp_pass__20161129211044.pdb.bp_20161219173042_0001_0002_option2_bpb2.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210726.pdb.bp_20161219173002_0001_0001_selected_input2.bp_pass_20170207172929.pdb.bp_pass_20170207203455_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_cterhelix_different_loop_bpb.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210726.pdb.bp_20161219173002_0001_0001_selected_test_bpb2.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210726.pdb.bp_20161219173002_0001_0001_selected_test_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_agba.bp_pass__20161129211044.pdb.bp_20161219173042_0001_0002_option1_bpb2.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_ba.bp_pass__20161129210609.pdb.bp_20161219173455_0001_0002_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210726.pdb.bp_20161219173002_0001_0001_selected_input2.bp_pass_20170207172909.pdb.bp_pass_20170207201908_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_baab.bp_pass__20161129201410.pdb.bp_20161219173607_0001_0002_bpb2.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_baab.bp_pass__20161129201410.pdb.bp_20161219173607_0001_0002_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/rif_rifdock_ppi_intdes.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210726.pdb.bp_20161219173002_0001_0001_selected_input2.bp_pass_20170207172909.pdb.bp_pass_20170207202756_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_baab.bp_pass__20161129201410.pdb.bp_20161219173607_0001_0002_selected_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210254.pdb.bp_20161219172548_0001_0003_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_long_ferrodoxins_like_extend_strand_and_relax_again_run_jump_PPIdes.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210726.pdb.bp_20161219173002_0001_0001_selected_input2.bp_pass_20170207172929.pdb.bp_pass_20170207202829_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210726.pdb.bp_20161219173002_0001_0001_selected_input2.bp_pass_20170207172929.pdb.bp_pass_20170207200957_bpb2_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210228.pdb.bp_20161219172446_0001_0001_selected_build.bp_pass_20170209105717_bpb2_csts.xml",
    "scripts/pilot/protein_design/pore_design/oct19_add_hbnet_designCx_export.xml",
    "scripts/pilot/crystal_refine/reciprocal_refinement.xml",
    "scripts/pilot/energy_optimization/rotamer_recovery.xml",
    "scripts/pilot/homology_modeling/hybridize/iterhybrid.cross.xml",
    "scripts/pilot/homology_modeling/hybridize/iterhybrid.mut.xml",
    "scripts/pilot/homology_modeling/hybridize/refine.hires.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/working_example/symm_design.xml",
    "scripts/pilot/enzymedesign/proenzyme_design/abinitio_topbroker.xml",
	"scripts/pilot/fold_and_dock_membrane_single_spanning_homodimers/fnd_homo.xml",
	"scripts/pilot/metal_binding/second_shell_interactions/min.xml"
]

#note - do not put a trailing comma on the closing ] if you are doing multiline editing to add the trailing commas to the 10 scripts you just added - it will convert the list to a tuple and blow up the world

# List all .xml files in all subdirectories of the scripts/ directory that should not
# be tested either in the validation- or parse-my-tag tests here.
# There are three classes of XML files that belong in this list.
# 1. Files that should just not be tested because they are out of date with the XSD
# and cannot readily be made up to date using the rewriter (perhaps one of the
# movers has changed significantly since the script was used)
# 2. Files that are xi:included from other (tested) XML files, but that do not start
# with <RosettaScripts> and so would not pass a validation test on their own, and
# 3. Files that are symlinked from some subdirectory of the main/tests/integration_tests
# directory, and that are thus fully tested in a different system.
#
# This script defines a large list that will be imported by other scripts

scripts_not_tested = [
    "scripts/pilot/example/an_example_for_testing_purposes/example_invalid.xml",
    "scripts/public/sewing/append/GTPase_inhibitors/HR1A_RhoA_LOV_cage/HR1A_RhoA_LOV_cage.xml",
    "scripts/public/sewing/append/GTPase_inhibitors/HR1B_Rac1_LOV_cage/HR1B_Rac1_LOV_cage.xml",
    "scripts/public/sewing/append/GTPase_inhibitors/Kalirin_zLock_2/Kalirin_zLock_2.xml",
    "scripts/public/sewing/append/gaq_binder_append.xml",
    "scripts/public/sewing/refinement/HEM_refinement.xml",
    "scripts/public/sewing/legacy_sewing/ca_assembly.xml",
    "scripts/public/sewing/append/HEM_append.xml",
    "scripts/public/sewing/append/zn_append_script.xml",
    "scripts/public/sewing/append/append_C-terminal_binding_helix.xml",
    "scripts/public/sewing/ligand_contacts/zn_tetra_script.xml",
    "scripts/public/sewing/ligand_contacts/zn_sewing_script.xml",
    "scripts/pilot/energy_optimization/general_potential/crystdock.xml",
    "scripts/pilot/energy_optimization/general_potential/crystmin.xml",
    "scripts/pilot/energy_optimization/general_potential/crystrefine.xml",
    "scripts/pilot/ligand_docking/GAdock/flexreceptor_soft_and_bbmove.xml",
    "scripts/pilot/ligand_docking/GAdock/flexsc_pack.xml",
    "scripts/pilot/ligand_docking/GAdock/rigidreceptor.xml",
    "scripts/pilot/ligand_docking/GAdock/rigidreceptor_useinput.xml",
    "scripts/pilot/protein_design/modular_protein_design/design.xml",
    "scripts/pilot/protein_design/motif_fiber_design/designCx.xml",
    "scripts/pilot/protein_design/motif_fiber_design/designHx.xml",
    "scripts/pilot/protein_design/motif_fiber_design/designHx_alatest.xml",
    "scripts/pilot/protein_design/motif_fiber_design/refineCx.xml",
    "scripts/pilot/protein_design/motif_fiber_design/refine_cap.xml",
    "scripts/pilot/protein_design/motif_fiber_design/refineCx_layer.xml",
    "scripts/pilot/protein_design/motif_fiber_design/refineCx_less_filter.xml",
    "scripts/pilot/protein_design/motif_fiber_design/refine_setup.xml",
    "scripts/pilot/protein_design/motif_fiber_design/setup_sym.xml",
    "scripts/pilot/protein_design/scotts_scripts/bgs_hbnet.xml",
    "scripts/pilot/protein_design/scotts_scripts/heterodimer_static_net_final_design.xml",
    "scripts/pilot/protein_design/scotts_scripts/ssdFilterNoDesign_pt7.xml",
    "scripts/pilot/protein_design/scotts_scripts/add_third_helix.xml",
    "scripts/pilot/protein_design/scotts_scripts/asymmetric_force_network_multiple.xml",
    "scripts/pilot/protein_design/scotts_scripts/heterotrimer_init.xml",
    "scripts/pilot/protein_design/scotts_scripts/ssdFilterNoDesign_pt8.xml",
    "scripts/pilot/protein_design/scotts_scripts/scoreNativeNoRepack.xml",
    "scripts/pilot/protein_design/scotts_scripts/hbnet_helbundle_min.xml",
    "scripts/pilot/protein_design/scotts_scripts/hbnet_unit_test_beta.xml",
    "scripts/pilot/protein_design/scotts_scripts/bgs_hbnet_heterodimer.xml",
    "scripts/pilot/protein_design/scotts_scripts/heterotrimer_final_design.xml",
    "scripts/pilot/protein_design/scotts_scripts/hbnet_helbundle.xml",
    "scripts/pilot/protein_design/scotts_scripts/new_buns_and_holes_w_satisfier.xml",
    "scripts/pilot/protein_design/scotts_scripts/final_design.xml",
    "scripts/pilot/protein_design/scotts_scripts/post_hbnet_resfile_and_cst.xml",
    "scripts/pilot/protein_design/scotts_scripts/new_pack_CAZ_no_resfile.xml",
    "scripts/pilot/protein_design/scotts_scripts/homotrimer_pH_His.xml",
    "scripts/pilot/protein_design/scotts_scripts/heterodimer_final_design_only_design_noMPM.xml",
    "scripts/pilot/protein_design/scotts_scripts/C5_ank1.xml",
    "scripts/pilot/protein_design/scotts_scripts/homotetramer_init.xml",
    "scripts/pilot/protein_design/scotts_scripts/homotrimer_init_detectsymm_resfile.xml",
    "scripts/pilot/protein_design/scotts_scripts/280613design.xml",
    "scripts/pilot/protein_design/scotts_scripts/homotrimer_init.xml",
    "scripts/pilot/protein_design/scotts_scripts/scoreNativeNoRBminNoBBmin.xml",
    "scripts/pilot/protein_design/scotts_scripts/add_third_helix_to_finished_design.xml",
    "scripts/pilot/protein_design/scotts_scripts/global_optimization_GenericSimulatedAnnealer.xml",
    "scripts/pilot/protein_design/scotts_scripts/fix_surf.xml",
    "scripts/pilot/protein_design/scotts_scripts/hbnet_unit_test_pH_His.xml",
    "scripts/pilot/protein_design/scotts_scripts/new_pack_TAZ_no_resfile.xml",
    "scripts/pilot/protein_design/scotts_scripts/soft_design.xml",
    "scripts/pilot/protein_design/scotts_scripts/FD_FR_and_scoring_benchmark_v3_digs.xml",
    "scripts/pilot/protein_design/scotts_scripts/reclose_and_design_around_loops.xml",
    "scripts/pilot/protein_design/scotts_scripts/hbnet_homotet_pH_beta.xml",
    "scripts/pilot/protein_design/scotts_scripts/force_network_multiple.xml",
    "scripts/pilot/protein_design/scotts_scripts/homotetramer.xml",
    "scripts/pilot/protein_design/scotts_scripts/post_hbnet_resfile_and_cst_norpkmin.xml",
    "scripts/pilot/protein_design/scotts_scripts/pH_His_heterobundle_w_transform_sc.xml",
    "scripts/pilot/protein_design/scotts_scripts/design_after_3rd_helix_closure.xml",
    "scripts/pilot/protein_design/scotts_scripts/pH_His_heterobundle.xml",
    "scripts/pilot/protein_design/scotts_scripts/heterodimer_final_design.xml",
    "scripts/pilot/protein_design/scotts_scripts/CA2_C2symm_final_design.xml",
    "scripts/pilot/protein_design/scotts_scripts/helical_bundle_hbnet_8.5_C2.xml",
    "scripts/pilot/protein_design/scotts_scripts/MakeBundle_SB13.xml",
    "scripts/pilot/protein_design/scotts_scripts/heterotrimer_all_helical_interfaces.xml",
    "scripts/pilot/protein_design/scotts_scripts/scoreNativeNoRBwithLigMinNoRepack.xml",
    "scripts/pilot/protein_design/scotts_scripts/for_daniel.xml",
    "scripts/pilot/protein_design/scotts_scripts/initFilter_design.xml",
    "scripts/pilot/protein_design/scotts_scripts/per_satisfy_hb.xml",
    "scripts/pilot/protein_design/scotts_scripts/homotetramer_init_no_met_or_trp.xml",
    "scripts/pilot/protein_design/scotts_scripts/post_hbnet_resfile_and_cst_nosoft.xml",
    "scripts/pilot/protein_design/scotts_scripts/heterodimer_final_design_only_design.xml",
    "scripts/pilot/protein_design/scotts_scripts/homotrimer_init_detectsymm.xml",
    "scripts/pilot/protein_design/scotts_scripts/heterotrimer_final_design_add_more_nets.xml",
    "scripts/pilot/protein_design/scotts_scripts/loops_and_hardpack_only.xml",
    "scripts/pilot/protein_design/scotts_scripts/new_buns_and_holes.xml",
    "scripts/pilot/protein_design/scotts_scripts/heterodimer_final_design_only_design_hyak.xml",
    "scripts/pilot/protein_design/scotts_scripts/closed_bundle_hbnet_design.xml",
    "scripts/pilot/protein_design/scotts_scripts/scoreNativeNoRBmin.xml",
    "scripts/pilot/protein_design/scotts_scripts/hbnet_bundle_design_onesided.xml",
    "scripts/pilot/protein_design/scotts_scripts/ssdFilterNoDesign.xml",
    "scripts/pilot/protein_design/scotts_scripts/add_third_helix_to_finished_design_C3_2L.xml",
    "scripts/pilot/protein_design/scotts_scripts/per_dock.xml",
    "scripts/pilot/protein_design/scotts_scripts/final_init.xml",
    "scripts/pilot/protein_design/scotts_scripts/hbnet_unit_test.xml",
    "scripts/pilot/protein_design/scotts_scripts/hbnet_start_from_his.xml",
    "scripts/pilot/protein_design/scotts_scripts/heterotetramerHis_Ring.xml",
    "scripts/pilot/protein_design/scotts_scripts/heterotetramer_Fix_His_Ring.xml",
    "scripts/pilot/protein_design/scotts_scripts/bgs_loop_closure_test.xml",
    "scripts/pilot/protein_design/scotts_scripts/scoreNative.xml",
    "scripts/pilot/protein_design/scotts_scripts/homotrimer.xml",
    "scripts/pilot/protein_design/scotts_scripts/hbnet_mpm_C4.xml",
    "scripts/pilot/protein_design/scotts_scripts/scoreNativeNoMin.xml",
    "scripts/pilot/protein_design/scotts_scripts/add_third_helix_to_finished_design_C2_2L.xml",
    "scripts/pilot/protein_design/scotts_scripts/griddesign.xml",
    "scripts/pilot/protein_design/scotts_scripts/BundleGridSampler_extend_ends_template.xml",
    "scripts/pilot/protein_design/scotts_scripts/filter_Trp.xml",
    "scripts/pilot/protein_design/scotts_scripts/minimize_and_filter_beta_symm.xml",
    "scripts/pilot/protein_design/scotts_scripts/per_griddesign.xml",
    "scripts/pilot/protein_design/scotts_scripts/hbnet_homotri_pH_beta.xml",
    "scripts/pilot/protein_design/scotts_scripts/extract_asym.xml",
    "scripts/pilot/protein_design/scotts_scripts/MC_hbnet_2layer_para_full.xml",
    "scripts/pilot/protein_design/pH_responsive_cages/his_scan.cheat.xml",
    "scripts/pilot/protein_design/pH_responsive_cages/his_scan.xml",
    "scripts/pilot/protein_design/pH_responsive_cages/revert.xml",
    "scripts/pilot/protein_design/RGD_loop_remodeling/Hyak_scripts_blueprint_builder_original.xml",
    "scripts/pilot/protein_design/RGD_loop_remodeling/blueprint_builder.xml",
    "scripts/pilot/protein_design/RGD_loop_remodeling/Test_Top7_blueprint_builder.xml",
    "scripts/pilot/protein_design/RGD_loop_remodeling/Hyak_scripts_blueprint_builder3.xml",
    "scripts/pilot/protein_design/RGD_loop_remodeling/Test_ub_out_blueprint_builder.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/32_design_fragment_derived_scaffolfilter.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/27_add_hbnet_initial_designhomotrimer_init.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/42_add_hbnet_to_desighbnet_CLA.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/42_add_hbnet_to_desighbnet_Zn.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/31_large_run_rotamer_dockindistance_filter.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/43_repack_hbnetted_designnew_symm_design.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/27_add_hbnet_initial_designscore.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/10_symmetric_desigclose_loop.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/27_add_hbnet_initial_designhbnet_zn.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/33_filter_fragment_derived_scaffolfilter.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/30_script_for_HH_blueprintest.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/29_prelim_design_remodeled_scaffolsymm_design.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/45_run_hbnet_fragment_based_flowerhbnet_Zn.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/40_redesign_to_improve_packinnew_symm_design.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/32_design_fragment_derived_scaffolsymm_design.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/32_design_fragment_derived_scaffolnew_symm_design.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/25_filter_C3_zheterodimer_final_design_only_design_noMPM.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/52_measure_ne2_distance_new_parametric_bundldistance_filter.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/47_add_hbnet_layers_to_designhomotrimer_init.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/12_close_looold_close_loop.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/32_design_fragment_derived_scaffolheterodimer_final_design_only_design_noMPM.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/46_finish_up_sequencnew_symm_design.xml",
    "scripts/pilot/metal_binding/zinc_dependent_hydrolase/25_filter_C3_zfilter.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_764m18_design10_cluster_0001_rank0485_size0025_fSS_E__bpb_ferr.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_bpb_strand.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_helix_variation_good_ppi_bpb_variation_pair_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_2kl8_ferrodoxin_antiparallel_bpb_ferr.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_helix_variation_good_ppi_other_scaffolds_bpb.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_halfway_bpb.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_2nd_helix_back_designs_c_pass_gba.bp_pass__20161129210726.pdb.bp_20161219173002_0001_0001_bpb_variation_pair_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_764m18_design10_blueprintpass__20161017111851_denovo_strand_rebuild_cter_helix_bpb_ferr_pair_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_helix_variation_good_ppi_start_len71aa_bpb_variation_pair_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_2kpo_rsmn_2x2_cluster0001_rank0888_bpb_ferr.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/BuildDeNovoBackboneMover_test.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_764m18_design10_large_sheet_best_c_frag_extendEB_loopEA.bp_pass_20161117111250_bpb_rebuild.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_2l69_rosman_bpb.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/bpb_strand.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_764m18_design10_blueprintpass__20161017111851_denovo_strand_bpb_ferr.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_2kpo_rsmn_2x2_bpb_1extraloopresihelix4_ferr.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_helix_variation_good_ppi_start_len72aa_bpb_variation_pair_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_2kpo_rsmn_2x2_bpb_ferr.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/graft_test_strand_miniproteins_design_try_jump0_design_flexbb.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_764m18_design10_helix1_side_cluster_0001_rank0049_size0025_fSS_E__rebuild_blueprintpass__20161030172734_2aaLoopNhelix_bpb_ferr.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_2kpo_rsmn_2x2_rebuild_scaffold_GBB_loop_bpb_ferr.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_large_sheet_bpb_strand.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_large_sheet_selected_link_bpb_strand.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/BuildDeNovoBackboneMover_cystatin_input_cystatin.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_EHEE_rd2_0647.pdb.ec50rise_1.55_antiparallel_cluster_0003_rank0616_size0023_fSS_E__bpb_ferr.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_helix_bpb.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_motif15aa_3aaloop_offset-1_two_chain_min_strand.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_764m18_design10_large_sheet_best_c_frag_extendEB_loopEA.bp_pass_20161117111127_bpb_ferr.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_motifgraft_motifgraft_helix_and_design.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_EAtypeloop_bpb_strand.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_build_LB_bpb_strand.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_764m18_design10_large_sheet_best_c_frag_extendEB_loopEA.bp_pass_20161117111250_bpb_ferr.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_motifgraft_only_graft_cartmin.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_2l69_rosman_3353_make_gbbloop_selected_bpb.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_motif15aa_l3_off-1_rosman_2kpo_bpb.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_764m18_design10_helix1_side_cluster_0001_rank0049_size0025_fSS_E__rebuild_blueprintpass__20161030172734_EHEE_bpb_ferr.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/graft_test_strand_miniproteins_design_try_design_flexbb.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_helix_variation_good_ppi_other_scaffolds_bpb_variation_pair_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_2kpo_rsmn_2x2_score.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_764m18_design10_helix1_side_cluster_0001_rank0049_size0025_fSS_E__bpb_ferr.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_764m18_design10_large_sheet_best_c_frag_extendEB_loopEA.bp_pass_20161117111250_bpb_ferr_pair_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_motif15aa_l3_off-1_bpb.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_EHEE_rd2_1260.pdb.ec50rise_2.33_parallel_cluster_0008c_rank1248_size0010_fSS_E__bpb_ferr.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_motifgraft_netmotifs_cartmin_grafting_only_graft_cartmin.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_motif15aa_l3_off-1_c_B_denovo_blueprintpass__20161017111338.pdb_modified_0001_0001.pdb_modified_0001_rebuild_helix_test_bpb_ferr_pair_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_motifgraft_only_graft.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_motifgraft_cartmin_denovos_only_graft_cartmin_jump0.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_helix_variation_good_ppi_start_len70aa_bpb_variation_pair_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_2kpo_rsmn_2x2_rebuild_scaffold_BGBB_loop_bpb_ferr.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_764m18_design10_blueprintpass__20161017111851_denovo_strand_rebuild_cter_helix_bpb_ferr.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_motif15aa_l3_off-1_rosman_2kpo_c_B_denovo_blueprintpass__20161017111338.pdb_modified_0001_0001.pdb_modified_0001_rebuild_helix_test_bpb_ferr_pair_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_add_helix_variation_good_ppi_start_len73aa_bpb_variation_pair_csts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_large_sheet_selected_bpb_strand.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_764m18_design10_helix1_side_cluster_0001_rank0049_size0025_fSS_E__rebuild_blueprintpass__20161030172734_bpb_ferr.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_764m18_design10_helix1_side_cluster_0001_rank0049_size0025_fSS_E__rebuild_blueprintpass__20161030172734_EHEE_bpb_ferr_jumps.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_DeNovoStrands_764m18_design10_large_sheet_best_c_frag_extendEB_loopEA.bp_pass_20161117111250_min_strand.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/graft_test_strand_miniproteins_only_motifgraft.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_764m18_design10_cluster_0001_rank0049_size0025_fSS_E__bpb_ferr.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_motifgraft_netmotifs_cartmin_grafting_only_graft_cartmin_jump0.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_2kpo_rsmn_2x2_rebuild_scaffold_GBB_loop_GBB_scaffolds_with_motif_bpb_ferr.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_2kl8_ferrodoxin_rebuild_scaffold_bpb_ferr.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_764m18_design10_bpb_ferr.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_motifgraft_netmotifs_cartmin_grafting_design_testing_design_grafts.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_2kpo_rsmn_2x2_cluster0001_rank0888_bpb_ferr_GBB.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_DeNovo_scaffolds_2kpo_rsmn_2x2_rebuild_scaffold_blueprintpass__20161030111603_GBB_bpb_ferr.xml",
    "scripts/pilot/protein_interface_design/edge_strand_mediated_interface_design/relaxed_tfr_retry_nonrelaxed_motifgraft_cartmin_denovos_only_graft_cartmin.xml",
    "scripts/pilot/protein_interface_design/motifgrafting/epigraft.xml",
    "scripts/pilot/protein_design/de_novo_heterodimers/hyak_flatland_hydrophobic.xml",
    "scripts/pilot/protein_design/de_novo_heterodimers/hyak_helical_bundle_C3.xml",
    "scripts/pilot/protein_design/de_novo_heterodimers/hyak_flatland_asym_hbnet.xml",
    "scripts/pilot/protein_design/de_novo_heterodimers/hyak_para_hetero.xml",
    "scripts/pilot/protein_design/de_novo_heterodimers/wormhole_packing_weights_hack.xml",
    "scripts/pilot/protein_design/de_novo_heterodimers/heptad_hbnet.xml",
    "scripts/pilot/protein_design/de_novo_heterodimers/hyak_setup_c2.xml",
    "scripts/pilot/protein_design/de_novo_heterodimers/hyak_helical_bundle_C2.xml",
    "scripts/pilot/protein_design/de_novo_heterodimers/hyak_flatland.xml",
    "scripts/pilot/protein_design/de_novo_heterodimers/heterodimer_hbnet_design.xml",
    "scripts/pilot/protein_design/de_novo_heterodimers/heterodimer_hbnet_design_asymbackbone.xml",
    "scripts/pilot/protein_design/de_novo_heterodimers/heterodimer_hbnet_design_3helix.xml",
    "scripts/pilot/protein_design/de_novo_heterodimers/wormhole_packing.xml",
    "scripts/pilot/protein_design/de_novo_heterodimers/flatland_full_lattice_design.xml",
    "scripts/pilot/protein_design/de_novo_heterodimers/flatland_final_packing.xml",
    "scripts/pilot/protein_design/de_novo_heterodimers/heterodimer_final_design_only_design.xml",
    "scripts/pilot/protein_design/de_novo_heterodimers/adjacent.xml",
    "scripts/pilot/protein_design/de_novo_heterodimers/wormhole_packing_HBNet.xml",
    "scripts/pilot/protein_design/pore_design/nov2_refine_hbnet_c6hb3_designInterface.xml",
    "scripts/pilot/protein_design/pore_design/oct19_hb3_redo_filter.xml",
    "scripts/pilot/protein_design/pore_design/sep19_HB3_C6_network_designCx.xml",
    "scripts/pilot/protein_design/pore_design/oct18_hb3_c6_designCx.xml",
    "scripts/pilot/protein_design/pore_design/oct18_greater_symmetrize_designCx.xml",
    "scripts/pilot/protein_design/pore_design/dock_scripts_designCx.xml",
    "scripts/pilot/protein_design/pore_design/nov30_hb1_c4_add_hbnet_motifs.xml",
    "scripts/pilot/protein_design/pore_design/sep25_hbnet_pores_mincontacts3_designCx.xml",
    "scripts/pilot/protein_design/pore_design/oct23_regen_docks_regen_docks.xml",
    "scripts/pilot/protein_design/pore_design/oct24_hb3_c6_mchbnet_extend_hbnet_on_docks.xml",
    "scripts/pilot/protein_design/pore_design/nov29_hb1_C6_add_hbnet_motifs.xml",
    "scripts/pilot/protein_design/pore_design/oct19_add_hbnet_add_hbnet_1021.xml",
    "scripts/pilot/protein_design/pore_design/dec12_ry1_C6_add_hbnet_motifs.xml",
    "scripts/pilot/protein_design/pore_design/dec14_ry1_C6_add_hbnet_motifs.xml",
    "scripts/pilot/protein_design/pore_design/nov13_mchbnet_extend_hbnet_on_docks_less_mc.xml",
    "scripts/pilot/protein_design/pore_design/oct18_hb3_c6_designCx_core_fix.xml",
    "scripts/pilot/protein_design/pore_design/dec12_ry1_C6_add_hbnet_motifs_rud.xml",
    "scripts/pilot/protein_design/pore_design/nov29_hb1_C7_add_hbnet_motifs.xml",
    "scripts/pilot/protein_design/pore_design/dec14_ry1_C6_add_hbnet_motifs_rud.xml",
    "scripts/pilot/protein_design/pore_design/dec13_ry1_C44_add_hbnet_motifs_rud.xml",
    "scripts/pilot/protein_design/pore_design/nov29_hb1_C8_add_hbnet_motifs.xml",
    "scripts/pilot/protein_design/pore_design/oct18_greater_symmetrize_designCx_core_fix.xml",
    "scripts/pilot/protein_design/pore_design/dec13_ry1_C5_add_hbnet_motifs.xml",
    "scripts/pilot/protein_design/pore_design/oct_hb3_c6_scripts_designCx.xml",
    "scripts/pilot/protein_design/pore_design/oct19_hb3_redo_designCx.xml",
    "scripts/pilot/protein_design/pore_design/oct_hb3_c6_scripts_designCx_core_fix.xml",
    "scripts/pilot/protein_design/pore_design/oct19_add_hbnet_designCx.xml",
    "scripts/pilot/protein_design/pore_design/sep15_HB3C6_network_motif_setup_designCx.xml",
    "scripts/pilot/protein_design/pore_design/oct19_add_hbnet_design_cX_hbnet.xml",
    "scripts/pilot/protein_design/pore_design/dec13_ry1_C5_add_hbnet_motifs_rud.xml",
    "scripts/pilot/protein_design/pore_design/dec13_ry1_C44_add_hbnet_motifs.xml",
    "scripts/pilot/protein_design/pore_design/oct_hb3_c6_scripts_filter.xml",
    "scripts/pilot/protein_design/pore_design/oct19_add_hbnet_add_hbnet_2.xml",
    "scripts/pilot/protein_design/pore_design/oct19_add_hbnet_add_hbnet_1.xml",
    "scripts/pilot/protein_design/pore_design/exclude_KR_HBNET_2_designCx.xml",
    "scripts/pilot/protein_design/pore_design/oct18_hb3_c6_filter.xml",
    "scripts/pilot/protein_design/pore_design/oct18_greater_symmetrize_filter.xml",
    "scripts/pilot/protein_design/pore_design/oct19_add_hbnet_filter.xml",
    "scripts/pilot/protein_design/pore_design/dec13_ry1_C7_add_hbnet_motifs_rud.xml",
    "scripts/pilot/protein_design/pore_design/nov2_refine_hbnet_c6hb3_add_hbnet_1021.xml",
    "scripts/pilot/protein_design/pore_design/oct19_add_hbnet_add_hbnet.xml",
    "scripts/pilot/protein_design/pore_design/nov7_extendnet_add_hbnet_motifs.xml",
    "scripts/pilot/protein_design/pore_design/oct19_add_hbnet_designCx_core_fix.xml",
    "scripts/pilot/protein_design/pore_design/exclude_KR_HBNET_designCx2.xml",
    "scripts/pilot/protein_design/pore_design/sep18_HB3_C6_network_designCx.xml",
    "scripts/pilot/protein_design/pore_design/oct24_hb3_c6_mchbnet_extend_hbnet_on_docks_less_mc.xml",
    "scripts/pilot/protein_design/pore_design/oct23_hb3_c6_network_search_extend_hbnet_on_docks.xml",
    "scripts/pilot/protein_design/pore_design/oct24_hb3_c6_mchbnet_extend_hbnet_on_docks_nomc.xml",
    "scripts/pilot/protein_design/pore_design/exclude_KR_HBNET_designCx.xml",
    "scripts/pilot/protein_design/pore_design/oct19_add_hbnet_designInterface.xml",
    "scripts/pilot/protein_design/pore_design/oct19_hb3_redo_designCx_core_fix.xml",
    "scripts/pilot/protein_design/pore_design/dec13_ry1_C7_add_hbnet_motifs.xml",
    "scripts/pilot/protein_design/pore_design/nov13_mchbnet_extend_hbnet_on_docks_nomc.xml",
    "scripts/pilot/protein_design/pore_design/funwithdocks2_designCx.xml",
    "scripts/public/multistage_examples/batch_relax.xml",
    "scripts/public/multistage_examples/de_novo_interface_design/dock_and_design_msrs.xml",
    "scripts/public/multistage_examples/de_novo_interface_design/multistage_hbnet_example.xml",
	"scripts/pilot/energy_optimization/liquid_simulation.xml",
	"scripts/public/cryoem/cryoem_glycan_refinement.xml",
    "scripts/public/macrocycle_inhibitor_design/NDM1i-1_design_script/original/xml/NDM1i_1_design_legacy.xml",
    "scripts/public/macrocycle_inhibitor_design/NDM1i-1_design_script/original/xml/design_8res_setup.xml",
    "scripts/public/docking/grid_docking/1.test_single_DoF/grid_dock_visualize_coordinate_system_protocol.xml",
    "scripts/public/docking/grid_docking/2.grid_dock/grid_dock_coarse_grain_protocol.xml",
    "scripts/public/docking/grid_docking/3.grid_dock_local_dock/grid_dock_coarse_and_local_dock_protocol.xml",
    "scripts/public/docking/grid_docking/4.grid_dock_local_dock_design/grid_dock_coarse_and_local_dock_plus_design_protocol.xml",
    "scripts/public/stabilize_proteins_pm_mc/mutation_clusters.xml",
    "scripts/public/stabilize_proteins_pm_mc/mutation_clusters_sym.xml",
    "scripts/public/stabilize_proteins_pm_mc/point_mutations.xml",
]
#note - do not put a trailing comma on the closing ] if you are doing multiline editing to add the trailing commas to the 10 scripts you just added - it will convert the list to a tuple and blow up the world

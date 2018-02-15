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
    "scripts/public/sewing/refinement/HR1B_refinement.xml",
    "scripts/public/sewing/refinement/HR1B_refinement_remove_partner.xml",
    "scripts/public/sewing/refinement/refine_C-terminal_binding_helix.xml",
    "scripts/public/sewing/refinement/gaq_binder_refinement.xml",
    "scripts/public/analysis/interface/custom_interface_filter2.xml",
    "scripts/public/docking/ancient_lrf_docking.xml",
    "scripts/public/docking/lrf_docking_with_autointerfacecst.xml",
    "scripts/public/docking/lrf_docking_with_usersuppliedconstraints.xml",
    "scripts/public/homology_modeling/hybridize_example.xml",
    "scripts/pilot/protein_design/backrub_disulfidize_monte_carlo/backrub_disulfidize_monte_carlo.xml",
    "scripts/pilot/mutation_scanning/filterscan_score_all/filterscan-nopssm.xml",
    "scripts/public/visualize_protocol/template_pymol_mover.xml",
    "scripts/pilot/enzymedesign/proenzyme_design/cpg2_proenzyme_prodomain_energylandscape.xml",
    "scripts/pilot/enzymedesign/proenzyme_design/cpg2_proenzyme_prodomain_fixedbbdesign.xml",
    "scripts/pilot/enzymedesign/proenzyme_design/cpg2_proenzyme_rebuildlinker.xml",
    "scripts/pilot/enzymedesign/proenzyme_design_SEWING/cpg2_proenzyme_postsewing.xml",
    "scripts/pilot/enzymedesign/proenzyme_design/cpg2_proenzyme_prodomain_hbnetdesign.xml",
    "scripts/pilot/protein_binding_energy_estimation/h3h4_designs/fastrelax3x_h3h4_fullrelax.xml",
    "scripts/pilot/protein_design/bundle_tools/extend_bundle.xml",
    "scripts/pilot/protein_design/bundle_tools/graft_bundle_Nterm.xml",
    "scripts/pilot/protein_design/bundle_tools/graft_bundle_Cterm.xml",
    "scripts/pilot/protein_design/TERM_decoy_design/pose_comp.xml",
    "scripts/pilot/protein_interface_design/motifgrafting/180212_small_motif.xml",
    "scripts/pilot/protein_interface_design/design_from_dock/mc_hbnet_only.xml",
    "scripts/pilot/protein_interface_design/generate_stubs/invrot_E.xml",
    "scripts/pilot/protein_interface_design/design_from_dock/FD_MRM_nobb.xml",
    "scripts/pilot/protein_interface_design/design_from_dock/FD_MRM_wbb.xml",
    "scripts/pilot/denovo_smallmolecule_binding_design/beta_barrel_design/hbi_p2_rectBarrel_aacomp.xml",
    "scripts/pilot/denovo_smallmolecule_binding_design/beta_barrel_design/hbi_p2_rectBarrel_aacomp_releaserif.xml",
    "scripts/pilot/metal_binding/second_shell_interactions/hbnet.xml",
    "scripts/pilot/protein_design/scotts_scripts/monomer_fil.xml",
    "scripts/pilot/protein_design/scotts_scripts/david_nohbnet.xml",
    "scripts/pilot/protein_design/scotts_scripts/packing_filter.xml",
    "scripts/pilot/protein_design/scotts_scripts/c3.xml",
    "scripts/pilot/protein_design/scotts_scripts/david_nohbnet_polar_layer.xml",
    "scripts/pilot/protein_design/scotts_scripts/post_hbnet_min_repack_filter.xml",
    "scripts/pilot/protein_design/scotts_scripts/invrot_rem_itest.xml",
    "scripts/pilot/protein_design/scotts_scripts/makePolyAla.xml",
    "scripts/pilot/protein_design/scotts_scripts/all_interface_filters.xml",
    "scripts/pilot/protein_design/scotts_scripts/bgs_hbnet_MPM.xml",
    "scripts/pilot/protein_design/scotts_scripts/CDB_build_HHH_backbone_disulfides_and_design.xml",
    "scripts/pilot/protein_design/scotts_scripts/mutate_minimize_w_cst.xml",
    "scripts/pilot/cyclic_peptide_design/cis_peptide_design_backbone_generation/KIC.xml",
    "scripts/pilot/cyclic_peptide_design/membrane_permeable_peptide_design/cyclic_aromatic_permeable_design.xml",
    "scripts/pilot/homology_modeling/hybridize/cm.xml",
    "scripts/pilot/mutation_scanning/singlemutation_symrescore/mutalyze.xml",
    "scripts/pilot/mutation_scanning/singlemutation_symrescore/1c_mutalyze.xml",
    "scripts/pilot/protein_design/membrane_design_3helical_tetramer/design.xml",
    "scripts/pilot/protein_design/membrane_design_3helical_tetramer/fiter.xml", 
    "scripts/pilot/homology_modeling/map_align/PF14912.5.xml"
]

#note - do not put a trailing comma on the closing ] if you are doing multiline editing to add the trailing commas to the 10 scripts you just added - it will convert the list to a tuple and blow up the world

def getprefix(filename) :
#------------------------
#
#   TOAR profiles : submission 2024-november
    if (   filename == 'globalmeanprofile_o3_0011-0050-YEA_glob_pressure_n20241022_toarmip_diff'                      ) : prefix='a) '
    elif ( filename == 'globalmeanprofile_o3_as_partpress_0011-0050-YEA_glob_pressure_n20241022_toarmip_diff'         ) : prefix='b) '
    elif ( filename == 'globalmeanprofile_ta_0011-0050-YEA_glob_pressure_n20241022_toarmip_diff'                      ) : prefix='c) '
    elif ( filename == 'globalmeanprofile_cl_0011-0050-YEA_glob_pressure_n20241022_toarmip_diff'                      ) : prefix='d) '
    elif ( filename == 'globalmeanprofile_o3_2012-2016-YEA_glob_pressure_n20241022_toarmip_diff_ODSonly'              ) : prefix='e) '
    elif ( filename == 'globalmeanprofile_o3_as_partpress_2012-2016-YEA_glob_pressure_n20241022_toarmip_diff_ODSonly' ) : prefix='f) '
    elif ( filename == 'globalmeanprofile_ta_2012-2016-YEA_glob_pressure_n20241022_toarmip_diff_ODSonly'              ) : prefix='g) '
    elif ( filename == 'globalmeanprofile_cl_2012-2016-YEA_glob_pressure_n20241022_toarmip_diff_ODSonly'              ) : prefix='h) '
#   TOAR profiles : revision 2025-march
    if (   filename == 'globalmeanprofile_o3_0011-0050-YEA_glob_pressure_n20250309_toarmip_diff'                      ) : prefix='a) '
    elif ( filename == 'globalmeanprofile_o3_as_partpress_0011-0050-YEA_glob_pressure_n20250309_toarmip_diff'         ) : prefix='b) '
    elif ( filename == 'globalmeanprofile_ta_0011-0050-YEA_glob_pressure_n20250309_toarmip_diff'                      ) : prefix='c) '
    elif ( filename == 'globalmeanprofile_cl_0011-0050-YEA_glob_pressure_n20250309_toarmip_diff'                      ) : prefix='d) '
    elif ( filename == 'globalmeanprofile_o3_2012-2016-YEA_glob_pressure_n20250309_toarmip_diff_ODSonly'              ) : prefix='e) '
    elif ( filename == 'globalmeanprofile_o3_as_partpress_2012-2016-YEA_glob_pressure_n20250309_toarmip_diff_ODSonly' ) : prefix='f) '
    elif ( filename == 'globalmeanprofile_ta_2012-2016-YEA_glob_pressure_n20250309_toarmip_diff_ODSonly'              ) : prefix='g) '
    elif ( filename == 'globalmeanprofile_cl_2012-2016-YEA_glob_pressure_n20250309_toarmip_diff_ODSonly'              ) : prefix='h) '
#   TOAR profiles : revision 2025-march
    if (   filename == 'globalmeanprofile_o3_0011-0050-YEA_glob_pressure_n20250701_toarmip_diff'                      ) : prefix='(a) '
    elif ( filename == 'globalmeanprofile_o3_as_partpress_0011-0050-YEA_glob_pressure_n20250701_toarmip_diff'         ) : prefix='(b) '
    elif ( filename == 'globalmeanprofile_ta_0011-0050-YEA_glob_pressure_n20250701_toarmip_diff'                      ) : prefix='(c) '
    elif ( filename == 'globalmeanprofile_cl_0011-0050-YEA_glob_pressure_n20250701_toarmip_diff'                      ) : prefix='(d) '
    elif ( filename == 'globalmeanprofile_hus_0011-0050-YEA_glob_pressure_n20250210_toarmip_diffrel_extra'            ) : prefix='(e) '
    elif ( filename == 'globalmeanprofile_o3_0011-0050-YEA_glob_pressure_n20250701_toarmip_diff_ODSonly'              ) : prefix='(f) '
    elif ( filename == 'globalmeanprofile_o3_as_partpress_0011-0050-YEA_glob_pressure_n20250701_toarmip_diff_ODSonly' ) : prefix='(g) '
    elif ( filename == 'globalmeanprofile_ta_0011-0050-YEA_glob_pressure_n20250701_toarmip_diff_ODSonly'              ) : prefix='(h) '
    elif ( filename == 'globalmeanprofile_cl_0011-0050-YEA_glob_pressure_n20250701_toarmip_diff_ODSonly'              ) : prefix='(i) '
    elif ( filename == 'globalmeanprofile_hus_0011-0050-YEA_glob_pressure_n20250210_toarmip_diffrel_sens_extra'       ) : prefix='(j) ' 
#   TOAR scatter plots : submission 2024-november
    elif ( filename == 'scatter_clt_glob_minusrsutcloud_glob_n20241027_toarmip_all'    ) : prefix='a) '
    elif ( filename == 'scatter_clt_glob_minusrlutcloud_glob_n20241027_toarmip_all'    ) : prefix='b) '
    elif ( filename == 'scatter_clt_glob_minusrsutrlutcloud_glob_n20241027_toarmip_all') : prefix='c) '
#   TOAR scatter plots : revision 2025-March
    elif ( filename == 'scatter_clt_glob_minusrsutcloud_glob_n20250309_toarmip_all'    ) : prefix='(a) '
    elif ( filename == 'scatter_clt_glob_minusrlutcloud_glob_n20250309_toarmip_all'    ) : prefix='(b) '
    elif ( filename == 'scatter_clt_glob_minusrsutrlutcloud_glob_n20250309_toarmip_all') : prefix='(c) '
#   ESM2025 Deliverable D7.1
    elif ( filename == 'F_N2O_DENIT_NITxLANDFRAC_glob_YEA_n20251107_n2olandocean_deliverable7_1'    ) : prefix='(a) '
    elif ( filename == 'SFN2O_as_N_glob_YEA_n20251107_n2olandocean_deliverable7_1'                  ) : prefix='(b) '
    elif ( filename == 'N2O_SRF_glob_YEA_n20251107_n2olandocean_deliverable7_1'                     ) : prefix='(c) '
    elif ( filename == 'TAU2_N2O_glob_YEA_n20251107_n2olandocean_deliverable7_1'                    ) : prefix='(d) '
#
    else : prefix = ''

    return prefix

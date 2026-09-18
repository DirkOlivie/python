import combine
#   
#---------------------------
#
# AIM
# 	combining seperate .ps-files into one .ps-file
#
#-------------------------------------------

figlist=['globalmeanprofile_o3_0011-0050-YEA_glob_pressure_n20250701_toarmip_diff.ps', \
         'globalmeanprofile_o3_as_partpress_0011-0050-YEA_glob_pressure_n20250701_toarmip_diff.ps', \
         'globalmeanprofile_ta_0011-0050-YEA_glob_pressure_n20250701_toarmip_diff.ps', \
         'globalmeanprofile_cl_0011-0050-YEA_glob_pressure_n20250701_toarmip_diff.ps', \
         'globalmeanprofile_hus_0011-0050-YEA_glob_pressure_n20250210_toarmip_diffrel_extra.ps', \
         'globalmeanprofile_o3_0011-0050-YEA_glob_pressure_n20250701_toarmip_diff_ODSonly.ps', \
         'globalmeanprofile_o3_as_partpress_0011-0050-YEA_glob_pressure_n20250701_toarmip_diff_ODSonly.ps', \
         'globalmeanprofile_ta_0011-0050-YEA_glob_pressure_n20250701_toarmip_diff_ODSonly.ps', \
         'globalmeanprofile_cl_0011-0050-YEA_glob_pressure_n20250701_toarmip_diff_ODSonly.ps', \
         'globalmeanprofile_hus_0011-0050-YEA_glob_pressure_n20250210_toarmip_diffrel_sens_extra.ps']
figdir='/projects/NS9560K/users/olivie/plots'
figout='toar_prof.ps'
nx=5
ny=2
#
combine.combine(figlist=figlist, figdir=figdir, figout=figout, nx=nx, ny=ny)



figlist=['scatter_clt_glob_minusrsutcloud_glob_n20250309_toarmip_all.ps', \
         'scatter_clt_glob_minusrlutcloud_glob_n20250309_toarmip_all.ps', \
         'scatter_clt_glob_minusrsutrlutcloud_glob_n20250309_toarmip_all.ps']
#
figdir='/projects/NS9560K/users/olivie/plots'
figout='scatter_all.ps'
nx=3
ny=1 
#
combine.combine(figlist=figlist, figdir=figdir, figout=figout, nx=nx, ny=ny)

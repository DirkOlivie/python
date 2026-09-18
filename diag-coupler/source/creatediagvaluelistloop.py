import creatediagvaluelistloop2


expidlist=[\
#          ne16pg3
          'n1850.ne16pg3_tn14.noresm3_0_beta09.2025-12-19', \
          'n1850.ne16pg3_tn14.noresm3_0_beta09.LandSpinup.2025-12-24', \
          'n1850.ne16pg3_tn14.noresm3_0_beta09.Run3.2025-12-30', \
          'n1850.ne16pg3_tn14.noresm3_0_beta09.Run4.2026-01-06', \
          'n1850.ne16pg3_tn14.noresm3_0_beta09.Run5.2026-01-08', \
          'n1850.ne16pg3_tn14.noresm3_0_beta10.Run6.2026-01-23', \
          'n1850.ne16pg3_tn14.noresm3_0_beta10.Run7.2026-01-26', \
          'n1850.ne16pg3_tn14.noresm3_0_beta11.Run8.2026-02-07', \
          'n1850.ne16pg3_tn14.noresm3_0_beta12.Run9.2026-03-11', \
          'n1850.ne16pg3_tn14.noresm3_0_beta12a.Run10_hyb.2026-03-28', \
          'n1850.ne16pg3_tn14.noresm3_0_beta13a.Run11_drydep_oldBLOM.2026-04-17', \
#          ne30pg3
          'n1850.ne30_tn14.noresm3_0_beta03a-run1_yr001.20251016', \
          'n1850.ne30_tn14.noresm3_0_beta03b-run1_yr001.20251021', \
          'n1850.ne30_tn14.noresm3_0_beta03b-run2_yr001.20251023', \
          'n1850.ne30_tn14.noresm3_0_beta03b-run2_yr031_eminatred.20251031', \
          'n1850.ne30_tn14.noresm3_0_beta04-run1_yr001.20251103', \
          'n1850.ne30_tn14.nor3_b05-rc1-run1_yr001.20251110', \
          'n1850.ne30_tn14.noresm3_0_beta06-run1_yr001.20251114', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run1_yr001.20251218', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run2_yr001.20251223', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run2_yr031.20251227', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run2_yr051_cplhist.20251230', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run1_yr001.20251218_lowmicromgautoconlwpexp', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run1_yr001.20251218_highmicromgautoconlwpexp', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09.CESM3devTuning.20251220', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09.CESM3devTuning.v2.20251222', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run1_yr001_lowdp1', \
          'n1850.ne30pg3_tn14.noresm3_0_beta09-run1_yr001_highdp1', \
          'n1850.ne30pg3_tn14.noresm3_0_beta11-run1_yr001.20260213', \
          'n1850.ne30pg3_tn14.noresm3_0_beta11-run2_yr001.20260213', \
          'n1850.ne30pg3_tn14.noresm3_0_beta11-run3_yr001.20260226', \
          'n1850.ne30pg3_tn14.noresm3_0_beta10-run1_yr101.20260120', \
          'n1850.ne30pg3_tn14.noresm3_0_beta10-run2_yr101.20260120', \
          'n1850.ne30pg3_tn14.noresm3_0_beta10-run3_yr101.20260123', \
          'n1850.ne30pg3_tn14.noresm3_0_beta10-run4_yr101.20260126', \
          'n1850.ne30pg3_tn14.noresm3_0_beta10-run5_yr121.20260127', \
          'n1850.ne30pg3_tn14.noresm3_0_beta10-run6_yr121.20260128', \
          'n1850.ne30pg3_tn14.noresm3_0_beta10-run7_yr121.20260128', \
          'n1850.ne30pg3_tn14.noresm3_0_beta10-run8_yr121.20260131']
expidlist=[ \
#          cesm3 - #316
          'b.e30_alpha08b.B1850C_LTso.ne30_t232_wgx3.316']           
#
varlist=['sum']
componentlist=['atm','lnd','rof','ocn','ice_nh','ice_sh','glc','sum']
#componentlist=['atm']
budgettypelist=['heat']
freqtypelist=['monthly']

creatediagvaluelistloop2.creatediagvaluelistloop2(expidlist=expidlist,varlist=varlist, componentlist=componentlist, budgettypelist=budgettypelist,freqtypelist=freqtypelist)





def getfinalexpidinfo(expid) :
#-----------------------------
    '''
    INPUT
        expid

    RETURN : structure containing
        year0
        year1
        scenario
        realisation
        grid
        model

    MODIFICATIONS
        (2024-12-09) added simulation for Jason (HyWay) - on H2
        (2025-09-23) removed freqfile

    '''

    print('Expid : ', expid)

#   CMI6 HISTORICAL
    if   ( expid == 'NHIST_f19_tn14_20190625ext' )                                 : year0=1850 ; year1=2014 ; scenario='historical' ; realisation='r1i1p1f1' ; grid='gn' ; model='NorESM2-LM' 
    elif ( expid == 'NHISTfrc2_f09_tn14_20191001ext' )                             : year0=1850 ; year1=2014 ; scenario='historical' ; realisation='r1i1p1f1' ; grid='gn' ; model='NorESM2-MM' 
#
#   ESM2025-WP1
#   aerosol-only
    elif ( expid == 'NF1850norbc_f19_20240312_test01'         )                    : year0=1 ; year1=40 ; scenario='piClim-control' ; realisation='r1i1p1f1' ; grid='gn'  ; model='NorESM2-LM'
    elif ( expid == 'NF1850norbc_aer2014_f19_20240312_test01' )                    : year0=1 ; year1=40 ; scenario='piClim-aer'     ; realisation='r1i1p1f1' ; grid='gn'  ; model='NorESM2-LM'
    elif ( expid == 'NF1850norbc_so22014_f19_20240312_test01' )                    : year0=1 ; year1=40 ; scenario='piClim-so2'     ; realisation='r1i1p1f1' ; grid='gn'  ; model='NorESM2-LM'
#   full chemistry
    elif ( expid == 'NF1850norbc_tropstratchem_f19_20240312_test01' )              : year0=1 ; year1=40 ; scenario='piClim-control' ; realisation='r1i1p1f1' ; grid='gn'  ; model='NorESM2-LM-C'
    elif ( expid == 'NF1850norbc_tropstratchem_aer2014_f19_20240312_test01' )      : year0=1 ; year1=40 ; scenario='piClim-aer'     ; realisation='r1i1p1f1' ; grid='gn'  ; model='NorESM2-LM-C'
    elif ( expid == 'NF1850norbc_tropstratchem_so22014_f19_20240312_test01' )      : year0=1 ; year1=40 ; scenario='piClim-so2'     ; realisation='r1i1p1f1' ; grid='gn'  ; model='NorESM2-LM-C'
    elif ( expid == 'NF1850norbc_tropstratchem_noxcovoc2014_f19_20240312_test01' ) : year0=1 ; year1=40 ; scenario='piClim-O3'      ; realisation='r1i1p1f1' ; grid='gn'  ; model='NorESM2-LM-C'
#   aerosol-only but with oxidants derived from full-chemistry : use "f2" to identify
    elif ( expid == 'NF1850norbc_tropstratoxid_f19_20240312_test01'         )                    : year0=1 ; year1=40 ; scenario='piClim-control' ; realisation='r1i1p1f2' ; grid='gn'  ; model='NorESM2-LM'
    elif ( expid == 'NF1850norbc_tropstratoxid_aer2014_f19_20240312_test01' )                    : year0=1 ; year1=40 ; scenario='piClim-aer'     ; realisation='r1i1p1f2' ; grid='gn'  ; model='NorESM2-LM'
    elif ( expid == 'NF1850norbc_tropstratoxid_so22014_f19_20240312_test01' )                    : year0=1 ; year1=40 ; scenario='piClim-so2'     ; realisation='r1i1p1f2' ; grid='gn'  ; model='NorESM2-LM' 
#
#   ESM2025-WP4/5
    elif ( expid == 'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1950_s01_esm2025_20250506' )     : year0=1950 ; year1=2014 ; scenario='amip'        ; realisation='r1i1p1f2' ; grid='gn'  ; model='NorESM2-LM-C'
    elif ( expid == 'NFHISTnorpddmsbc_tropstratchem_01_f19_f19_r1960_s04_esm2025_20250506' )     : year0=1960 ; year1=2014 ; scenario='amip-ch4ems' ; realisation='r1i1p1f2' ; grid='gn'  ; model='NorESM2-LM-C'   
#
#   ESM2025-WP6/7
    elif ( expid == 'N1850vslsn2onh3_f19_tn14_test10' ) : year0=31 ; year1=50 ; scenario='piControl'        ; realisation='r1i1p1f1' ; grid='gn'  ; model='NorESM2-LM-C'

#   TOAR
#   radiative ozone = chemical ozone
    elif ( expid == 'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20240315_sim01'               )  : year0=1 ; year1=40 ; scenario='pdClim-control'               ; realisation='r1i1p1f1' ; grid='gn'  ; model='NorESM2-LM'
    elif ( expid == 'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_ozon2050rad2015_fxemiyear_20240315_sim01'               )  : year0=1 ; year1=40 ; scenario='pdClim-2050ssp370noAER-radO3' ; realisation='r1i1p1f1' ; grid='gn'  ; model='NorESM2-LM'
    elif ( expid == 'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2050rad2015_fxemiyear_20240315_sim01'               )  : year0=1 ; year1=40 ; scenario='pdClim-2050ssp370-radO3'      ; realisation='r1i1p1f1' ; grid='gn'  ; model='NorESM2-LM'
#   prescribing the ozone climatologies
    elif ( expid == 'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2015_fxemiyear_20240315_sim01'     ) : year0=1 ; year1=40 ; scenario='pdClim-controlfixO3' ; realisation='r1i1p1f1' ; grid='gn'  ; model='NorESM2-LM'
    elif ( expid == 'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050_fxemiyear_20240315_sim01'     ) : year0=1 ; year1=40 ; scenario='pdClim-controlfixO3-2050ssp370noAER' ; realisation='r1i1p1f1' ; grid='gn'  ; model='NorESM2-LM'
    elif ( expid == 'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050chem_fxemiyear_20240315_sim01' ) : year0=1 ; year1=40 ; scenario='pdClim-controlfixO3-2050ssp370' ; realisation='r1i1p1f1' ; grid='gn'  ; model='NorESM2-LM'
#
#   HYDROGEN JASON
#   simulations from methaneMIP
    elif ( expid == 'NHIST_tropstratchem_01_f19_tn14_r2000_s01_20241118' ) : year0=2005 ; year1=2014 ; scenario='hist' ; realisation='r1i1p1f1' ; grid='gn'  ; model='NorESM2-LM'
#   hyway simulation
    elif ( expid == 'NFHISTSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_r2000_s01_hyway_20250521' ) : year0=2010 ; year1=2019 ; scenario='transient2010s' ; realisation='r1' ; grid='gn'  ; model='NorESM2-LM-C' # transient2010s
    elif ( expid == 'NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_s01_hyway_3hr2015_20250521'   ) : year0=2015 ; year1=2015 ; scenario='transient2010s' ; realisation='r1' ; grid='gn'  ; model='NorESM2-LM-C' # 3-hourly
    elif ( expid == 'NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_s01_hyway_3hr2019_20250521'   ) : year0=2019 ; year1=2019 ; scenario='transient2010s' ; realisation='r1' ; grid='gn'  ; model='NorESM2-LM-C' # 3-hourly
    elif ( expid == 'NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep0p75_s01_hyway_20260403' )             : year0=2019 ; year1=2038 ; scenario='cntr'     ; realisation='r1' ; grid='gn'  ; model='NorESM2-LM-C' # cntr
    elif ( expid == 'NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep0p75_ch4x1p1_s01_hyway_20260403' )     : year0=2019 ; year1=2038 ; scenario='ch4pert'  ; realisation='r1' ; grid='gn'  ; model='NorESM2-LM-C' # ch4pert
    elif ( expid == 'NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr2019_h2emi_h2dep0p75_h2plus100tg_s01_hyway_20260403' ) : year0=2019 ; year1=2038 ; scenario='h2pert'   ; realisation='r1' ; grid='gn'  ; model='NorESM2-LM-C' # h2pert
    elif ( expid == 'NFSSP245norpddmsbc_tropstratchem_sdyn_01_f19_f19_cntr1850_h2emi_h2dep0p75_s01_hyway_20260403' )             : year0=2019 ; year1=2038 ; scenario='cntr1850' ; realisation='r1' ; grid='gn'  ; model='NorESM2-LM-C' # cntr1850 
#
#   METHANEMIP
#   ssp245
    elif ( expid == 'NSSP245_tropstratchem_01_f19_tn14_s01_20241118' ) : year0=2015 ; year1=2050 ; scenario='ssp245' ; realisation='r1i1p1f1' ; grid='gn'  ; model='NorESM2-LM'
    elif ( expid == 'NSSP245_tropstratchem_02_f19_tn14_s01_20241118' ) : year0=2015 ; year1=2050 ; scenario='ssp245' ; realisation='r2i1p1f1' ; grid='gn'  ; model='NorESM2-LM'
    elif ( expid == 'NSSP245_tropstratchem_03_f19_tn14_s01_20241118' ) : year0=2015 ; year1=2050 ; scenario='ssp245' ; realisation='r3i1p1f1' ; grid='gn'  ; model='NorESM2-LM'
    elif ( expid == 'NSSP245_tropstratchem_04_f19_tn14_s01_20241118' ) : year0=2015 ; year1=2050 ; scenario='ssp245' ; realisation='r4i1p1f1' ; grid='gn'  ; model='NorESM2-LM'
    elif ( expid == 'NSSP245_tropstratchem_05_f19_tn14_s01_20241118' ) : year0=2015 ; year1=2050 ; scenario='ssp245' ; realisation='r5i1p1f1' ; grid='gn'  ; model='NorESM2-LM'
    elif ( expid == 'NSSP245_tropstratchem_06_f19_tn14_s01_20241118' ) : year0=2015 ; year1=2050 ; scenario='ssp245' ; realisation='r6i1p1f1' ; grid='gn'  ; model='NorESM2-LM'
#   ssp245-tech
    elif ( expid == 'NSSP245TECH_tropstratchem_01_f19_tn14_s01_20241118' ) : year0=2020 ; year1=2050 ; scenario='ssp245-tech' ; realisation='r1i1p1f1' ; grid='gn'  ; model='NorESM2-LM'    
    elif ( expid == 'NSSP245TECH_tropstratchem_02_f19_tn14_s01_20241118' ) : year0=2020 ; year1=2050 ; scenario='ssp245-tech' ; realisation='r2i1p1f1' ; grid='gn'  ; model='NorESM2-LM'    
    elif ( expid == 'NSSP245TECH_tropstratchem_03_f19_tn14_s01_20241118' ) : year0=2020 ; year1=2050 ; scenario='ssp245-tech' ; realisation='r3i1p1f1' ; grid='gn'  ; model='NorESM2-LM'    
    elif ( expid == 'NSSP245TECH_tropstratchem_04_f19_tn14_s01_20241118' ) : year0=2020 ; year1=2050 ; scenario='ssp245-tech' ; realisation='r4i1p1f1' ; grid='gn'  ; model='NorESM2-LM'    
    elif ( expid == 'NSSP245TECH_tropstratchem_05_f19_tn14_s01_20241118' ) : year0=2020 ; year1=2050 ; scenario='ssp245-tech' ; realisation='r5i1p1f1' ; grid='gn'  ; model='NorESM2-LM'    
    elif ( expid == 'NSSP245TECH_tropstratchem_06_f19_tn14_s01_20241118' ) : year0=2020 ; year1=2050 ; scenario='ssp245-tech' ; realisation='r6i1p1f1' ; grid='gn'  ; model='NorESM2-LM'    
#   ssp245-ambi
    elif ( expid == 'NSSP245AMBI_tropstratchem_01_f19_tn14_s01_20241118' ) : year0=2020 ; year1=2050 ; scenario='ssp245-ambi' ; realisation='r1i1p1f1' ; grid='gn'  ; model='NorESM2-LM'    
    elif ( expid == 'NSSP245AMBI_tropstratchem_02_f19_tn14_s01_20241118' ) : year0=2020 ; year1=2050 ; scenario='ssp245-ambi' ; realisation='r2i1p1f1' ; grid='gn'  ; model='NorESM2-LM'    
    elif ( expid == 'NSSP245AMBI_tropstratchem_03_f19_tn14_s01_20241118' ) : year0=2020 ; year1=2050 ; scenario='ssp245-ambi' ; realisation='r3i1p1f1' ; grid='gn'  ; model='NorESM2-LM'    
    elif ( expid == 'NSSP245AMBI_tropstratchem_04_f19_tn14_s01_20241118' ) : year0=2020 ; year1=2050 ; scenario='ssp245-ambi' ; realisation='r4i1p1f1' ; grid='gn'  ; model='NorESM2-LM'    
    elif ( expid == 'NSSP245AMBI_tropstratchem_05_f19_tn14_s01_20241118' ) : year0=2020 ; year1=2050 ; scenario='ssp245-ambi' ; realisation='r5i1p1f1' ; grid='gn'  ; model='NorESM2-LM'    
    elif ( expid == 'NSSP245AMBI_tropstratchem_06_f19_tn14_s01_20241118' ) : year0=2020 ; year1=2050 ; scenario='ssp245-ambi' ; realisation='r6i1p1f1' ; grid='gn'  ; model='NorESM2-LM'    
#
#   ELSE
    else :
        print('No expid recognized : '+expid)
        quit()
#
    data={ 'year0' : year0, \
           'year1' : year1, \
           'scenario' : scenario, \
           'realisation' : realisation, \
           'grid' : grid, \
           'model' : model}
#
    return data



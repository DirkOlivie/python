def getfinalexpidinfo(expid) :
#-----------------------------
    '''
    INPUT

    MODIFICATIONS
        (2024-09-21) extended for CAMS bromoform simulations [Michael Gauss]
    '''

    print('Expid : ', expid)

#   CMIP6
#   aerosol-only
#   2x2
    if   ( expid == 'NHIST_f19_tn14_20190710'         )                         : year0=2000 ; year1=2014 ; scenario='hist-2x2' ; realisation='r1' ; grid='gn' ; calendar='noleap' ; model='NorESM2-LM'
    elif ( expid == 'NHIST_02_f19_tn14_20190813'      )                         : year0=2000 ; year1=2014 ; scenario='hist-2x2' ; realisation='r2' ; grid='gn' ; calendar='noleap' ; model='NorESM2-LM'
    elif ( expid == 'NHIST_03_f19_tn14_20190813'      )                         : year0=2000 ; year1=2014 ; scenario='hist-2x2' ; realisation='r3' ; grid='gn' ; calendar='noleap' ; model='NorESM2-LM'
    elif ( expid == 'NSSP585frc2_f19_tn14_20191014'   )                         : year0=2015 ; year1=2024 ; scenario='hist-2x2' ; realisation='r1' ; grid='gn' ; calendar='noleap' ; model='NorESM2-MM'

#   1x1
    elif ( expid == 'NHISTfrc2_f09_tn14_20191025'     )                         : year0=2000 ; year1=2014 ; scenario='hist-1x1' ; realisation='r1' ; grid='gn' ; calendar='noleap' ; model='NorESM2-MM'
    elif ( expid == 'NSSP585frc2_f09_tn14_20191105'   )                         : year0=2015 ; year1=2024 ; scenario='hist-1x1' ; realisation='r1' ; grid='gn' ; calendar='noleap' ; model='NorESM2-MM'
#
#   KEYclim full-chemistry
    elif ( expid == 'NHISTvsls_tropstratchem_prep_f09_nt14_20220223_test03'   ) : year0=2000 ; year1=2014 ; scenario='hist-1x1' ; realisation='r1' ; grid='gn' ; calendar='noleap' ; model='NorESM2-MM-C'
    elif ( expid == 'NSSP585vsls_tropstratchem_prep_f09_nt14_20220223_test01' ) : year0=2015 ; year1=2022 ; scenario='hist-1x1' ; realisation='r1' ; grid='gn' ; calendar='noleap' ; model='NorESM2-MM-C'
#
#   CAMS-VSLS [Michael Gauss]
    elif ( expid == 'NHISTfrc2sdyn_01_f09_tn14_bromo_r1995_sim03'   )           : year0=2000 ; year1=2014 ; scenario='hist-1x1' ; realisation='r1' ; grid='gn' ; calendar='gregorian' ; model='NorESM2-MM-bromo'
    elif ( expid == 'NSSP585frc2sdyn_01_f09_tn14_bromo_r1995_sim03'   )         : year0=2015 ; year1=2023 ; scenario='ssp585-1x1' ; realisation='r1' ; grid='gn' ; calendar='gregorian' ; model='NorESM2-MM-bromo'
    elif ( expid == 'NHISTSSP585frc2sdyn_01_f09_tn14_bromo_r1995_sim03'   )     : year0=2000 ; year1=2023 ; scenario='histssp585-1x1' ; realisation='r1' ; grid='gn' ; calendar='gregorian' ; model='NorESM2-MM-bromo'
    elif ( expid == 'NSSP585frc2sdyn_01_f09_tn14_bromo_r1995_sim03_2024_2025' ) : year0=2024 ; year1=2025 ; scenario='histssp585-1x1-2024-2025' ; realisation='r1' ; grid='gn' ; calendar='gregorian' ; model='NorESM2-MM-bromo'
#
#   HYWAY test Jan
    elif ( expid == 'NFHISTnorpddmsbc_tropstratchem_sdyn_01_f19_f19_r2000_s01_20250503' ) : year0=2010 ; year1=2014 ; scenario='nudged-2x2' ; realisation='r1' ; grid='gn' ; calendar='noleap' ; model='NorESM2-MM-C'

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
           'calendar' : calendar, \
           'model' : model}


    return data



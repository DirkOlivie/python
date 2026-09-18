def getfinalexpidinfo(expid) :
#-----------------------------
    '''
    INPUT


    '''

    print('Expid : ', expid)

#   ESM2025-WP1
#   aerosol-only
    if   ( expid == 'NF1850norbc_f19_20240312_test01'         )                    : year0=1 ; year1=40 ; scenario='piClim-control' ; realisation='r1i1p1f1' ; grid='gn' ; freqfile='monthly' ; model='NorESM2-LM'
    elif ( expid == 'NF1850norbc_aer2014_f19_20240312_test01' )                    : year0=1 ; year1=40 ; scenario='piClim-aer'     ; realisation='r1i1p1f1' ; grid='gn' ; freqfile='monthly' ; model='NorESM2-LM'
    elif ( expid == 'NF1850norbc_so22014_f19_20240312_test01' )                    : year0=1 ; year1=40 ; scenario='piClim-so2'     ; realisation='r1i1p1f1' ; grid='gn' ; freqfile='monthly' ; model='NorESM2-LM'
#   full chemistry
    elif ( expid == 'NF1850norbc_tropstratchem_f19_20240312_test01' )              : year0=1 ; year1=40 ; scenario='piClim-control' ; realisation='r1i1p1f1' ; grid='gn' ; freqfile='monthly' ; model='NorESM2-LM-C'
    elif ( expid == 'NF1850norbc_tropstratchem_aer2014_f19_20240312_test01' )      : year0=1 ; year1=40 ; scenario='piClim-aer'     ; realisation='r1i1p1f1' ; grid='gn' ; freqfile='monthly' ; model='NorESM2-LM-C'
    elif ( expid == 'NF1850norbc_tropstratchem_so22014_f19_20240312_test01' )      : year0=1 ; year1=40 ; scenario='piClim-so2'     ; realisation='r1i1p1f1' ; grid='gn' ; freqfile='monthly' ; model='NorESM2-LM-C'
    elif ( expid == 'NF1850norbc_tropstratchem_noxcovoc2014_f19_20240312_test01' ) : year0=1 ; year1=40 ; scenario='piClim-O3'      ; realisation='r1i1p1f1' ; grid='gn' ; freqfile='monthly' ; model='NorESM2-LM-C'
#
#   TOAR
#   radiative ozone = chemical ozone
    elif ( expid == 'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_fxemiyear_20240315_sim01'               )  : year0=1 ; year1=1 ; scenario='pdClim-control' ; realisation='r1i1p1f1' ; grid='gn' ; freqfile='monthly' ; model='NorESM2-LM-C'
    elif ( expid == 'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_ozon2050rad2015_fxemiyear_20240315_sim01'               )  : year0=1 ; year1=1 ; scenario='pdClim-control' ; realisation='r1i1p1f1' ; grid='gn' ; freqfile='monthly' ; model='NorESM2-LM-C'
    elif ( expid == 'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2050rad2015_fxemiyear_20240315_sim01'               )  : year0=1 ; year1=1 ; scenario='pdClim-control' ; realisation='r1i1p1f1' ; grid='gn' ; freqfile='monthly' ; model='NorESM2-LM-C'
#   prescribing the ozone climatologies
    elif ( expid == 'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2015_fxemiyear_20240315_sim01'     ) : year0=1 ; year1=1 ; scenario='pdClim-control' ; realisation='r1i1p1f1' ; grid='gn' ; freqfile='monthly' ; model='NorESM2-LM-C-O3clim'
    elif ( expid == 'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050_fxemiyear_20240315_sim01'     ) : year0=1 ; year1=1 ; scenario='pdClim-control' ; realisation='r1i1p1f1' ; grid='gn' ; freqfile='monthly' ; model='NorESM2-LM-C-O3clim'
    elif ( expid == 'NFSSP370norpddmsbc_tropstratchem_f19_mg17_toar_chem2015rad2015_o3clim2050chem_fxemiyear_20240315_sim01' ) : year0=1 ; year1=1 ; scenario='pdClim-control' ; realisation='r1i1p1f1' ; grid='gn' ; freqfile='monthly' ; model='NorESM2-LM-C-O3clim'
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
           'freqfile' : freqfile, \
           'model' : model}


    return data



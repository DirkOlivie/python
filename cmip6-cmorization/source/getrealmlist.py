import time


def getrealmlist(var, freqfile) :
#--------------------------------
#
    '''
    INPUT
        var
        freqfile

    COMMENT 
        Some variables exist both in Amon and AERmon : I had to choose ...


    MODIFICATIONS
        (2022-05-10) : added freqfile as input parameter
        (2025-05-21) : inventing new realm : AERZmon (with altitude as vertical coordinate)
        (2026-02-06) : adding '3hourly' as option for freqfile
        (2026-03-13) : adding 'orog' to fxlist
    '''

    realmlist=[]


#   monthly data
    if ( freqfile == 'monthly' \
      or freqfile == '3hourly' ) :

#       1. Amon
        Amonlist=['ccb', \
                  'cct', \
                  'cfc11global', 'cfc12global', 'ch4global', \
                  'cl', 'cli', 'clivi', 'clt', 'clw', 'clwvi', \
                  'co2mass', \
                  'evspsbl', \
                  'hfls', 'hfss', \
                  'hur', 'hurs', 'hus', 'huss', \
                  'n2oglobal', \
                  'o3', \
                  'pr', 'prc', 'prsn', 'prw', \
                  'ps', 'psl', \
                  'rlds', 'rlus', 'rlut', 'rlutcs', \
                  'rsds', 'rsdscs', 'rsdt', 'rsus', 'rsuscs', 'rsut', 'rsutcs', \
                  'rtmt', \
                  'sfcWind', \
                  'ta', 'tas', \
                  'tauu', 'tauv', \
                  'ts', \
                  'ua', \
                  'va', \
                  'wap', \
                  'zg']

        if ( var in Amonlist) : realmlist.append('Amon')

#       2. AERmon
        AERmonlist= ['abs550aer', \
                     'airmass', \
                     'aodvisvolso4', \
                     'bldep', \
                     'ch4losscl','ch4lossf','ch4lossoh','ch4losso1d', \
                     'c2h2', 'c2h4', 'c2h6', 'c3h6', 'c3h8', 'c6h6', 'ch3cho', 'ch3coch3', 'ch3cooh', 'ch3oh', 'ch4', 'co', 'h2o', 'hcho', 'hno3', 'ho2', \
                     'ccn', 'cdnc', 'chepsoa', \
                     'cod', \
                     'dms', \
                     'drybc', 'drych3coch3', 'ch3cooh', 'drych3oh','drych3cooh', 'drychocho', 'dryhcooh','drych4', 'dryco', 'dryh2', 'dryhcho', 'drydust', 'drymhp', 'dryo3', 'dryoa', 'drypan',  'dryso2', 'dryso4', 'dryss', \
                     'emibc', 'emibvoc', 'emico', 'emic6h6', 'emich3cho', 'emidms', 'emidust', 'emiisop', 'eminh3', 'emimtp', 'emioa', 'eminox', 'emiso2', 'emiso4', 'emiss', 'emivoc', \
                     'emic2h2', 'emic2h4','emic2h6','emic3h6','emic3h8','emich3coch3','emich3cooh','emich3oh','emihcho','emihcooh','emih2', \
                     'hcooh', \
                     'isop', \
                     'lossch3cho', 'lossch3coch3', 'lossch3oh', 'lossch3cooh', 'lossch4', 'losschocho', 'losshcho', 'losshcooh', 'lossh2', 'lossh2o', 'lossco', 'lossisop', 'losspan', \
                     'lwp', \
                     'mhp', 'mtp', \
                     'mmraerh2o', 'mmrbc', 'mmrdust', 'mmroa', 'mmrpm1', 'mmrpm2p5', 'mmrso4', 'mmrsoa', 'mmrss', \
                     'nh3','n2o','no','no2','no3','o1d','o3','o3st', \
                     'o3loss','o3prod', \
                     'od440aer', 'od550aer', 'od550aerh2o', 'od550bc', 'od550csaer', 'od550dust', 'od550lt1aer', 'od550oa', 'od550so4', 'od550ss', 'od870aer', \
                     'oh', \
                     'pan', \
                     'pfull', 'phalf', 'ps', \
                     'prodch3coch3', 'prodch3cooh', 'prodch3oh','prodco','prodh2','prodh2o','prodhcho', 'prodhcooh', 'prodmhp', 'prodpan', \
                     'ptp', \
                     'reffclwtop', \
                     'rlutaf', 'rlutcsaf', 'rsutaf', 'rsutcsaf', \
                     'so2', \
                     'toluene', \
                     'toz','tropoz', \
                     'ua', 'va', \
                     'volume', \
                     'wetbc', 'wetdust', 'wetoa', 'wetso2', 'wetso4', 'wetss', \
                     'wetch3cho', 'wetch3coch3', 'wetch3oh', 'wethcho', 'wethcooh', 'wetmhp', 'wetnh3', \
                     'zg', 'ztp', \
#                     original NORESM variables
                     'CDNUMC', \
                     'h2', \
                     'o3surface']
#
        if ( var in AERmonlist ) : realmlist.append('AERmon')    

#       3. CFmon
        CFmonlist = ['albiscc','clhcalipso','cllcalipso','clmcalipso','cltcalipso','cltisccp','hur','hus','pctisccp','ta']        

        if ( var in CFmonlist ) : realmlist.append('CFmon')

#       4. SImon
        SImonlist = ['siconc']

        if ( var in SImonlist ) : realmlist.append('SImon')
#
#       5. AERZmon
        AERZmonlist = ['o3']

        if ( var in AERZmonlist ) : realmlist.append('AERZmon')

#   daily data
    elif ( freqfile == 'daily' ) :
        print('Has to be added ...')
        quit()

#   constant data
    elif ( freqfile == 'fixed' ) :
#       1. fx
        fxlist = ['areacella','orog']

        if ( var in fxlist ) : realmlist.append('fx')

#   not monthly or daily
    else : 
        print('+++ getrealm +++')
        print('No freqfile recognized = '+str(freqfile))
        quit()
#
#  
    if ( len(realmlist) == 0) : 
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('+++ getrealmlist +++')
        print('Realmlist should contain at least 1 element')
        print('var : ', var)
        print('realmlist : ', realmlist)
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        time.sleep(3)
        quit()
 
    return realmlist

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
    '''

    realmlist=[]


#   monthly data
    if ( freqfile == 'monthly' ) :

#       Amon
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

#       AERmon
        AERmonlist= ['abs550aer', \
                     'airmass', \
                     'bldep', \
                     'ccn', 'cdnc', 'chepsoa', \
                     'co', \
                     'cod', \
                     'dms', \
                     'drybc', 'drydust', 'dryoa', 'dryso2', 'dryso4', 'dryss', \
                     'emibc', 'emibvoc', 'emidms', 'emidust', 'emiisop', 'emioa', 'emiso2', 'emiso4', 'emiss', 'emivoc', \
                     'isop', \
                     'lwp', \
                     'mmraerh2o', 'mmrbc', 'mmrdust', 'mmroa', 'mmrpm1', 'mmrpm2p5', 'mmrso4', 'mmrsoa', 'mmrss', \
                     'n2o','no','no2','o3','o3st', \
                     'o3loss','o3prod', \
                     'od440aer', 'od550aer', 'od550aerh2o', 'od550bc', 'od550csaer', 'od550dust', 'od550lt1aer', 'od550oa', 'od550so4', 'od550ss', 'od870aer', \
                     'oh', \
                     'pfull', 'phalf', 'ps', \
                     'reffclwtop', \
                     'rlutaf', 'rlutcsaf', 'rsutaf', 'rsutcsaf', \
                     'so2', \
                     'ua', 'va', \
                     'wetbc', 'wetdust', 'wetoa', 'wetso2', 'wetso4', 'wetss' \
                     'zg', 'ztp', \
#                     original NORESM variables
                     'CDNUMC']
#
        if ( var in AERmonlist ) : realmlist.append('AERmon')    
#
#   daily data
    elif ( freqfile == 'daily' ) :
        print('Has to be added ...')
        quit()

#   not monthly or daily
    else : 
        print('+++ getrealm +++')
        print('No freqfile recognized = '+str(freqfile))
        quit()
#
#  
    if ( len(realmlist) == 0) : 
        print('Realmlist should contain at least 1 element')
        print('var : ', var)
        print('realmlist : ', realmlist)
        quit()
 
    return realmlist

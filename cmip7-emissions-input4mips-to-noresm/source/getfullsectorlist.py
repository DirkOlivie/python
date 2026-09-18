def getfullsectorlist(activity, scenario, i4mpdownload):
#------------------------------
    '''
    MODIFICATIONS
        (2021-02-23) added possibility for sensitivity tests
        (2026-02-09) replaced 'ALL' by 'SINGLE'
        (2026-07-22) added 'ScenarioMIP' as scenario possibility
        (2026-08-20) changed 'anthro' into 'anthrosurfgas' as activity possibility ['anthro' should never have been used before hopefully]
        (2026-08-25) added 'volcstratclim' as activity possibility

    INPUT
        activity
        scenario

    CALLED BY
        composefield
    '''
#--------------------------------
#
    print('Starting : getfullsectorlist')
#    
#    srfemi  = getvalue_commonblock(descriptor='srfemi')
#    profemi = getvalue_commonblock(descriptor='profemi')
#
#   standard values
    srfemi  = 0          
    profemi = 0
#
    if (   activity == 'air'  ) : sectorlist=['SINGLE']
    elif ( activity == 'ocean') : sectorlist=['SINGLE']
    elif ( activity == 'soil' ) : sectorlist=['SINGLE']
    elif ( activity == 'volc' ) : sectorlist=['EXPL','CONT']
    elif ( activity == 'volcstratclim1850-2021' \
        or activity == 'volcstratclim1750-2023' ) : sectorlist=['SINGLE']
    elif ( activity == 'bb' \
        or activity == 'bbsurf' ) : 
        if ( scenario == 'hist' or scenario == 'CMIP' ) :
            sectorlist=['AGRI','BORF','DEFO','PEAT','SAVA','TEMF']
        elif ( scenario == 'ScenarioMIP' \
            or scenario.index('ssp') >= 0 ) :
            sectorlist=['AGRI','FORE','GRAS','PEAT']
        else :
            print('+++ getfullsectorlist +++') 
            print('No scenario recognized = ', scenario)
            quit()
    elif ( activity == 'anthrosurf' and i4mpdownload == 'GFDL' ) : sectorlist=['SINGLE'] 
    elif ( activity == 'anthrosurf' ) : 
        if   ( srfemi == 0 ) : sectorlist=['AGR',            'TRA','DOM','SOL','WST','SHP'] # standard
        elif ( srfemi == 1 ) : sectorlist=['AGR','ENE','IND','TRA','DOM','SOL','WST','SHP'] # perturbation for emission-MIP
        else : 
            print('+++ getfullsectorlist +++') 
            print('No srfemi recognized = ', srfemi)
            quit()
    elif ( activity == 'anthroprof' ) : 
        if   ( profemi == 0) : sectorlist=[      'ENE','IND'                              ] # standard
        elif ( profemi == 1 ) : sectorlist=['AGR','ENE','IND','TRA','DOM','SOL','WST','SHP'] # perturbation for emission-MIP
        else : 
            print('+++ getfullsectorlist +++')
            print('No profemi recognized = ', profemi)
            quit()
    elif ( activity == 'anthrosurfgas' ) : sectorlist=['AGR','ENE','IND','TRA','DOM','SOL','WST','SHP']
    else :
        print('+++ getfullsectorlist +++')
        print('No activity recognized : ', activity)
        quit()
#
    return sectorlist


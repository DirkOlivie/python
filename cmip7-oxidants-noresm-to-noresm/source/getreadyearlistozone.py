import numpy as np

def getreadyearlistozone(yearlist, scenario, activity, i4mpdownload):
#-----------------------
    '''
    MODIFICATIONS
        (2026-07-22) creation

    INPUT
        yearlist
        scenario
        activity
        i4mpdownload

    RETURNS
        modified 


    '''

    if ( actvity != 'ozone' ) :
        print('+++ getreadyearlistozone +++')
        print('Only ozone activity allowed : ', activity)
        quit()

    nyear=len(yearlist)

    readyearlist = np.zeros(nyear, dtype=int)

    for iyear in range(nyear) :
        year = yearlist[iyear]

        if   ( scenario == 'CMIP'        and year <  1850 ) : readyearlist[iyear] = 1850
        elif ( scenario == 'ScenarioMIP' and year == 2101 ) : readyearlist[iyear] = 2100
        else                                        : readyearlist[iyear] = year

    return readyearlist

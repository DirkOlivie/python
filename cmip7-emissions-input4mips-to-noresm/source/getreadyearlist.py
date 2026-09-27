import numpy as np

def getreadyearlist(yearlist, scenario, activity, i4mpdownload):
#------------------
    '''
    MODIFICATIONS
        (2026-03-15) added i4mpdownload as argument


    INPUT
        yearlist
        scenario
        activity
        i4mpdownload

    '''
    nyear=len(yearlist)

    readyearlist = np.zeros(nyear, dtype=int)

    for iyear in range(nyear) :
        year = yearlist[iyear]

        if   ( scenario == 'hist' and year > 2019 and i4mpdownload == 'GFDL' ) : readyearlist[iyear] = 2019
        elif ( scenario == 'hist' and year > 2023                            ) : readyearlist[iyear] = 2023
        elif ( scenario == 'ScenarioMIP' and year == 2101                    ) : readyearlist[iyear] = 2100
        else                                                                   : readyearlist[iyear] = year

    return readyearlist

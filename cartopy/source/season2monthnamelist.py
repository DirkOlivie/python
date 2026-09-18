import numpy as np

def season2monthnamelist (season):
#-----------------------    
    '''
    MODIFICATIONS
        (2022-09-07) : creation
        (2024-02-19) : changed function name : season2monthlist -> season2monthnamelist
    '''
    if   ( season == 'JAN' ) : monthlist=[season]
    elif ( season == 'FEB' ) : monthlist=[season]
    elif ( season == 'MAR' ) : monthlist=[season]
    elif ( season == 'APR' ) : monthlist=[season]
    elif ( season == 'MAY' ) : monthlist=[season]
    elif ( season == 'JUN' ) : monthlist=[season]
    elif ( season == 'JUL' ) : monthlist=[season]
    elif ( season == 'AUG' ) : monthlist=[season]
    elif ( season == 'SEP' ) : monthlist=[season]
    elif ( season == 'OCT' ) : monthlist=[season]
    elif ( season == 'NOV' ) : monthlist=[season]
    elif ( season == 'DEC' ) : monthlist=[season]
    elif ( season == 'DJF' ) : monthlist=['DEC','JAN','FEB']
    elif ( season == 'MAM' ) : monthlist=['MAR','APR','MAY']
    elif ( season == 'JJA' ) : monthlist=['JUN','JUL','AUG']
    elif ( season == 'SON' ) : monthlist=['SEP','OCT','NOV']
    elif ( season == 'YEA' ) : monthlist=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    else : quit()

    return monthlist 

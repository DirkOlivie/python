import numpy as np
    
def season2monthnumberlist ( season) :
#-------------------------------
    '''
	MODIFICATIONS
		(2022-02-02) creation
                (2024-02-19) change name : season2monthlist -> season2monthnumberlist

    	INPUT
    		loninbd  : size = #longitudes+1 (because bounds)
                    lonoutbd : size = #longitudes+1 (because bounds)
  
    '''

    if   ( season == 'JAN' ) : monthlist=[1]
    elif ( season == 'FEB' ) : monthlist=[2]
    elif ( season == 'MAR' ) : monthlist=[3]
    elif ( season == 'APR' ) : monthlist=[4]
    elif ( season == 'MAY' ) : monthlist=[5]
    elif ( season == 'JUN' ) : monthlist=[6]
    elif ( season == 'JUL' ) : monthlist=[7]
    elif ( season == 'AUG' ) : monthlist=[8]
    elif ( season == 'SEP' ) : monthlist=[9]
    elif ( season == 'OCT' ) : monthlist=[10]
    elif ( season == 'NOV' ) : monthlist=[11]
    elif ( season == 'DEC' ) : monthlist=[12]

    elif ( season == 'YEA' ) : monthlist=[1,2,3,4,5,6,7,8,9,10,11,12]

    elif ( season == 'MAM' ) : monthlist=[3,4,5]
    elif ( season == 'JJA' ) : monthlist=[6,7,8]
    elif ( season == 'SON' ) : monthlist=[9,10,11]
    elif ( season == 'DJF' ) : monthlist=[1,2,12]
    else : 
        print('No season recognized :')
        print(season)
        exit()

    return monthlist

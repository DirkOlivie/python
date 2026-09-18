import sys
sys.path.insert(0,'/nird/home/olivie/code/python/cartopy/source')
import readsinglefield
import readsinglehxfield

def readsinglefieldgeneral(expid, variable, date):
#-------------------------
    '''
    INPUT
        expid
        variable
        date : yyyy-mm or yyyy-mm-dd-hh:mm:ss    

    CALLS
        readsinglefield         : for monthly
        readsinglefield_3hourly

    '''

    if ( ':00:00' in date ) :
        data=readsinglehxfield.readsinglehxfield(expid,variable,date, hx='h1', dhx='10800')
    else :
        data=readsinglefield.readsinglefield(expid, variable, date)

    return data

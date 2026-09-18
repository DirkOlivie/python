import numpy as np

def getseasonalcycle(data, vartype):
#-------------------
    '''
    INPUT
        data=D : timeseries data
        vartype : 
               var-unweighted : every year weights the same
               var-weighted   : every year is used according to its % coverage 
               weight

    RETURN
       structure containing seasonal cyccle
               var
               Ex
               Exx
               sigma
               Emin            
               Emax

    CALLED BY
        analyseseries
 
    CALLS 

    '''
#------------------------------------------------------------
#
    nmonth=12
#
    monthlist=np.arange(0,nmonth,dtype=int) + 1 # runs from 1 -> 12
    timelist=monthlist

#   initialize empty arrays
    Ex = np.zeros(nmonth,dtype=float)
    Exx= np.zeros(nmonth,dtype=float)
    sigma=np.zeros(nmonth,dtype=float)

    Emin = np.zeros(nmonth,dtype=float)
    Emax = np.zeros(nmonth,dtype=float)

#   loop over all 12 months
    for imonth in range(0,nmonth):
        month=imonth+1

        iset = ( data['monthlist'] == month ) # [False, False, True, False, ...]
        
        nset = sum(iset) # sums up only the True

        if ( nset > 0 ) :

            if   ( vartype == 'var-unweighted' ) : x = data['valuelist'][iset]  ; w = np.zeros(nset,dtype=float) + 1. # every month gets weight 1 
            elif ( vartype == 'var-weighted'   ) : x = data['valuelist'][iset]  ; w = data['masklist'][iset]             
            elif ( vartype == 'weight'         ) : x = data['masklist'][iset]   ; w = np.zeros(nset,dtype=float) + 1.
            else : 
                print('No vartype recognized : ', vartype)
                quit()

#           weight every month according to mask
            Ex[imonth]    = np.sum( x     * w ) / np.sum(w)
            Exx[imonth]   = np.sum( x * x * w ) / np.sum(w)
            sigma[imonth] = np.sqrt(Exx[imonth] - Ex[imonth]*Ex[imonth])
#
            Emin[imonth] = np.min(x)
            Emax[imonth] = np.max(x)
#
        else :
            Ex[imonth]   = np.nan
            Exx[imonth]  = np.nan
            sigma[imonth]= np.nan
            Emin[imonth] = np.nan
            Emax[imonth] = np.nan

    outputdata = { 'var'    : data['var'], \
                   'region' : data['region'], \
                   'units'  : data['units'], \
                   'Ex'     : Ex, \
                   'Exx'    : Exx, \
                   'sigma'  : sigma, \
                   'Emin'   : Emin, \
                   'Emax'   : Emax, \
                   'monthlist':monthlist, \
                   'timelist' : timelist}
#
    return outputdata

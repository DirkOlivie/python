import numpy as np

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getlenintervaloverlap
import getboundsintervaloverlap
import integr1d

def getwavelengthweight( wvl_bnds0, wvl_bnds2, spectrum):
#-----------------------
    '''
    INPUT
        wvl_bnds0 : original
        wvl_bnds2 : final       
        spectrum  : None | a real sepctrum

    RETURN
        weight : 2-dimensioanl array

    CALLS
        getlenintervaloverlap
        getboundsintervaloverlap

    '''
#
#   number of wavelengths
    nwvl0 = len(wvl_bnds0) - 1
    nwvl2 = len(wvl_bnds2) - 1    

#   INTERPOLATION WEIGHT
    weight      = np.zeros((nwvl2,nwvl0), dtype=float)
    for iwvl2 in range(nwvl2) :          # final wavelength
        for iwvl0 in range (nwvl0) :    # original wavelength

            x = [ wvl_bnds0[iwvl0] , wvl_bnds0[iwvl0+1] ]     # original wavelength
            y = [ wvl_bnds2[iwvl2] , wvl_bnds2[iwvl2+1] ]     # final wavelength

#           standard interpolation
            if ( spectrum == None ) :

                overlaplength       = getlenintervaloverlap.getlenintervaloverlap ( x , y )                         # returns length of the overlap
                baselength          = wvl_bnds2[iwvl2+1] - wvl_bnds2[iwvl2]  
                weight[iwvl2,iwvl0] = overlaplength / baselength   # overlap width / final widht       

#           weighting with some spectrum
            else :

                overlapbounds=getboundsintervaloverlap.getboundsintervaloverlap ( x , y )
                if ( overlapbounds != None ) :

                    overlapintegral     = integr1d.integr1d(x=spectrum['wavelength'] ,fx=spectrum['valuelist'], x0=overlapbounds[0], x1=overlapbounds[1])
                    baseintegral        = integr1d.integr1d(x=spectrum['wavelength'] ,fx=spectrum['valuelist'], x0=y[0]            , x1=y[1]            )
                    weight[iwvl2,iwvl0] = overlapintegral / baseintegral 

            if ( weight[iwvl2,iwvl0] != 0. ) :
                print('iwvl2, iwvl0, weight : ', iwvl2, iwvl0, weight[iwvl2,iwvl0])

    return weight

import numpy as np
import copy

def intplev(levinbd, levoutbd, extrapolate=False):
#-----------
    '''  
    INPUT
        levinbd=x : boundaries of input intervals
        levoutbd=y : boundaries of output intervals
        extrapolate
            0 : no extrapolation
            1 : extrapolation (the pressure boundaries of the original grid are extended tot the boundaries of the final grid)

    METHOD
        conv=fltarr(nlevout,nlevin) : indicates how much (weight) an output level coincides with an input level
    
    OUTPUT
        pt=pt : (nlevout, 50) : 
            0 : indicates number of input levels that contributes to output level
            1-49 : number of input levels that contribute

        wt=wt : (nlevout, 50) : the weights of these contribution
    
    REMARK : interpretation of UPWARD/DOWNWRD
                         UPWARD                     DOWNWARD
                 pressure <=> level            level <=/\=> pressure

                     0 hPa    0-------------------60        0 hPa


                    20 hPa    1-------------------59       20 hPa


                               --------------------


                   994 hPa   59-------------------1      994 hPa 

               1013.25 hPa   60-------------------0     1013.25 hPa
                               ///\\\///\\\///\\\/ 
    '''

    x = levinbd
    y = levoutbd

    nlevin=len(x)-1
    nlevout=len(y)-1 

#   increasing or decreasing (correspondence between level counting and pressure)
    xupward=0 # level=0 <=> press=surface pressure ; level=nlev <=> press=TOA pressure
    yupward=0 # 
    if ( x[1] > x[0] ) : xupward = 1 # level=0 <=> press=TOA pressure ; level=nlev <=> press=surface pressure
    if ( y[1] > y[0] ) : yupward = 1
#
#   copy of the original pressure boundaries
    xextra=copy.deepcopy(x)
#
    ymin=min(y)
    ymax=max(y)

#   lowering the lowest pressure a lot and increasing the highest pressure a lot
    if ( extrapolate ) :
        if ( xupward == 1 ) : # level=0 <=> press=TOA pressure~0; level=nlev <=> press=surface pressure	   
            xextra[0]      = min([xextra[0],ymin])	   
            xextra[nlevin] = max([xextra[nlevin],ymax])
        else                : # level=0 <=> press=surface pressure ; level=nlev <=> press=TOA pressure	   
            xextra[0]      = max([xextra[0],ymax])
            xextra[nlevin] = min([xextra[nlevin],ymin])
#
#   indicates how much an input levels coincides with an output level
    conv=np.zeros((nlevout,nlevin), dtype=float)
#
    xmin=min(xextra)
    xmax=max(xextra)
#
    for ilevout in range(0, nlevout) :
#       the lower and upper boundaries and tickness of output level	
        y0=min([y[ilevout],y[ilevout+1]])
        y1=max([y[ilevout],y[ilevout+1]])
        wy=y1-y0

        for jlevin in range(0, nlevin) : 
#           the lower and upper boundaries of input level	
            x0=min([xextra[jlevin],xextra[jlevin+1]])
            x1=max([xextra[jlevin],xextra[jlevin+1]])
#
            if ( y1 >= x0 and y0 <= x1) :
#               the thickness of the overlap interval
                z0=max([x0,y0])
                z1=min([x1,y1])
                wz=abs(z1-z0)   
                conv[ilevout,jlevin]=wz/wy
#   2. calculation of wt and pt
    wt=np.zeros((nlevout,50), dtype=float)
    pt=np.zeros((nlevout,50), dtype=int)
#
    for ilevout in range(0, nlevout) :
        ncontr=0	
        for jlevin in range (nlevin) :
            if ( conv[ilevout,jlevin] > 0. ) :
                ncontr=ncontr+1 
                pt[ilevout,0]=ncontr
                pt[ilevout,ncontr]=jlevin
                wt[ilevout,ncontr]=conv[ilevout,jlevin]
#
    return pt, wt

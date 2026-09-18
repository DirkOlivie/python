import numpy as np

def intplat ( latinbd , latoutbd ) :
#-----------------------------------
    '''
    INPUT 
       x (latinbd) : 1-dimesional array [nlatin]
       y (latoutbd): 1-dimensonal array [nlatout]

    CALCULATE
       conv : 2-dimensional array [nlatout,nlatin] : how much each (x) interval contributes to (y) interval
                                                     takes into account sinus of the latitde

    RETURN            
       wt   : 2-dimensional array [nlatout,20]
       pt   : 2-dimensional array [nlatout,20] : integers !

    METHOD        
                                        x0    (ilatin)       x1     
                                        |--------------------|
                     
                                   y0 (jlatout) y1
                                   |------------|

                                        z0      z1                                    
                                        |-------|                                                                          

    '''
#----------------------------------------------
#
    x=latinbd        # latitude boundaries, so is 1 larger than latitudes
    y=latoutbd       # latitude boundaries, so is 1 larger than latitudes

    nlatin=len(x)-1  # number of latitudes
    nlatout=len(y)-1 # number of latitudes
#
# 1. calculation of conv : how much (=weight) contributes jlatin to ilatout
    conv=np.zeros((nlatout,nlatin), dtype=float)
#
    for ilatout in range(0,nlatout) :
        y0=min([y[ilatout],y[ilatout+1]])
        y1=max([y[ilatout],y[ilatout+1]])
        wy=abs(np.sin(y0*np.pi/180.)-np.sin(y1*np.pi/180.))

        for jlatin in range(0,nlatin) :
            x0=min([x[jlatin],x[jlatin+1]])
            x1=max([x[jlatin],x[jlatin+1]])

            if ( y1 >= x0 and y0 <= x1) :  # ge , le
                z0=max([x0,y0])
                z1=min([x1,y1])
                wz=abs(np.sin(z0*np.pi/180.)-np.sin(z1*np.pi/180.))
                conv[ilatout,jlatin]=wz/wy
#
# 2. calculation of wt and pt
    wt=np.zeros((nlatout,20), dtype=float)   # 
    pt=np.zeros((nlatout,20), dtype=int)     # integers ! will contain "ilat" from all gridpoints that contribute
#
    for ilatout in range(0, nlatout) :
        ncontr=0
        for ilatin in range(0, nlatin) :
            if ( conv[ilatout,ilatin] > 0. ) : # gt
                ncontr=ncontr+1
                pt[ilatout,0]=ncontr                     # zero-th element  : how many gridpoints contribute
                pt[ilatout,ncontr]=ilatin                # other   elements : which (=ilat) contributes  
                wt[ilatout,ncontr]=conv[ilatout,ilatin]  #
#
#    print(pt)
#    print(wt)

    return pt, wt

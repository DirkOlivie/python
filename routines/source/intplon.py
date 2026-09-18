import numpy as np
    
def intplon ( loninbd , lonoutbd ) :
#-----------------------------------
    '''
    	INPUT
    		loninbd  : size = #longitudes+1 (because bounds)
                    lonoutbd : size = #longitudes+1 (because bounds)
  
    '''
    x=loninbd
    y=lonoutbd
    
    nlonin=len(x)-1
    nlonout=len(y)-1
  
    print('nlonin', nlonin) 
    print('nlonout', nlonout)
    
#   1. calculation of conv
    conv=np.zeros((nlonout,nlonin), dtype=float)
#    
    for ilonout in range(0,nlonout) :
        for jlonin in range(0,nlonin) :
#           
            y0=y[ilonout]
            y1=y[ilonout+1]
#           
            x0=x[jlonin]
            x1=x[jlonin+1]
#    
#           shift everything such that
#           x0=0 degrees
#           all angles are in [0 , 360] degrees
#    
            x1=(x1-x0+720.) % 360.        #     modulo
            if ( x1 <= 0.01 ) : x1 = 360. #     le
            y0=(y0-x0+720 ) % 360.        #     modulo
            y1=(y1-x0+720.) % 360.        #     modulo
            if ( y1 <= 0.01 ) : y1 = 360. #     le
            x0=0.
#    
            wy=(y1-y0+720.) % 360.        #     modulo
            if ( wy <= 0.01 ) : wy=360.   #     le
#    
            wz=0.
            if ( y0 < y1 ) :              #     lt
#     normal case
                if ( y1 >= x0 and y0 <= x1) : # ge , le
                    z0=max([x0,y0])
                    z1=min([x1,y1])
                    wz=abs(z1-z0)
               
            else :
                wz=min([x1,y1])+max([0.,x1-y0])
#    
            conv[ilonout,jlonin]=wz/wy
#

    print('conv')
    print(conv)

    
#   2. calculation of weights
    wt=np.zeros((nlonout,50),dtype=float)
    pt=np.zeros((nlonout,50),dtype=int)  #     integers

    for ilonout in range(0,nlonout) :
        ncontr=0
        for ilonin in range(0, nlonin) : 
            if ( conv[ilonout,ilonin] > 0. ) :
                ncontr=ncontr+1
                pt[ilonout,0]=ncontr
                pt[ilonout,ncontr]=ilonin
                wt[ilonout,ncontr]=conv[ilonout,ilonin]

    print('pt')
    print(pt)
    print('wt')
    print(wt)

    
    return pt, wt

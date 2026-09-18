import numpy as np

def integr1d (x, fx, x0, x1) :
#------------------------
    '''
    REMARK
        extrapolates : takes last value   

    METHOD
                             o
                             |
                             |                   o 
              o         |    |                   |
              |     o   | fx(2)                  |  
           fx(0)    |   |    |                fx(3)                      
              |  fx(1)  |    |                   |
              |     |   |    |                   |               
    ----------|-----|--------|-------------------|--
            x(0)  x(1)  ^  x(2)             ^  x(3)          
                        |                   |
                        x0 -----------------x1

    INPUT
        x  : points where function is given
        fx : values of given function
        x0 : start of integration interval
        x1 : end of integration interval

    '''
# 
#    print('+++ integr1d +++')
#    print('x  : ', x)
#    print('fx : ', fx)
#    print('x0 : ', x0)
#    print('x1 : ', x1)

#   x-array and fx-array should have the same length
    if ( len(x) != len(fx) ) : 
        print('+++ integr1d +++')
        print('x and fx have different size')
        print('x  : ', len( x))
        print('fx : ', len(fx))  
        quit()
#   
#   x-values should be in increasing order
    for i in range(len(x)-1) :
        if ( x[i+1] <= x[i] ) :
            print('+++ integr1d +++')            
            print('x-values not in increasing order : ', x)
            quit()
#
#   check order of integration bounds
    if ( x1 <= x0 ) :
        print('+++ integr1d +++')
        print('integration bounds not in increasing order : ', x0, x1)
        quit()


#
#   is integration interval inside function domain
    if ( x0 < np.amin(x) \
      or x1 > np.amax(x) ) :
        print('+++ integr1d +++')
        print('integration interval is outside original function domain : ')
        print('inegration interval : ',  x0, x1)
        print('original function domain : ', np.amin(x), np.amax(x))
        quit()   

#   integration
    nx=len(x)

    integral=0.

    for ix in range(0,nx-1) :
        xa=x[ix]
        xb=x[ix+1]
        fa=fx[ix]
        fb=fx[ix+1]

        xlow=np.amax([xa,x0])
        xhigh=np.amin([xb,x1])
#        print(xlow,xhigh)

        if ( xlow < xhigh) :
            integral = integral + (xhigh-xlow) * ( fa + (fb-fa)/(xb-xa) * ( (xlow+xhigh)/2. - xa ) )

#   
    return integral

import numpy as np

def getlinearregression (x, y, imposethroughorigin=None) :
#-------------------------------------------------
    '''
    INFO :
        https://en.wikipedia.org/wiki/Simple_linear_regression

        If needs to go through origin : can also be found here


        y = alpha + beta * x
    '''

    Ex  = np.mean(x)
    Ey  = np.mean(y)
    Exy = np.mean(x*y)
    Exx = np.mean(x*x)

    Sxx = np.mean((x-Ex)*(x-Ex))
    Syy = np.mean((y-Ey)*(y-Ey))
    Sxy = np.mean((x-Ex)*(y-Ey))

    if ( imposethroughorigin == None ) :

        Rxy = ( Exy - Ex*Ey) / np.sqrt(Sxx*Syy)

        beta = Rxy * np.sqrt(Syy) / np.sqrt(Sxx)

        alpha = Ey - beta * Ex

    elif ( imposethroughorigin == True ) :

        beta = Exy / Exx

        alpha = 0.

        Rxy = None

    else :

        print('No imposethroughorigin recognized : ', imposethroughorigin)
        quit()

    data = { 'alpha' : alpha, \
             'beta'  : beta, \
             'r'     : Rxy}

    return data

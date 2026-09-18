import numpy as np

def getboundsintervaloverlap ( x , y ) :
#---------------------------
    '''
    INPUT 
        x : 1-dimesional array with 2 elements
        y : 1-dimesional array with 2 elements

    OUTPUT
        begin and endrange of overlap

    '''
#
    if ( len(x) != 2 or len(y) != 2 ) :
        print('+++ getboundsintervaloverlap +++')
        print('length x : ', len(x))
        print('length y : ', len(y))  
        quit()
#
    xmin = np.amin(x)
    xmax = np.amax(x)
    ymin = np.amin(y)
    ymax = np.amax(y)
    
    low=np.max([xmin,ymin])
    hgh=np.min([xmax,ymax])

    if ( low < hgh ) :
        overlap=[low,hgh]
    else :
        overlap = None

    return overlap

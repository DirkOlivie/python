import numpy as np

def writeminmax(datalist) :
#--------------
    '''


    '''

    ndata=len(datalist)

    if ( ndata != 2 ) :
        print('+++ writeminmax +++')
        print('Only works for two datasets.  #datasets : ', ndata)
        quit()

    ntime=len(datalist[0]['yearlist'])


    for itime in range(ntime) :
        print(datalist[0]['variable'], str("%2.2i"% (itime)), \
                                       str("%10.7f"% (np.min( datalist[0]['field'][itime,:,:]-datalist[1]['field'][itime,:,:]))),
                                       str("%10.7f"% (np.max( datalist[0]['field'][itime,:,:]-datalist[1]['field'][itime,:,:]))),
                                       str("%10.7f"% (np.mean(datalist[0]['field'][itime,:,:]-datalist[1]['field'][itime,:,:]))))

import numpy as np

def getdistribution(D) :
#------------------
    '''


    '''
    if ( D['variable'] == 'SSTbef' \
      or D['variable'] == 'SSTaft' ) :
        boundlist=np.array([-100,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,\
                                                                  11,12,13,14,15,16,17,18,19,20, \
                                                                  21,22,23,24,25,26,27,28.29,30, \
                                                                  31,32,33,34,35,36,37,38,39,40])
    elif ( D['variable'] == 'SICbef' \
        or D['variable'] == 'SICaft' ) :
        boundlist=np.array([-100,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,100])
    else :
        print('+++ getdistribution +++')
        print('No variable recognized : ', D['variable'])
        quit()
 #  
    nbound = len(boundlist)
    intervaldistributionlist = np.zeros(nbound-1,dtype=float)
    boundarydistributionlist = np.zeros(nbound    ,dtype=float)

#
    ntime, nlat, nlon = D['field'].shape
#
#   intervals
    for i in range(0,nbound-1) :
        intervaldistributionlist[i] = len(D['field'][(D['field'] > boundlist[i])*(D['field'] < boundlist[i+1])])
#
    for i in range(0,nbound) :
        boundarydistributionlist[i] = len(D['field'][D['field'] == boundlist[i]])
#
#
    data = {'boundlist' : boundlist, \
            'intervaldistributionlist' : intervaldistributionlist, \
            'boundarydistributionlist' : boundarydistributionlist}
#
    return data

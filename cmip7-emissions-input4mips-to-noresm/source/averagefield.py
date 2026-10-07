def averagefield(data, weightlist):
#---------------
    '''
    INPUT
        data
        weightlist

    '''
#
    nmonth=12
#
#   number of timesteps should be multiple of 12
    if ( ( data['ntime'] % nmonth ) != 0 ) :
        print('+++ averagefield +++')
        print('# timesteps not multipel of 12 : ', data['ntime'] )
        quit()

#   number of years to treat
    nyear = data['ntime'] // nmonth

#   number of weights
    if ( len(weightlist) != nyear ) :
        print('+++ averagefield +++')
        print('#years different from #weights : ', len(weightlist), nyear)
        quit()

#   find dimensions in original data
    ndim = data['field'].ndim

#   average field
    for iyear in range(nyear) :
    
        if   ( ndim == 2 ) : extract = data['field'][nmonth*iyear:nmonth*(iyear+1),:    ]
        elif ( ndim == 3 ) : extract = data['field'][nmonth*iyear:nmonth*(iyear+1),:,:  ]
        elif ( ndim == 4 ) : extract = data['field'][nmonth*iyear:nmonth*(iyear+1),:,:,:]
        else : 
            print('+++ averagefield +++')
            print('No data dimensions recognized : ', ndim)
            quit()

        if ( iyear == 0 ) :
            newfield =            extract * weightlist[iyear] 
        else :
            newfield = newfield + extract * weightlist[iyear]
#
#   new yearlist and monthlist : take the year in the middle
    iyear =  nyear // 2
    print(data)

    newyearlist  = data['yearlist'][nmonth*iyear:nmonth*(iyear+1)]
    newmonthlist = data['monthlist'][nmonth*iyear:nmonth*(iyear+1)]   
#   
#   new data structure
    newdata = { 'activity'   : data['activity'], \
                'sector'     : data['sector'], \
                'species'    : data['species'], \
#
                'field'      : newfield, \
                'longitude'  : data['longitude'], \
                'latitude'   : data['latitude'], \
                'area'       : data['area'], \
                'dim'        : data['dim'], \
                'units'      : data['units'], \
                'area_units' : data['area_units'], \
                'yearlist'   : newyearlist, \
                'monthlist'  : newmonthlist, \
                'ntime'      : nmonth} #

#
#   return structure
    if ( data['dim'] == '2d' ) :

        print('... nothing to be added ...')

    elif ( data['dim'] == '3d' ) :
        newdata.update({ \
#           'level'     : data['level'], \
            'levbnds'   : data['levbnds'], \
            'lev_units' : data['lev_units']})

    else :
        print('+++ averagefield +++')
        print('No dimension recognized : ', data['dim'])
        quit()

    return newdata

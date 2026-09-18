import numpy as np

import getaerocomvarcomponents

import os, sys

import copy

sys.path.insert(0,'/nird/home/olivie/code/python/cartopy/source')
import readsinglefield
import readsinglemap
import readsingleh1field

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getconversionfactorunits
import getstandardunits

def obtainfield(expid,var,year,month,day) :
#--------------
    '''
    INPUT
        expid
        var
        year
        month
        day
        
    CALLS
        getaerocomvarcomponents
        reasinglefield       [cartopy/source]
        readsingleh1field    [cartopy/source]

    
        getstandardunits
        getconversionfactorunits
    '''

    print('+++ obtainfield +++')

#   find the date
    cyear=str("%4.4i"% (year))
    cmonth=str("%2.2i"% (month))
    date=cyear+'-'+cmonth
    if ( day != None ) :
        cday=str("%2.2i"% (day))   
        date=date+'-'+cday

#   contributing fields
    varinfo = getaerocomvarcomponents.getaerocomvarcomponents(var=var, expid=expid)
    clist   = varinfo['clist']        
    cnoemer = varinfo['cnoemer']
    action  = varinfo['action']
    wlist   = varinfo['wlist']
    desiredunits = varinfo['desiredunits']

    ncomp=len(clist)

#   teller : add up contributions
    for icomp in range(0,ncomp) :

#       read component
#        tmp=readsinglefield.readsinglefield(expid, clist[icomp], date) # contains original units
        if ( day == None ) : tmp=readsinglemap.readsinglemap(expid, clist[icomp], date) # monthly
        else               : tmp=readsingleh1field.readsingleh1field(expid, clist[icomp], date) # daily 

#       initialization of total field
        if ( icomp== 0 ) :
            data=copy.deepcopy(tmp)
            data['field'][:,:] = 0.

#       check whether all units are the same
        if ( tmp['units'] != data['units'] ) : 
            print('Components have different units')
            print('Up to now : ', data['units'])
            print('Latest contribution : ', tmp['units'])
            print('All components : ', clist)
            print('Latest component : ', clist[icomp])
            quit()

#       add the component contribution
        data['field'] = data['field'] + tmp['field'] * wlist[icomp]
#           
#   noemer : division if needed 
    if ( cnoemer != None ) :

        if ( day == None ) : tmp=readsinglefield.readsinglefield(expid, cnoemer, date)     # monthly
        else               : tmp=readsingleh1field.readsingleh1field(expid, cnoemer, date) # daily

#       data['field'] = np.where( tmp['field'] >= 0., data['field'] / tmp['field'], 0.) 
        data['field'] =  data['field'] / ( tmp['field'] + 1.e-10 ) 

#   check standard writing of units
    data['units'] = getstandardunits.getstandardunits(units=data['units'])

#   convert mmr -> conc, 
#    if ( action == 'mmr2conc+surfacelevel' ) :
#
#
    print('... here ...')     

#   check units
    if ( desiredunits != None ) :
        factor = getconversionfactorunits.getconversionfactorunits(origunits=data['units'],finalunits=desiredunits)
        data['field'] = data['field'] * factor
        data['units'] = desiredunits
#
    return data

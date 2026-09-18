import numpy as np

import getcmorvarcomponents
import convert3dplev19

import os, sys

import copy

import readsingleh0field

import getconversionfactorunits
import getstandardunits

def obtainfield(expid,var,year,month,desiredunits,cdim) :
#--------------
    '''
    INPUT

    CALLS
        getcmorvarcomponents
        reasinglefield

    


    '''

    print('+++ obtainfield +++')

#   find the date
    cyear=str("%4.4i"% (year))
    cmonth=str("%2.2i"% (month))
    date=cyear+'-'+cmonth

#   contributing fields
    clist,wlist,cnoemer = getcmorvarcomponents.getcmorvarcomponents(var=var) # contains final units
    ncomp=len(clist)

#   teller : add up contributions
    for icomp in range(0,ncomp) :

#       read component
        tmp=readsingleh0field.readsingleh0field(expid, clist[icomp], date) # contains original units

#       initialization of total field
        if ( icomp== 0 ) :
            data=copy.deepcopy(tmp)
            ndim=data['field'].ndim
            if   ( ndim == 2 ) : data['field'][:,:] = 0.
            elif ( ndim == 3 ) : data['field'][:,:,:] = 0.
            else :
                print('No # dimensions recognized : ', ndim)
                quit()

#       check whether all units are the same
        if ( tmp['units'] != data['units'] ) : 
            print('Components have different units')
            quit()

#       add the component contribution
        data['field'] = data['field'] + tmp['field'] * wlist[icomp]
#           
#   noemer : division if needed 
    if ( cnoemer != None ) :

        tmp=readsingleh0field.readsingleh0field(expid, cnoemer, date) 

#       data['field'] = np.where( tmp['field'] >= 0., data['field'] / tmp['field'], 0.) 
        data['field'] =  data['field'] / ( tmp['field'] + 1.e-10 ) 

#   check standard writing of units
    data['units'] = getstandardunits.getstandardunits(units=data['units'])

#   conversion to 
    if ( cdim == '3d-plev19' ) : 
        data = convert3dplev19.convert3dplev19(data=data) 

#   check units
    factor = getconversionfactorunits.getconversionfactorunits(origunits=data['units'],finalunits=desiredunits)
    data['field'] = data['field'] * factor
    data['units'] = desiredunits
#
    return data

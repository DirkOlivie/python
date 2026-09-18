import numpy as np
import copy

import sys

import getoxidantcomponents

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readnc
import readattributenc

sys.path.insert(0,'/nird/home/olivie/scripts-python')
import experimentdefinition




def readmeanfieldoxidants(species, expid, period, month):
#------------------------
    '''
    INPUT
        species
        expid
        period
        month

    CALLS
        experimentdefinition.getexpidinfo
        getoxidantcomponents
        readnc

    '''

    line=period.split('-')

    if (len(line) != 2 ) :
        print('+++ readmeanfieldoxidants +++')
        print('Period not in correct yyyy0-yyyy1 format : ', period)
        quit()

    year0=int(line[0])
    year1=int(line[1])

    nyear = year1-year0+1

    expidinfo = experimentdefinition.getexpidinfo(expid=expid)

    camversion='cam'
    h0version='h0'

#
    complist, weightlist = getoxidantcomponents.getoxidantcomponents(species=species)
    
    ncomp=len(complist)

#   loop over years
    for iyear in range(0,nyear) :

        for icomp in range(0,ncomp) :
            filename  = expidinfo['subdir']+'/'+expidinfo['cdir']+'/atm/hist/'+expidinfo['cexpid']+'.'+camversion+'.'+h0version+'.'+str("%4.4i"% (expidinfo['year1']))+'-'+str("%2.2i"% (month))+'.nc'

            tmp = np.squeeze(readnc.readnc(complist[icomp], filename)) # remove the time dimension of size 1

            if ( iyear == 0 and icomp == 0) : field =         copy.deepcopy(tmp) / float(nyear) * weightlist[icomp]
            else                            : field = field +               tmp  / float(nyear) * weightlist[icomp]
#
            units = readattributenc.readattributenc(complist[icomp], filename, 'units')

    data = { 'field' : field, \
             'units' : units}

#   return
    return data

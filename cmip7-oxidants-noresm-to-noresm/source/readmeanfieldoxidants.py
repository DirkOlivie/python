import numpy as np
import copy

import sys

import getoxidantcomponents

sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readnc
import readattributenc

sys.path.insert(0,'/nird/home/olivie/code/python/cartopy/source')
import readsingleh0field

sys.path.insert(0,'/nird/home/olivie/scripts-python')
import experimentdefinition




def readmeanfieldoxidants(species, expid, period, month):
#------------------------
    '''
    MODIFICATIONS
        (2026-10-20) : use readsingleh0field.åy

    ERROR
        I was always reading the year1 (from the experiment) !!!!!

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

#   actually not needed
#   expidinfo = experimentdefinition.getexpidinfo(expid=expid)

    camversion='cam'
    h0version='h0'

#
    complist, weightlist = getoxidantcomponents.getoxidantcomponents(species=species)
    
    ncomp=len(complist)

#   loop over years
    for iyear in range(0,nyear) :

        year = year0 + iyear

        for icomp in range(0,ncomp) :
#
#            filename  = expidinfo['subdir']+'/'+expidinfo['cdir']+'/atm/hist/'+expidinfo['cexpid']+'.'+camversion+'.'+h0version+'.'+str("%4.4i"% (expidinfo['year1']))+'-'+str("%2.2i"% (month))+'.nc'
#            tmp = np.squeeze(readnc.readnc(complist[icomp], filename)) # remove the time dimension of size 1
#            units = readattributenc.readattributenc(complist[icomp], filename, 'units')

#           data  = readsingleh0field.readsingleh0field(expid=expid, var=complist[icomp], date=str("%4.4i"% (expidinfo['year1']))+'-'+str("%2.2i"% (month)))
            data  = readsingleh0field.readsingleh0field(expid=expid, var=complist[icomp], date=str("%4.4i"% (year))+'-'+str("%2.2i"% (month)))
            units = data['units']
            tmp   = data['field']

            if ( iyear == 0 and icomp == 0) : field =         copy.deepcopy(tmp) / float(nyear) * weightlist[icomp]
            else                            : field = field +               tmp  / float(nyear) * weightlist[icomp]
#

    avgdata = { 'field' : field, \
                'units' : units}

#   return
    return avgdata

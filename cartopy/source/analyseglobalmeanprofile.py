import copy

import readmeanglobalmeanprofile
import plotglobalmeanprofile

def analyseglobalmeanprofile (expidlist, refidlist, refid2list, refid3list, wlist, wNRlist, legendlist, varlist, year0list, year1list, refyear0list, refyear1list, seasonlist, regionlist, verticalaxis, figlayoutlist, code, colorlist, linestylelist) :
#---------------------------
#
# MODIFICATIONS
#   (2023-04-14) adding refidlist and wlist
#   (2025) possibility for wNRlist (for fractions, percentages, ...)
#   (2026-04-22) adding refyear0list, refyear1list
#
#---------------------------------------------------------------------------------------
#
    print('+++ analyseglobalmeanprofile +++')

    print(expidlist)
    print(legendlist)
    print(varlist)
    print(year0list)
    print(year1list)
    print(refyear0list)
    print(refyear1list)
    print(seasonlist)
    print(regionlist)
#
# read all the data (loop over experiments)
    nexpid = len(expidlist)
    datalist=[]

    for iexpid in range(0,nexpid) :

#       CHECK WHETHER HAVE TO BE READ
        doexp  = False
        doref  = False
        doref2 = False
        doref3 = False

        if ( expidlist  != None and wlist[0] != 0. and expidlist[ iexpid] != '' ) : doexp  = True
        if ( refidlist  != None and wlist[1] != 0. and refidlist[ iexpid] != '' ) : doref  = True
        if ( refid2list != None and wlist[2] != 0. and refid2list[iexpid] != '' ) : doref2 = True
        if ( refid3list != None and wlist[3] != 0. and refid3list[iexpid] != '' ) : doref3 = True
        
#       READ ALL POSSIBLE CONTRIBUTIONS
        if ( doexp  ) : expdata  = readmeanglobalmeanprofile.readmeanglobalmeanprofile(expid=expidlist[iexpid],  var=varlist[iexpid], year0=year0list[iexpid],    year1=year1list[iexpid], season=seasonlist[iexpid], region=regionlist[iexpid],verticalaxis=verticalaxis)
        if ( doref  ) : refdata  = readmeanglobalmeanprofile.readmeanglobalmeanprofile(expid=refidlist[iexpid],  var=varlist[iexpid], year0=refyear0list[iexpid], year1=refyear1list[iexpid], season=seasonlist[iexpid], region=regionlist[iexpid],verticalaxis=verticalaxis)
        if ( doref2 ) : ref2data = readmeanglobalmeanprofile.readmeanglobalmeanprofile(expid=refid2list[iexpid], var=varlist[iexpid], year0=year0list[iexpid],    year1=year1list[iexpid], season=seasonlist[iexpid], region=regionlist[iexpid],verticalaxis=verticalaxis)   # year0, year1 assumed valid
        if ( doref3 ) : ref3data = readmeanglobalmeanprofile.readmeanglobalmeanprofile(expid=refid3list[iexpid], var=varlist[iexpid], year0=year0list[iexpid],    year1=year1list[iexpid], season=seasonlist[iexpid], region=regionlist[iexpid],verticalaxis=verticalaxis)   # year0, year1 assumed valid
#
#       SUM UP TELLER 
        dataTeller = copy.deepcopy(expdata)
        dataTeller['valuelist'][:] = 0.   # initialize to 0
        if ( doexp  ) : dataTeller['valuelist'] =    dataTeller['valuelist'] +  expdata[ 'valuelist'] * wlist[0]
        if ( doref  ) : dataTeller['valuelist'] =    dataTeller['valuelist'] +  refdata[ 'valuelist'] * wlist[1]
        if ( doref2 ) : dataTeller['valuelist'] =    dataTeller['valuelist'] +  ref2data['valuelist'] * wlist[2]
        if ( doref3 ) : dataTeller['valuelist'] =    dataTeller['valuelist'] +  ref3data['valuelist'] * wlist[3]
#
#       NOEMER
        if ( wNRlist != None) : 

#       CHECK WHETHER HAVE TO BE READ
            doexp  = False
            doref  = False
            doref2 = False
            doref3 = False

            if ( expidlist  != None and wNRlist[0] != 0. and expidlist[ iexpid] != '' ) : doexp  = True
            if ( refidlist  != None and wNRlist[1] != 0. and refidlist[ iexpid] != '' ) : doref  = True
            if ( refid2list != None and wNRlist[2] != 0. and refid2list[iexpid] != '' ) : doref2 = True
            if ( refid3list != None and wNRlist[3] != 0. and refid3list[iexpid] != '' ) : doref3 = True

#           SUM UP TELLER 
            dataNoemer = copy.deepcopy(dataTeller)
            dataNoemer['valuelist'][:] = 0.   # intialize to 0
            if ( doexp  ) : dataNoemer['valuelist'] =    dataNoemer['valuelist'] +  expdata[ 'valuelist'] * wNRlist[0]
            if ( doref  ) : dataNoemer['valuelist'] =    dataNoemer['valuelist'] +  refdata[ 'valuelist'] * wNRlist[1]
            if ( doref2 ) : dataNoemer['valuelist'] =    dataNoemer['valuelist'] +  ref2data['valuelist'] * wNRlist[2]
            if ( doref3 ) : dataNoemer['valuelist'] =    dataNoemer['valuelist'] +  ref3data['valuelist'] * wNRlist[3]
#
#           DO DIVISION
            dataTeller['valuelist'] = dataTeller['valuelist'] / dataNoemer['valuelist'] * 100.
            dataTeller['units'] = '%'

        datalist.append(dataTeller)

# plot the zonal mean
    for figlayout in figlayoutlist :
        plotglobalmeanprofile.plotglobalmeanprofile(datalist=datalist, legendlist=legendlist, wlist=wlist, figlayout=figlayout, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
    print('--- analyseglobalmeanprofile ---')

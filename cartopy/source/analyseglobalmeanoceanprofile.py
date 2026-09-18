import readmeanglobalmeanoceanprofile
import plotglobalmeanoceanprofile

def analyseglobalmeanoceanprofile (expidlist, refidlist, wlist, legendlist, varlist, expyear0list, expyear1list, refyear0list, refyear1list, seasonlist, regionlist, verticalaxis, figlayoutlist, code, colorlist, linestylelist) :
#---------------------------
#
# MODIFICATIONS



    print('+++ analyseglobalmeanprofile +++')

    print(expidlist)
    print(legendlist)
    print(varlist)
    print(expyear0list)
    print(expyear1list)
    print(refyear0list)
    print(refyear1list)
    print(seasonlist)
    print(regionlist)
#
# read all the data (loop over experiments)
    nexpid = len(expidlist)
    datalist=[]

    for iexpid in range(0,nexpid) :
        expid=expidlist[iexpid]
        refid=refidlist[iexpid]

#       read experiment
        data = readmeanglobalmeanoceanprofile.readmeanglobalmeanoceanprofile(expid=expid, var=varlist[iexpid], year0=expyear0list[iexpid], year1=expyear1list[iexpid], season=seasonlist[iexpid], region=regionlist[iexpid],verticalaxis=verticalaxis)
        data['valuelist'] =    data['valuelist'] * wlist[0]


#       read ref
        if ( wlist[1] != 0. ) :
            refdata = readmeanglobalmeanoceanprofile.readmeanglobalmeanoceanprofile(expid=refid, var=varlist[iexpid], year0=refyear0list[iexpid], year1=refyear1list[iexpid], season=seasonlist[iexpid], region=regionlist[iexpid],verticalaxis=verticalaxis)

            data['valuelist'] =    data['valuelist'] \
                             + refdata['valuelist'] * wlist[1]

#       append additional experiment
        datalist.append(data)

# plot the zonal mean
    for figlayout in figlayoutlist :
        plotglobalmeanoceanprofile.plotglobalmeanoceanprofile(datalist=datalist, legendlist=legendlist, wlist=wlist, figlayout=figlayout, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
    print('--- analyseglobalmeanprofile ---')

#import readmodelprofile
import readshadozprofile
import statshadozprofile
import plotshadozprofile
import readmodelprofile
import statmodelprofile

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/cartopy-cmorized/source')
import experimentdefinition

def analyseshadozprofile (expidlist, legendlist, var, station, year0list, year1list, season, verticalaxis, figlayout, code) :
#-----------------------
    '''
    INPUT
        expidlist
        legendlist
        var : 'ozone'
        station
        year0list
        year1list
        season
        verticalaxis : 'height' | 'pressure'
        figlayout
        code

    CALLS
        readshadozprofile
        statshadozprofile
        experimentdefinition
        readmodelprofile    
        statmodelprofile
        plotshadozprofile

    MODIFICATIONS
        (2024-02-20) adding refidlist and wlist
    '''
#-------------------------------------------------
#
    print('+++ analyseshadozprofile +++')
#
# 0. variables to read from observations and models
#--------------------------------------------------
#   allowed variables
    if ( var == 'ozone' ) :
        yvar_obs  ='O3_mPa'
        yvar_model='O3_as_partpress'
        yunits_standard='mPa'
    else : 
        print('No variable recognized : '+variable)
        quit()   
 
#   allowed vertical coordinates
    if ( verticalaxis == 'height' ) :
        xvar_obs='GeopAlt' 
        xvar_model='height'
        xunits_standard='km'
    elif ( verticalaxis == 'pressure' ) :
        xvar_obs='Press'
        xvar_model='pressure'
        xunits_standard='?'
    else :
        print('No vertical coordinate recognized : '+verticalaxis)
        quit()

# I.a read the observational data 
#------------------------------------------------------------------------
    obsdata=readshadozprofile.readshadozprofile(station=station, season=season, xvar=xvar_obs, yvar=yvar_obs)


#    statistics to observational data (mean, median, min, max, q25, q75)
#------------------------------------------------------------------------
    obsdata=statshadozprofile.statshadozprofile(D=obsdata) # contains {'xvar': 'Press', 'xunit': 'hPa', 'xlist' : ..., 'xbndlist' : ...
                                                           #           'yvar': 'O3_mPa', 'yunit': 'mPa', 'ymean' : ..., 'ymin' : ....}

    xlat=obsdata['latitude']
    xlon=obsdata['longitude']


# II. read all the model data (loop over experiments)
#------------------------------------------------------------------------
    nexpid = len(expidlist)
    modeldatalist=[]

    for iexpid in range(0,nexpid) :
        expid=expidlist[iexpid]
#
        expidinfo=experimentdefinition.getexpidinfo(expid=expid)
        dataformat=expidinfo['dataformat']
#
#       read all months that satisfy
        if ( expid == 'NHISTfrc2_f09_tn14_20191025') : yvar_model_local='ozone_as_partpress'
        elif ( dataformat == 'rawnoresm' )           : yvar_model_local= 'O3_as_partpress'
        elif ( dataformat == 'cmorized' )            : yvar_model_local= 'o3_as_partpress'
        else : 
            print('No expid or dataformat recognized : ...')
            quit()

        tmp = readmodelprofile.readmodelprofile(expid=expid, var=yvar_model_local, year0=year0list[iexpid], year1=year1list[iexpid], season=season, xlon=xlon, xlat=xlat, verticalaxis=xvar_model)

#       calculate statistics (mean, median, ...)
        tmp = statmodelprofile.statmodelprofile(D=tmp) # contains : 'xvar': 'pressure', 'xunit': 'Pa', 'xlist': ...
                                                       #            'yvar': 'o3_as_partpress', 'yunit': 'Pa', 'ymean': ..., 'ymax' : ..., ...                         

        modeldatalist.append(tmp)
#
    print('MODEL X-VALUES')
    print(modeldatalist[0]['xlist'])

    print(obsdata['xunit'])
    print(obsdata['yunit'])
    print(modeldatalist[0]['xunit'])
    print(modeldatalist[0]['yunit'])

# III. bring to same units
#--------------------------------------------------
#   scale x variable (height)    
    if ( obsdata['xunit'] != modeldatalist[0]['xunit'] ) :
        if (   obsdata['xunit'] == 'hPa' and modeldatalist[0]['xunit'] == 'Pa' ) : factor = 0.01
        elif ( obsdata['xunit'] == 'km'  and modeldatalist[0]['xunit'] == 'm'  ) : factor = 0.001
        else :
            print('+++ analyseshadozprofile +++')
            print('No coversion between units : ', obsdata['xunit'], modeldatalist[0]['xunit'])
            quit()

        for i in range(len(modeldatalist)) :
                modeldatalist[i]['xlist'][:] = modeldatalist[i]['xlist'][:] * factor
                modeldatalist[i]['xunit']    = obsdata['xunit']
#
#   scale actual y variable
    if ( obsdata['yunit'] != modeldatalist[0]['yunit'] ) :
        if ( obsdata['yunit'] == 'mPa' and modeldatalist[0]['yunit'] == 'Pa' ) : factor = 1000.
        else :
            print('+++ analyseshadozprofile +++')
            print('No coversion between units : ', obsdata['yunit'], modeldatalist[0]['yunit'])
            quit()

        for i in range(len(modeldatalist)) :
                modeldatalist[i]['ymean'  ][:] = modeldatalist[i]['ymean'  ][:] * factor
                modeldatalist[i]['ymin'   ][:] = modeldatalist[i]['ymin'   ][:] * factor
                modeldatalist[i]['ymax'   ][:] = modeldatalist[i]['ymax'   ][:] * factor
                modeldatalist[i]['ymedian'][:] = modeldatalist[i]['ymedian'][:] * factor
                modeldatalist[i]['yq25'   ][:] = modeldatalist[i]['yq25'   ][:] * factor
                modeldatalist[i]['yq75'   ][:] = modeldatalist[i]['yq75'   ][:] * factor
                modeldatalist[i]['yunit'  ]    = obsdata['yunit']


# IV. plot the data
#-----------------------------------------------------------------------

    plotshadozprofile.plotshadozprofile(var=var, season=season, station=station, modeldatalist=modeldatalist, legendlist=legendlist, obsdata=obsdata, figlayout=figlayout, code=code, verticalaxis=verticalaxis)
#
    print('--- analyseshadozprofile ---')

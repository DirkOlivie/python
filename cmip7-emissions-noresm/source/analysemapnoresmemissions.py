import constructmapnoresmemissions

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/cartopy/source')
import plotmap

def analysemapnoresmemissions(directory, filename, period, figlayoutlist, code):
#-------------------------------
    '''
    INPUT
        directory
        filename
        freqtype

    CALLED BY
        analysemapnoresmemissions

    CALLS
        constructmapnoresmemissions

    '''

#=============================
#
# 1. read 3D/4D data
#-------------------
#
    Dlist = constructmapnoresmemissions.constructmapnoresmemissions(filename=directory+'/'+filename+'.nc', period=period)

# 2. plot maps
#======================= 
#
    line=period.split('-')
    year0=int(line[0])      # conversion string -> integer
    year1=int(line[1])      # conversion string -> integer 
    season=line[2]

    for D in Dlist :
        for figlayout in figlayoutlist :

            plotmap.plotmap(expid     = filename, \
                            refid     = filename, \
                            wlist     = [1.,0.], \
                            var       = 'emiss_'+D['species'], \
                            year0     = year0, \
                            year1     = year1, \
                            season    = season, \
                            expdata   = D, \
                            refdata   = D, \
                            figlayout = figlayout, \
                            code      = code)



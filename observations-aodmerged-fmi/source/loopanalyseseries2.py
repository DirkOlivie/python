import numpy as np

import analyseseries

def loopanalyseseries2 (expidlist, refidlist, xdifflist, regionlist, varlist, year0, year1, plottypelist, description, code, figlayout, colorlist=None, linestylelist=None, legendlist=None, dolegendlist=None):
#----------------------
    '''
    INPUTDATA
        description [optional] : regioncommon | ...

    CALLED BY 
        loopanalyseseries

    CALLS
        analyseseries      
    '''
#
    print('+++ loopanalyseseries2 +++')

    nexpid=len(expidlist)
    nrefid=len(refidlist)
    nregion=len(regionlist)
    nvar=len(varlist)
    ndiff=len(xdifflist)
#
    print('here')
#
    if ( colorlist == None )    : colorlist=np.arange(0,nexpid)            # [0, 1, 2, 3, 4, 5, ...]
    if ( linestylelist == None) : linestylelist=np.zeros(nexpid,dtype=int) # [0, 0, 0, 0, 0, 0, ...]
    if ( legendlist == None )   : legendlist=expidlist                    
    if ( dolegendlist == None ) : dolegendlist=np.zeros(nexpid,dtype=int)  # [1, 1, 1, 1, 1, 1, ...]
#
    print('here 2')
#
    ncolor=len(colorlist)
    nlinestyle=len(linestylelist)
    nlegend=len(legendlist)
    ndolegend=len(dolegendlist)
    ncolor=len(colorlist)
    nlinestyle=len(linestylelist)
    nlegend=len(legendlist)
    ndolegend=len(dolegendlist)
#
    print('here 3')
#
    if ( nexpid != nrefid \
      or nexpid != nregion \
      or nexpid != nvar \
      or nexpid != ncolor \
      or nexpid != nlinestyle \
      or nexpid != nlegend \
      or nexpid != ndolegend ) :
        print('nexpid      : ', nexpid)
        print('nrefid      : ', nrefid)
        print('nregion     : ', nregion)
        print('nvar        : ', nvar)
        print('ncolor      : ', ncolor)
        print('nlinestyle  : ', nlinestyle)
        print('nlegend     : ', nlegend)
        print('ndolegend   : ', ndolegend)
        quit()
#  
    print('here 4')
#
    for xdiff in xdifflist : 
        analyseseries.analyseseries(expidlist=expidlist, refidlist=refidlist, xdiff=xdiff, regionlist=regionlist, varlist=varlist, year0=year0, year1=year1, code=code, plottypelist=plottypelist,\
                    colorlist=colorlist, linestylelist=linestylelist, legendlist=legendlist, dolegendlist=dolegendlist, figlayout=figlayout)

    print('--- loopanalyseseries2 ---')

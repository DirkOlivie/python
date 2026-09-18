import plotseriesnoresmemissions

def plotseriesnoresmemissionsloop2(filelist, prefactorlist, legendlist, shiftlist, smoothlist, freqtype, code, figlayout, colorlist=None, linestylelist=None):
#-----------------------------------
#
    '''
    INPUT
        filelist : list of lists : the internal lists have to be added (e.g., BC_air + BC_anthrosurf + BC_anthroprof
        prefactorlist : list of lists


    CALLED BY
        plotseriesnoresmemissionsloop

    CALLS
        plotseriesnoresmemissions

    '''
#   SOME CHECKS
    if ( ( len(filelist) != len(prefactorlist) ) \
      or ( len(filelist) != len(legendlist)    ) \
      or ( len(filelist) != len(shiftlist)     ) \
      or ( len(filelist) != len(smoothlist)    ) ) :
        print('+++ plotseseriesnoresmemissionsloop2 +++')
        print('length filelist      : ', len(filelist)     )
        print('length prefactorlist : ', len(prefactorlist))
        print('length legendlist    : ', len(legendlist)   )
        print('length shiftlist     : ', len(shiftlist)    )
        print('length smoothlist    : ', len(smoothlist)   )
        quit()
#    
    nset = len(filelist)
    for iset in range(nset) :
        if ( len(filelist[iset]) != len(prefactorlist[iset]) ) :
            print('+++ plotseseriesnoresmemissionsloop2 +++')
            print('length filelist      : ', len(filelist[iset])     )
            print('length prefactorlist : ', len(prefactorlist[iset]))
            quit()
#
    if ( colorlist == None ) :
        colorlist=np.arange(nset,dtype=int)
    if ( colorlist == None ) :
        linestylelist=np.zeros(nset,dtype=int)

    if ( ( len(filelist) != len(colorlist) ) \
      or ( len(filelist) != len(linestylelist) ) ) :
        print('length setlist : ', len(setlist))
        print('length colorlist : ', len(colorlist))
        print('length linestylelist : ', len(linestylelist))
        quit()

    plotseriesnoresmemissions.plotseriesnoresmemissions(filelist=filelist, prefactorlist=prefactorlist, legendlist=legendlist, shiftlist=shiftlist, smoothlist=smoothlist, freqtype=freqtype, code=code, figlayout=figlayout, colorlist=colorlist, linestylelist=linestylelist)

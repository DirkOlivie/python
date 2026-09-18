import analysespectrum

def loopanalysespectrum2(setlist, legendlist, shiftlist, smoothlist, code, figlayout, colorlist=None, linestylelist=None):
#-------------------------

#   SOME CHECKS

    if ( ( len(setlist) != len(legendlist) ) \
      or ( len(setlist) != len(shiftlist)  ) \
      or ( len(setlist) != len(smoothlist) ) ) :
        print('length setlist : ', len(setlist))
        print('length legendlist : ', len(legendlist))
        print('length shiftlist : ', len(shiftlist))
        print('length smoothlist : ', len(smoothlist))
        quit()

    nset = len(setlist)
    if ( colorlist == None ) :
        colorlist=np.arange(nset,dtype=int)
    if ( colorlist == None ) :
        linestylelist=np.zeros(nset,dtype=int)

    if ( ( len(setlist) != len(colorlist) ) \
      or ( len(setlist) != len(linestylelist) ) ) :
        print('length setlist : ', len(setlist))
        print('length colorlist : ', len(colorlist))
        print('length linestylelist : ', len(linestylelist))
        quit()

    analysespectrum.analysespectrum(setlist=setlist, legendlist=legendlist, shiftlist=shiftlist, smoothlist=smoothlist, code=code, figlayout=figlayout, colorlist=colorlist, linestylelist=linestylelist)

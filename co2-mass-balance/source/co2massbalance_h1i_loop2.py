import co2massbalance_h1i

def co2massbalance_h1i_loop2(expidlist, speciesgrouplist, legendlist, shiftlist, smoothlist, freqtypelist, code, figlayoutlist, colorlist, linestylelist):
#-----------------------------
#
    '''
    INPUT
        expidlist
        speciesgrouplist
        legendlist
        shiftlist
        smoothlist
        freqtypelist
        code
        figlayoutlist
        colorlist
        linestylelist

    CALLED BY
        co2massbalance_h1i_loop

    CALLS
        co2massbalance_h1i

    '''

    for expid in expidlist :
        for specieslist in speciesgrouplist : 
            if ( len(specieslist) != len(shiftlist) \
              or len(specieslist) != len(smoothlist) \
              or len(specieslist) != len(colorlist) \
              or len(specieslist) != len(linestylelist) ) :
                print('+++ co2massimbalance_h1i_loop2 +++')
                print('specieslist  : ', len(specieslist))
                print('shiftlist    : ', len(shiftlist))
                print('smoothlist   : ', len(smoothlist))
                print('colorlist    : ', len(colorlist))
                print('linestyllist : ', len(linestylelist))
                quit()

            co2massbalance_h1i.co2massbalance_h1i(expid=expid, specieslist=specieslist, legendlist=legendlist, shiftlist=shiftlist, smoothlist=smoothlist, freqtypelist=freqtypelist, code=code, figlayoutlist=figlayoutlist, colorlist=colorlist, linestylelist=linestylelist)
#
if __name__ == '__main__':
    main()

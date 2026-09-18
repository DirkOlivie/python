import comparenoresmghg

def comparenoresmghgloop2(dir0,file0,dir1,file1,specieslist):
#------------------------------
    '''

    CALLED BY
        comparenoresmghgloop

    CALLS
        comparenoresmghg

    '''

    for species in specieslist :
        comparenoresmghg.comparenoresmghg(filename0=dir0+'/'+file0+'.nc',filename1=dir1+'/'+file1+'.nc',species=species)

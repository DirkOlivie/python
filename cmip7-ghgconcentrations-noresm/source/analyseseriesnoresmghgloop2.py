import analyseseriesnoresmghg

def analyseseriesnoresmghgloop2(directory,filenamelist,freqtypelist,specieslist):
#------------------------------
    '''

    CALLED BY
        analysenoresmghgloop

    CALLS
        analysenoresmghg

    '''

    for filename in filenamelist :
        for freqtype in freqtypelist :
            analyseseriesnoresmghg.analyseseriesnoresmghg(directory=directory,filename=filename,freqtype=freqtype,specieslist=specieslist)

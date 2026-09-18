import analyseseriesnoresmemissions

def analyseseriesnoresmemissionsloop2(directory,filenamelist,freqtype):
#------------------------------
    '''

    CALLED BY
        analysenoresmemissionsloop

    CALLS
        analysenoresmemissions

    '''

    for filename in filenamelist :
        analyseseriesnoresmemissions.analyseseriesnoresmemissions(directory=directory,filename=filename,freqtype=freqtype)

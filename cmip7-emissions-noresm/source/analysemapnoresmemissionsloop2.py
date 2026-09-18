import analysemapnoresmemissions

def analysemapnoresmemissionsloop2(directory,filenamelist,periodlist,figlayoutlist,code):
#------------------------------
    '''

    CALLED BY
        analysenoresmemissionsloop

    CALLS
        analysenoresmemissions

    '''

    for filename in filenamelist :
        for period in periodlist : 
            analysemapnoresmemissions.analysemapnoresmemissions(directory=directory,filename=filename,period=period,figlayoutlist=figlayoutlist,code=code)

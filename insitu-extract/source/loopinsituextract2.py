import insituextract


def loopinsituextract2(expidlist, variablelist, locationlist):
#---------------------

    for expid in expidlist :
        for variable in variablelist :
            for location in locationlist :
                insituextract.insituextract(expid=expid, variable=variable, location=location)

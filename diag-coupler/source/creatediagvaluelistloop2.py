import creatediagvaluelist

def creatediagvaluelistloop2(expidlist,varlist, componentlist, budgettypelist, freqtypelist):
#---------------------------
    '''


    '''
    for expid in expidlist :
        for component in componentlist :
            for variable in varlist :
                for budgettype in budgettypelist :
                    for freqtype in freqtypelist :

                        creatediagvaluelist.creatediagvaluelist(expid=expid, component=component, variable=variable, budgettype=budgettype, freqtype=freqtype)           



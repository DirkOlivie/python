import getdiagvaluelist
import writediagvaluelist

def creatediagvaluelist(expid, component, variable, budgettype, freqtype):
#----------------------
    '''


    '''
    data=getdiagvaluelist.getdiagvaluelist(expid=expid, component=component, variable=variable, budgettype=budgettype, freqtype=freqtype)

    writediagvaluelist.writediagvaluelist(expid=expid, component=component, variable=variable, budgettype=budgettype, freqtype=freqtype, data=data)

    


import sys
sys.path.insert(0,'/nird/home/olivie/scripts-python')
import experimentdefinition

def expidlist2attributelist(expidlist, attributetype):
#--------------------------

    n=len(expidlist)

    outputlist=[]

    for expid in expidlist : 

        expidinfo=experimentdefinition.getexpidinfo(expid=expid)

        outputlist.append(expidinfo[attributetype])

    return outputlist

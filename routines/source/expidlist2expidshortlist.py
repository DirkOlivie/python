import sys
sys.path.insert(0,'/nird/home/olivie/scripts-python')
import experimentdefinition

def expidlist2expidshortlist(expidlist):
#---------------------------

    n=len(expidlist)

    expidshortlist=[]

    for expid in expidlist : 

        expidinfo=experimentdefinition.getexpidinfo(expid=expid)

        expidshortlist.append(expidinfo['expidshort'])

    return expidshortlist

import loopanalyseexpdependence2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


generaldescription='varcommon-typevarcommon'
generalcode='n20250205_noresm2.3_cpl'

figlayout=cfiglayout.CFigLayout()


listA=['N1850_f19_tn14_20241127_test01', \
       'N1850_f19_tn14_20241127_test03', 
       'N1850_f19_tn14_20241127_test07', 
       'N1850_f19_tn14_20241127_test08', 
       'N1850_f19_tn14_20241127_test02', 
       'N1850_f19_tn14_20241127_test04'] 
listB=['N1850_f19_tn14_20190621', \
       'N1850_f19_tn14_20190621', \
       'N1850_f19_tn14_20190621', \
       'N1850_f19_tn14_20190621', \
       'N1850_f19_tn14_20190621', \
       'N1850_f19_tn14_20190621']
expyear0list=[1680,1680,1680,1680,1680,1680]
expyear1list=[1699,1699,1699,1699,1699,1699]
refyear0list=[1600,1600,1600,1600,1600,1600]
refyear1list=[1619,1619,1619,1619,1619,1619]
seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA']
xvaluelist=[0.264,0.274,0.276,0.278,0.284,0.294]
xtitle='CLUBB-gamma'
xunits=''



# 1. DIFFERENCE VALUES
#----------------------------------
# x-axis
expidlist=listA
refidlist=listB
wlist=[1.,-1.]
#
# variables
varlist=['tempocn']
typevarlist=['glob']
legendlist=['']
colorlist=[0]
linestylelist=[0]
description=generaldescription
# 
#
code=generalcode+'_diff'
#
loopanalyseexpdependence2.loopanalyseexpdependence2(\
        expidlist=expidlist,refidlist=refidlist, \
        expyear0list=expyear0list,expyear1list=expyear1list,refyear0list=refyear0list,refyear1list=refyear1list,seasonlist=seasonlist, \
        wlist=wlist, \
        varlist=varlist,typevarlist=typevarlist,legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist, \
        xvaluelist=xvaluelist, xtitle=xtitle, xunits=xunits, \
        description=description,code=code,figlayout=figlayout)

# 2. ABSOLUTE VALUES
#----------------------------------
# x-axis
expidlist=listA
refidlist=expidlist
wlist=[1.,0.]
#
# variables
varlist=['FSLNT','SWCF','LWCF','CDNUMC','PRECT']
typevarlist=['glob']
legendlist=['']
colorlist=[0]
linestylelist=[0]
description=generaldescription
# 
#
code=generalcode
#
loopanalyseexpdependence2.loopanalyseexpdependence2(\
        expidlist=expidlist,refidlist=refidlist, \
        expyear0list=expyear0list,expyear1list=expyear1list,refyear0list=refyear0list,refyear1list=refyear1list,seasonlist=seasonlist, \
        wlist=wlist, \
        varlist=varlist,typevarlist=typevarlist,legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist, \
        xvaluelist=xvaluelist, xtitle=xtitle, xunits=xunits, \
        description=description,code=code,figlayout=figlayout)


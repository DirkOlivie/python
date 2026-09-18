import loopanalysedigital2

# MAIN PROGRAM

typevar='glob'
#freqtype='annavg'
freqtype='YEA'
description='varcommon'


# OBTAINING VOLCANIC EMISSION TOTAL
#----------------------------------
#
expidlist=[ \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test02', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test05', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test09', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test08', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test10', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test04', \
           'NFHISTnorpddmsbc_tropstratchem_f19_mg17_20220105_test03']
refidlist=expidlist
wlist=[1.,0.]
xlist=[0.,0.025,0.05,0.1,0.2,0.5,1.]


expyear0list=[1992,1992,1992,1992,1992,1992,1992]
expyear1list=[1992,1992,1992,1992,1992,1992,1992]
expseasonlist=['JUL','JUL','JUL','JUL','JUL','JUL','JUL']
refyear0list=[1992,1992,1992,1992,1992,1992,1992]
refyear1list=[1992,1992,1992,1992,1992,1992,1992]
refseasonlist=['JUL','JUL','JUL','JUL','JUL','JUL','JUL']

legendlist=['0%','2.5%','5%','10%','20%','50%','100%']
code='kclim_volcano'
#
varlist=['VCONC05_columnburden','NCONC05_columnburden','D550_SO4','AOD_VIS','cb_SO4_AC','cb_SO4_A1','cb_SO4_PR']
varlist=[['NMR01_VCONC01_weightedcolumnburden','NMR01_NCONC01_weightedcolumnburden', \
          'NMR05_VCONC05_weightedcolumnburden','NMR05_NCONC05_weightedcolumnburden'], \
         ['cb_SULFATE','cb_SO4_NA','cb_SO4_PR','cb_SO4_A1','cb_SO4_AC','cb_SO2'], \
         ['VCONC0105_columnburden','VCONC01_columnburden','VCONC05_columnburden']]
#varlist=[['NMR01_VCONC01_weightedcolumnburden','NMR01_NCONC01_weightedcolumnburden','NMR05_VCONC05_weightedcolumnburden','NMR05_NCONC05_weightedcolumnburden']]
#
loopanalysedigital2.loopanalysedigital2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,xlist=xlist, \
                                        expyear0list=expyear0list,
                                        expyear1list=expyear1list,
                                        expseasonlist=expseasonlist,
                                        refyear0list=refyear0list,
                                        refyear1list=refyear1list,
                                        refseasonlist=refseasonlist,                                                                            
                                        legendlist=legendlist,varlist=varlist,typevar=typevar,description=description,code=code)

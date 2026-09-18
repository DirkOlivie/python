import loopanalysezonalmeanline2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
#
def main():
#----------
#
    print('+++ loopanalysezonalmeanline +++')
#
    figlayout=cfiglayout.CFigLayout()
    figlayoutlist=[figlayout]
    horizontalaxislist=['']    
    regionlist=['glob']
#
    description='varcommon'
    code='n20250607_noresm2_erf'
#
    varlist=['FSLNT']

#
# 1. NorESM2
#----------------------------------------------------------------
    expidlist=['NF1850frc2norbc_4xco2_f09_20200108', \
               'NF1850norbc_4xco2_f19_20191025', \
               'NF1850frc2norbc_aer2014_f09_20200108', \
               'NF1850norbc_aer2014_f19_20191025', 
               'NF1850frc2norbc_aeroxid2014_f09_20200108', \
               'NF1850norbc_aeroxid2014_f19_20191025']
    year0list=[ 5, 5, 5, 5, 5, 5]
    year1list=[30,30,30,30,30,30]
    refidlist=['NF1850frc2norbc_f09_20200108', \
               'NF1850norbc_f19_20191025len30', \
               'NF1850frc2norbc_f09_20200108', \
               'NF1850norbc_f19_20191025len30', \
               'NF1850frc2norbc_f09_20200108', \
               'NF1850norbc_f19_20191025len30']
#
    wlist=[1.,-1.]
#    
    seasonlist=['YEA','YEA','YEA','YEA','YEA','YEA']
    linestylelist=[0,2,0,2,0,2]
    colorlist=[0,0,1,1,2,2]
    legendlist=['NorESM2-MM (4xCO2)','NorESM2-LM (4xCO2)','NorESM2-MM (aer)','NorESM2-LM (aer)','NorESM2-MM (aer+oxid)','NorESM2-LM (aer+oxid)']
#
    loopanalysezonalmeanline2.loopanalysezonalmeanline2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, horizontalaxislist=horizontalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)

if __name__ == '__main__':
    main()

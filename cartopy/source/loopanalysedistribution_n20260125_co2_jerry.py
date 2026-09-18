import loopanalysedistribution2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

#
def main():
#----------    
#
    print('+++ loopanalysedistribution +++')
    print('--- loopanalysedistribution ---')
#
    figlayout0=cfiglayout.CFigLayout(code='ylin')
    figlayout1=cfiglayout.CFigLayout(ytype='log',code='ylog')
    figlayoutlist=[figlayout0,figlayout1]

#
#   NorESM2 
    wlist=[1.,0.]
#   expidlist=['n1850esm.ne16pg3_tn4.noresm3_0_beta10_20260120']
    expidlist=['n1850esm.ne16pg3_tn14.noresm3_0_beta03b.BLOMalbAndBrine.2025-10-30'] * 3
    refidlist=expidlist  # reference
#   timedescriptionlist=['251-280-seperate-YEA-seperate']
    timedescriptionlist=['271-330-seperate-YEA-seperate'] * 3
#   timedescriptionlist=['271-330-average-YEA-seperate'] * 3
    varlist=['SFCO2','SFCO2_LND','SFCO2_OCN']
    typevarlist=[''] * 3
    finalresolutionlist=['orig'] * 3

    legendlist=['total','land','ocean']
    distributiontype='histogram'
    code='n20260125_co2_jerry'

    loopanalysedistribution2.loopanalysedistribution2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, varlist=varlist, typevarlist=typevarlist, timedescriptionlist=timedescriptionlist, finalresolutionlist=finalresolutionlist, legendlist=legendlist,distributiontype=distributiontype,figlayoutlist=figlayoutlist,code=code)  
#
if __name__ == '__main__':
    main()

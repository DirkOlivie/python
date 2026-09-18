import loopanalyseglobalmeanprofile2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
#
def main():
#----------
#
    print('+++ loopanalyseglobalmeanprofile +++')
#
    figlayout=cfiglayout.CFigLayout(code='standard', xtype='')
    figlayoutlog=cfiglayout.CFigLayout(code='standard',xtype='log')
#    figlayout20km=cfiglayout.CFigLayout(code='standard',yrange=[0.,20.])
    
#
#   1. prescribed versus online-calculated [global] : CO2
#-----------------------------------------
    code='n20260820_noresm2.5_radclimate_zonalgradient'
    figlayoutlist=[figlayout,figlayoutlog]
#   expidlist=['n1850Gaxg.n30b23LM.498.20260815.diagrad.r1446.latlon']*36
    expidlist=['n1850Gaxg.n30b23LM.498.20260815.diagrad.r1446.latlon.co2corr']*36
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[1446]*36
    year1list=[1447]*36
    seasonlist=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC', \
                'JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC', \
                'JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    linestylelist=[0,0,0,0,0,0,0,0,0,0,0,0, \
                   1,1,1,1,1,1,1,1,1,1,1,1, \
                   2,2,2,2,2,2,2,2,2,2,2,2]
    colorlist    =[0,1,2,3,4,5,6,7,8,9,10,11, \
                   0,1,2,3,4,5,6,7,8,9,10,11,
                   0,1,2,3,4,5,6,7,8,9,10,11]
    legendlist=['NH','','','','','','','','','','','', \
                '28S28N','','','','','','','','','','','', \
                'SH','','','','','','','','','','','']
    regionlist=['NH']*12+['28S28N']*12+['SH']*12
    verticalaxislist=['height']
#
    description='varcommon'
#
    varlist=['m_CO2_c_as_vmr_drytest','m_CH4_c_as_vmr_drytest','m_N2O_c_as_vmr_drytest']
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#


if __name__ == '__main__':
    main()

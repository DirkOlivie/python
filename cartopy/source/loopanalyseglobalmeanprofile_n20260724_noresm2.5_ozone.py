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
    figlayout=cfiglayout.CFigLayout(code='standard', xtype='',csvoutput=True)
    figlayoutlog=cfiglayout.CFigLayout(code='standard',xtype='log',csvoutput=True)
#    figlayout20km=cfiglayout.CFigLayout(code='standard',yrange=[0.,20.])
    
#
#   1. prescribed versus online-calculated [global]
#-----------------------------------------
    code='n20260724_noresm2.5_ozone'
    figlayoutlist=[figlayout,figlayoutlog]
    expidlist=['nhist.ne16pg3_tn14.pr-noresm3_0_beta19.Base_i446F.Olivia.2026-06-07.radclimate.r2000', \
               'nhist.ne16pg3_tn14.pr-noresm3_0_beta19.Base_i446F.Olivia.2026-06-07.radclimate.r2000.o3clim', \
               'nhist.ne16pg3_tn14.pr-noresm3_0_beta19.Base_i446F.Olivia.2026-06-07.radclimate.r2000.o3clim']
#
    refidlist=expidlist
    wlist=[1.,0.]
#    
    year0list=[2000,2000,2000]
    year1list=[2000,2000,2000]
#   year1list=[2001,2001,2001]
#   seasonlist=['YEA','YEA','YEA']
    seasonlist=['JAN','JAN','JAN']
    linestylelist=[0,0,0]
    colorlist    =[0,1,2]
    legendlist=['CESM3-derived', \
                'input4MIPs-derived', \
                'input4MIPs-derived']
    regionlist=['glob']
    verticalaxislist=['height']
#
    description='regioncommon'
#
    varlist=['m_ozone_c_as_vmr_drytest','m_ozone_c_as_vmr_drytest','ozone']
#    varlist=['T','T','T']
#
    loopanalyseglobalmeanprofile2.loopanalyseglobalmeanprofile2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, verticalaxislist=verticalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist)
#
if __name__ == '__main__':
    main()

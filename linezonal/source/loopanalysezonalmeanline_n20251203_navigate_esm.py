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
    code='n20251203_navigate_esm'
#
# 1.a 1850-1949 : 'FSLNT','TREFHT','PRECT'
#----------------------------------------------------------------
    varlist=['FSLNT','TREFHT','PRECT','FSNT','FLNT']

    expidlist=[ \
#               'N1850frc2esm_ZECMIP_B3_123_f19_tn14_20200316', \
#               'N1850frc2esm_ZECMIP_B3_f19_tn14_20200316', \
#               'N1850frc2esm_ZECMIP_B3_02_f19_tn14_20210224', \
#               'N1850frc2esm_ZECMIP_B3_03_f19_tn14_20210224', \
                \
#               'N1850frc2esm_ZECMIP_B4_123_f19_tn14_20200316', \
#               'N1850frc2esm_ZECMIP_B4_f19_tn14_20200316', \
#               'N1850frc2esm_ZECMIP_B4_02_f19_tn14_20210224', \
#               'N1850frc2esm_ZECMIP_B4_03_f19_tn14_20210224', \
                \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_123_f19_tn14_20250721', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_f19_tn14_20250721', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_02_f19_tn14_20250721', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_03_f19_tn14_20250721', \
                \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens123', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens01', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens02', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens03', \
                \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens123', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens01', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens02', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens03']
#
#    refidlist=['N1850frc2esm_ZECMIP_B3_123_f19_tn14_20200316']*12
    refidlist = ['N1850_f19_tn14_20190730esm']*12
#
    wlist=[1.,-1.]
#    
    seasonlist=['YEA']*12
    linestylelist=[0]*12
    linewidthlist=[2,0.1,0.1,0.1, \
                   2,0.1,0.1,0.1, \
                   2,0.1,0.1,0.1]
    colorlist=[3,3,3,3,2,2,2,2,0,0,0,0]
    legendlist=['2000Pg+CDR+SAI(TR)','','','', \
                '2000Pg+CDR+SAI(NH)','','','', \
                '2000Pg+CDR+SAI(SH)','','','']
#
    year0list=[1910]*12
    year1list=[1929]*12
#
    loopanalysezonalmeanline2.loopanalysezonalmeanline2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, horizontalaxislist=horizontalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist, linewidthlist=linewidthlist)

#
    year0list=[1930]*12
    year1list=[1949]*12
#
    loopanalysezonalmeanline2.loopanalysezonalmeanline2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, horizontalaxislist=horizontalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist, linewidthlist=linewidthlist)


# 1.b 1850-1949 : cb_SULFATE
#----------------------------------------------------------------a
    varlist=['cb_SULFATE']

    expidlist=[ \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_123_f19_tn14_20250721', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_f19_tn14_20250721', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_02_f19_tn14_20250721', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_03_f19_tn14_20250721', \
                \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens123', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens01', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens02', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens03', \
                \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens123', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens02', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens02', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens02']


    refidlist=['N1850_f19_tn14_20190730esm']*12
#
    wlist=[1.,-1.]
#    
    seasonlist=['YEA']*12
    linestylelist=[0]*12
    linewidthlist=[2,0.1,0.1,0.1, \
                   2,0.1,0.1,0.1, \
                   2,0.1,0.1,0.1]
    colorlist=[3,3,3,3,2,2,2,2,0,0,0,0]
    legendlist=['CDR+SAI(TR)','','','', \
                'CDR+SAI(NH)','','','', \
                'CDR+SAI(SH)','','','']
#
    year0list=[1930]*12
    year1list=[1949]*12
    loopanalysezonalmeanline2.loopanalysezonalmeanline2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, horizontalaxislist=horizontalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist, linewidthlist=linewidthlist)


# 2.a 2030-2049/2130-2149/2230-2249 : 'FSLNT','TREFHT','PRECT'
#----------------------------------------------------------------
    varlist=['FSLNT','TREFHT','PRECT']

    expidlist=[
#               'N1850frc2esm_ZECMIP_B3_123_f19_tn14_20200316', \
#               'N1850frc2esm_ZECMIP_B3_f19_tn14_20200316', \
#               'N1850frc2esm_ZECMIP_B3_02_f19_tn14_20210224', \
#               'N1850frc2esm_ZECMIP_B3_03_f19_tn14_20210224', \
                \
#               'N1850frc2esm_ZECMIP_B4_123_f19_tn14_20200316', \
#               'N1850frc2esm_ZECMIP_B4_f19_tn14_20200316', \
#               'N1850frc2esm_ZECMIP_B4_02_f19_tn14_20210224', \
#               'N1850frc2esm_ZECMIP_B4_03_f19_tn14_20210224', \
                \
#               'N1850frc2esm_IMPOSE_C1a_123_f19_tn14_20200316', \
#               'N1850frc2esm_IMPOSE_C1a_f19_tn14_20200316', \
#               'N1850frc2esm_IMPOSE_B3C1a_02_f19_tn14_20210224', \
#               'N1850frc2esm_IMPOSE_B3C1a_03_f19_tn14_20210224', \
                \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_123_f19_tn14_20250730', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_f19_tn14_20250730', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_02_f19_tn14_20250730', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_03_f19_tn14_20250730', \
                \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens123a', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens01a', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens02a', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens03a', \
                \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens123a', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens01a', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens02a', \
               'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens03a']


    refidlist=['N1850frc2esm_IMPOSE_C1a_123_f19_tn14_20200316']*12
    refidlist=['N1850_f19_tn14_20190730esm']*12
#
    wlist=[1.,-1.]
#    
    seasonlist=['YEA']*12
    linestylelist=[0]*12
    linewidthlist=[2,0.3,0.3,0.3,
                   2,0.3,0.3,0.3,
                   2,0.3,0.3,0.3]
    colorlist=[3,3,3,3,2,2,2,2,0,0,0,0]
    legendlist=['CDR+SAI(TR)','','','', \
                'CDR+SAI(NH)','','','', \
                'CDR+SAI(SH)','','','']               
#
    year0list=[2030]*12
    year1list=[2049]*12
    loopanalysezonalmeanline2.loopanalysezonalmeanline2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, horizontalaxislist=horizontalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist, linewidthlist=linewidthlist)
#
    year0list=[2130]*12
    year1list=[2149]*12
    loopanalysezonalmeanline2.loopanalysezonalmeanline2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, horizontalaxislist=horizontalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist, linewidthlist=linewidthlist)
#
    year0list=[2230]*12
    year1list=[2249]*12
#    loopanalysezonalmeanline2.loopanalysezonalmeanline2(expidlist=expidlist, refidlist=refidlist, wlist=wlist, legendlist=legendlist, varlist=varlist, year0list=year0list, year1list=year1list, seasonlist=seasonlist, regionlist=regionlist, horizontalaxislist=horizontalaxislist, figlayoutlist=figlayoutlist, description=description, code=code, colorlist=colorlist, linestylelist=linestylelist, linewidthlist=linewidthlist)
#
if __name__ == '__main__':
    main()

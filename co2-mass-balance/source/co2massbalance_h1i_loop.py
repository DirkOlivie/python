import co2massbalance_h1i_loop2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

def main():
#----------
#
    '''
    AIM
        all experiments are treated seperately
        all species end up in the same plot

    CALLS
        co2massbalance_h1i_loop2

    '''

#   figure layout [LINEAR/LOG]
    figlayout0=cfiglayout.CFigLayout(            title='CO2 budget discrepancy')
    figlayout1=cfiglayout.CFigLayout(ytype='log',title='CO2 budget discrepancy')
    figlayoutlist=[figlayout0, figlayout1]
#
    expidlist = ['n1850esm.ne16pg3_tn14.noresm3_0_beta10.SSP534.emisall.20260120b']
#                'nHISTesm.ne16pg3_tn14.noresm3_0_beta11_20260225']
    expidlist = ['nHISTesm.ne16pg3_tn14.noresm3_0_beta11_20260311']
    expidlist = ['nhistesm.ne16pg3_tn14.noresm3_0_beta19.Base_i446F.Olivia.2026-06-09.co2inst.segrid']
    expidlist = ['nhistesm.ne16pg3_tn14.noresm3_0_beta19.Base_i446F.Olivia.2026-06-09.co2inst']
    expidlist = ['nhistesm.ne16pg3_tn14.noresm3_0_beta19.Base_i446F.Olivia.2026-06-09.co2inst.segrid.singpre']
#    expidlist = ['nhistesm.ne16pg3_tn14.noresm3_0_beta19.Base_i446F.Olivia.2026-06-09.co2inst.segrid.singpre.r2000']
#
#   1. all species together
    speciesgrouplist=[['CO2_FFF','CO2_LND','CO2_OCN','CO2'], \
                      ['CO2_FFF_cumulative','CO2_LND_cumulative','CO2_OCN_cumulative','CO2_cumulative']]
    shiftlist  = [0,0,0,0]
    smoothlist = [0,0,0,0]
    colorlist     = [1,2,0,3]
    linestylelist = [0,0,0,0]
    legendlist    = ['CO2_FFF','CO2_LND','CO2_OCN','CO2']
    code         = 'n20260303_co2massbalance_combined_'+expidlist[0]
    freqtypelist = ['monthly','YEA','seasonalcycle']
#
    co2massbalance_h1i_loop2.co2massbalance_h1i_loop2(expidlist=expidlist, speciesgrouplist=speciesgrouplist, legendlist=legendlist, shiftlist=shiftlist, smoothlist=smoothlist, freqtypelist=freqtypelist, code=code, figlayoutlist=figlayoutlist, colorlist=colorlist, linestylelist=linestylelist)
#
#   2. seperately
    speciesgrouplist=[['CO2_FFF'],['CO2_LND'],['CO2_OCN'],['CO2'], \
                      ['CO2_FFF_cumulative'],['CO2_LND_cumulative'],['CO2_OCN_cumulative'],['CO2_cumulative']]
    shiftlist  = [0]
    smoothlist = [0]
    colorlist     = [0]
    linestylelist = [0]
    legendlist    = ['']
    code         = 'n20260303_co2massbalance_individual'+expidlist[0]
    freqtypelist = ['monthly','YEA','seasonalcycle']
#
#    co2massbalance_h1i_loop2.co2massbalance_h1i_loop2(expidlist=expidlist, speciesgrouplist=speciesgrouplist, legendlist=legendlist, shiftlist=shiftlist, smoothlist=smoothlist, freqtypelist=freqtypelist, code=code, figlayoutlist=figlayoutlist, colorlist=colorlist, linestylelist=linestylelist)






if __name__ == '__main__':
    main()

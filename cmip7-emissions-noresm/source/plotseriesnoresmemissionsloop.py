import plotseriesnoresmemissionsloop2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout
#----------



figlayout0=cfiglayout.CFigLayout()
figlayout1=cfiglayout.CFigLayout(xrange=[1840,2030])

# ANTHROPOGENIC
specieslist=['BC_N','OM_NI','SO2']

for species in specieslist :


    filelist=[['globalseries_YEA_emissions_cmip7_noresm3_'+species+'_airALL_vertical_1849-2025_1.9x2.5_CEDS-CMIP-2025-04-18_version20260105', \
               'globalseries_YEA_emissions_cmip7_noresm3_'+species+'_anthroprofENEIND_vertical_1849-2025_1.9x2.5_CEDS-CMIP-2025-04-18_version20260105', \
               'globalseries_YEA_emissions_cmip7_noresm3_'+species+'_anthrosurfAGRTRADOMSOLWSTSHP_surface_1849-2025_1.9x2.5_CEDS-CMIP-2025-04-18_version20260105'], \
#
              ['globalseries_YEA_emissions_cmip6_noresm2_'+species+'_airALL_vertical_1849-2015_1.9x2.5_version20180512', \
               'globalseries_YEA_emissions_cmip6_noresm2_'+species+'_anthroprofALL_vertical_1849-2015_1.9x2.5_version20180512', \
               'globalseries_YEA_emissions_cmip6_noresm2_'+species+'_anthrosurfALL_surface_1849-2015_1.9x2.5_version20180512']]

    if (   species == 'BC_N'  ) : prefactorlist = [[1./0.9,1./0.9,1./0.9], [1./0.9,1./0.9,1./0.9]]
    elif ( species == 'OM_NI' ) : prefactorlist = [[1.4,1.4,1.4],[1.,1.,1.]] 
    elif ( species == 'SO2'   ) : prefactorlist = [[1./0.975,1./0.975,1./0.975],[1./0.975,1./0.975,1./0.975]] 
    else : 
        print('+++ plotseriesnoresmemissionsloop +++')
        print('No species recognized : ', species)
        quit()        

    legendlist=['cmip7','cmip6']

    shiftlist=[0,0]
    smoothlist=[0,0]
    freqtype='YEA'

    colorlist=[0,1]
    linestylelist=[0,0]
    code='n20260218_emissions_anthro_'+species

    plotseriesnoresmemissionsloop2.plotseriesnoresmemissionsloop2(filelist=filelist, prefactorlist=prefactorlist, legendlist=legendlist, shiftlist=shiftlist, smoothlist=smoothlist, freqtype=freqtype, code=code, figlayout=figlayout0, colorlist=colorlist, linestylelist=linestylelist)

# BIOMASS
specieslist=['BC_NI','OM_NI','SO2']

for species in specieslist :

    filelist=[['globalseries_YEA_emissions_cmip7_noresm3_'+species+'_bbAGRIBORFDEFOPEATSAVATEMF_vertical_1849-2025_1.9x2.5_DRES-CMIP-BB4CMIP7-2-0_version20260105'], \
#
              ['globalseries_YEA_emissions_cmip6_noresm2_'+species+'_bbALL_vertical_1849-2015_1.9x2.5_version20180512']]

    if (   species == 'BC_NI' ) : prefactorlist = [[1.], [1.]]
    elif ( species == 'OM_NI' ) : prefactorlist = [[2.6],[1.]]
    elif ( species == 'SO2'   ) : prefactorlist = [[1./0.975],[1./0.975]]
    else :
        print('+++ plotseriesnoresmemissionsloop +++')
        print('No species recognized : ', species)
        quit() 

    legendlist=['cmip7','cmip6']

    shiftlist=[0,0]
    smoothlist=[0,0]
    freqtype='YEA'

    colorlist=[0,1]
    linestylelist=[0,0]
    code='n20260218_emissions_bb_'+species

    plotseriesnoresmemissionsloop2.plotseriesnoresmemissionsloop2(filelist=filelist, prefactorlist=prefactorlist, legendlist=legendlist, shiftlist=shiftlist, smoothlist=smoothlist, freqtype=freqtype, code=code, figlayout=figlayout0, colorlist=colorlist, linestylelist=linestylelist) 
 



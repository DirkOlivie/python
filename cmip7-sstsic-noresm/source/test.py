import numpy as np
import readinput4mipssstsic
import readnoresmsstsic
import getdistribution
import writedistributionlist
import writeminmax

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readnc

dirfinal='/scratch/olivie/noresm-inputdata/atm/cam/sst'

dirorig='/datalake/NS9560K/noresm3/input4mips/cmip7/PCMDI-AMIP-1-1-10'


f0=dirorig+'/siconcbcs_input4MIPs_SSTsAndSeaIce_CMIP_PCMDI-AMIP-1-1-10_gn_187001-202212.nc'  # temperature 260 Mb : siconcbcs [%]
#f0=dirorig+'/siconc_input4MIPs_SSTsAndSeaIce_CMIP_PCMDI-AMIP-1-1-10_gn_187001-202212.nc'  # temperature 260 Mb : siconcbcs [%]
#f0=dirorig+'/tosbcs_input4MIPs_SSTsAndSeaIce_CMIP_PCMDI-AMIP-1-1-10_gn_187001-202212.nc'     # sea-ice 32 Mb : tosbcs

f1=dirfinal+'/sst_input4MIPs_SSTsAndSeaIce_CMIP_PCMDI-AMIP-1-1-10_gn_187001-202212_c20260924.nc' # 1.9 Gb : ice_cov [fraction], ice_cov_prediddle, SST_cpl, SST_cpl_prediddle
#f1=dirfinal+'/sst_input4MIPs_SSTsAndSeaIce_CMIP_PCMDI-AMIP-1-1-10_gn_piclimo_c20260924.nc'


# check that prediddle values in input4MIPs and Marianas are eq
varlist=['SSTbef','SSTaft','SICbef','SICaft']

# historical
for var in varlist :

    fi = readinput4mipssstsic.readinput4mipssstsic(period='187001-202212',var=var,origin='input4mips-cmip7',year0=1880,year1=1880)
    fm = readnoresmsstsic.readnoresmsstsic(period='187001-202212',var=var,origin='input4mips-cmip7',year0=1880,year1=1880)
    writeminmax.writeminmax(datalist=[fi,fm])

    di = getdistribution.getdistribution(D=fi)
    dm = getdistribution.getdistribution(D=fm)
    writedistributionlist.writedistributionlist([di,dm])

quit()

# piclimo
for var in varlist :

    fi = readinput4mipssstsic.readinput4mipssstsic(period='187001-202212',var=var,origin='input4mips-cmip7',year0=1870,year1=1899,makeseasonalcycle=True)
    fm = readnoresmsstsic.readnoresmsstsic(period='piclimo',var=var,origin='input4mips-cmip7')
    writeminmax.writeminmax(datalist=[fi,fm])

    di = getdistribution.getdistribution(D=fi)
    dm = getdistribution.getdistribution(D=fm)
    writedistributionlist.writedistributionlist([di,dm])

# 2000climo
for var in varlist :

    fi = readinput4mipssstsic.readinput4mipssstsic(period='187001-202212',var=var,origin='input4mips-cmip7',year0=1995,year1=2005,makeseasonalcycle=True)
    fm = readnoresmsstsic.readnoresmsstsic(period='2000climo',var=var,origin='input4mips-cmip7')
#    writeminmax.writeminmax(datalist=[fi,fm])

    di = getdistribution.getdistribution(D=fi)
    dm = getdistribution.getdistribution(D=fm)
#    writedistributionlist.writedistributionlist([di,dm])

# 2010climo
for var in varlist :

    fi = readinput4mipssstsic.readinput4mipssstsic(period='187001-202212',var=var,origin='input4mips-cmip7',year0=2005,year1=2015,makeseasonalcycle=True)
    fm = readnoresmsstsic.readnoresmsstsic(period='2010climo',var=var,origin='input4mips-cmip7')
#    writedistributionlist.writedistributionlist([di,dm])

    di = getdistribution.getdistribution(D=fi)
    dm = getdistribution.getdistribution(D=fm)
#    writedistributionlist.writedistributionlist([di,dm])

# NorESM2 piClim
for var in varlist :

    fi = readnoresmsstsic.readnoresmsstsic(period='piclimo',var=var,origin='input4mips-cmip7')                                              # 180x360
    fm = readnoresmsstsic.readnoresmsstsic(period='N1850_f19_tn14_20190621_1751-1780_series_version20190726_clim',var=var,origin='noresm2') #  96x144

    di = getdistribution.getdistribution(D=fi)
    dm = getdistribution.getdistribution(D=fm)
#    writedistributionlist.writedistributionlist([di,dm])

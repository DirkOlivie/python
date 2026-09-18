import math
import numpy as np
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readnc
import getmonthlength

sys.path.insert(0,'/nird/home/olivie/scripts-python')
import areafraction


def co2massbalance_h1i_generate(expid, species):
#------------------------------
    '''
    INPUT
        expid
        species

    CALLED BY
        co2massbalance_h1i_loop

    CALLS
        readnc
        getmonthlength

    '''

    Rearth=6370e3    
    Aearth=Rearth*Rearth * 4. * math.pi
    dir       = '/datalake/NS9560K/noresm3/cases'

#   0.    
    if (   species == 'CO2_cumulative'     ) : origspecies = 'CO2'     ; action='integratetime'
    elif ( species == 'CO2_LND_cumulative' ) : origspecies = 'CO2_LND' ; action='integratetime'
    elif ( species == 'CO2_OCN_cumulative' ) : origspecies = 'CO2_OCN' ; action='integratetime'
    elif ( species == 'CO2_FFF_cumulative' ) : origspecies = 'CO2_FFF' ; action='integratetime'
    else                                     : origspecies = species   ; action=None 


#   1. read the different experiments and calculate budget

    if   ( expid == 'n1850esm.ne16pg3_tn4.noresm3_0_beta10_20260120dix' )                                                : hx='h0i' ; year0 =  251 ; month0 = 2 ; year1 =  260 ; month1 = 12                     
    elif ( expid == 'n1850esm.ne16pg3_tn14.noresm3_0_beta10.SSP534.emisall.20260120b')                                   : hx='h1i' ; year0 = 2015 ; month0 = 2 ; year1 = 2064 ; month1 = 12
    elif ( expid == 'nHISTesm.ne16pg3_tn14.noresm3_0_beta11_20260225')                                                   : hx='h1i' ; year0 = 1850 ; month0 = 2 ; year1 = 1879 ; month1 = 12
    elif ( expid == 'nHISTesm.ne16pg3_tn14.noresm3_0_beta11_20260311')                                                   : hx='h1i' ; year0 = 1880 ; month0 = 2 ; year1 = 1969 ; month1 = 12 ; calendar = 'noleap'
    elif ( expid == 'nhistesm.ne16pg3_tn14.noresm3_0_beta19.Base_i446F.Olivia.2026-06-09.co2inst' )                      : hx='h1i' ; year0 = 1850 ; month0 = 2 ; year1 = 1869 ; month1 = 12 ; calendar = 'noleap' ; grid='latlon-area'
    elif ( expid == 'nhistesm.ne16pg3_tn14.noresm3_0_beta19.Base_i446F.Olivia.2026-06-09.co2inst.segrid' )               : hx='h1i' ; year0 = 1850 ; month0 = 2 ; year1 = 1869 ; month1 = 12 ; calendar = 'noleap' ; grid='segrid'
    elif ( expid == 'nhistesm.ne16pg3_tn14.noresm3_0_beta19.Base_i446F.Olivia.2026-06-09.co2inst.segrid.singpre' )       : hx='h1i' ; year0 = 1850 ; month0 = 2 ; year1 = 2019 ; month1 = 12 ; calendar = 'noleap' ; grid='segrid'
    elif ( expid == 'nhistesm.ne16pg3_tn14.noresm3_0_beta19.Base_i446F.Olivia.2026-06-09.co2inst.segrid.singpre.r2000' ) : hx='h1i' ; year0 = 2000 ; month0 = 2 ; year1 = 2019 ; month1 = 12 ; calendar = 'noleap' ; grid='segrid'
    else : 
        print('+++ co2massbalance_h1i +++')
        print('No expid recognized : ', expid)
        quit()
#   specieslist=['CO2','CO2_LND','CO2_OCN','CO2_FFF']
    year=year0
    month=month0
#
    valuelist=[]
    monthlist=[]
    yearlist=[]
    timelist=[]

#   restarts
    while (year*100 + month <= year1*100+month1 ) :

#       find next month (nextmonth and nextyear)
        if ( month < 12 ) : nextmonth = month + 1 ; nextyear = year 
        else              : nextmonth = 1         ; nextyear = year + 1 

        yyyy = str("%4.4i"% (year))
        mm   = str("%2.2i"% (month))

        nextyyyy = str("%4.4i"% (nextyear))
        nextmm   = str("%2.2i"% (nextmonth))

        date     = yyyy+'-'+mm+'-01-00000'
        nextdate = nextyyyy+'-'+nextmm+'-01-00000'
        period   = yyyy+'-'+mm

#       instantaneous : begin of interval
        filename=dir+'/'+expid+'/atm/hist/'+expid+'.cam.'+hx+'.'+date+'.nc'
        field = np.squeeze(readnc.readnc('TM'+origspecies,filename))
        if ( grid == 'latlon-gw' ) : 
            nlat,nlon = field.shape
            gw= np.squeeze(readnc.readnc('gw',filename))
            area=np.zeros((nlat,nlon),dtype=float)
            for ilon in range(nlon) :
                area[:,ilon] = gw[:]

        elif ( grid == 'latlon-area' ) :
            latitude  = np.squeeze(readnc.readnc('lat',filename))
            longitude = np.squeeze(readnc.readnc('lon',filename))

            area = areafraction.areafraction(latitude=latitude, longitude=longitude)

#           area=np.squeeze(readnc.readnc('GRIDAREA','/datalake/NS9560K/noresm3/cases/nhist.ne16pg3_tn14.noresm3_0_beta01_550dcs_5p0clubbc8_0p75dust.20250716/atm/hist/nhist.ne16pg3_tn14.noresm3_0_beta01_550dcs_5p0clubbc8_0p75dust.20250716.cam.h0a.2014-11.nc'))
#           area=np.squeeze(readnc.readnc('GRIDAREA','/projects/NS9560K/noresm/cases/NHIST_f19_tn14_20190710/atm/hist/NHIST_f19_tn14_20190710.cam.h0.2014-12.nc'))

            area = area/np.sum(area) * math.pi

        else :
            area  = readnc.readnc('area',filename) # fraction of 4pi

        area = area/np.sum(area) * math.pi

        brd0  = np.sum(field[:]*area[:]) * Rearth * Rearth * 1.e-12 # kg -> Pg
#            print('Mass Pg[CO2] : ', date,brd0)

#       instantaneous : end of interval
        filename=dir+'/'+expid+'/atm/hist/'+expid+'.cam.'+hx+'.'+nextdate+'.nc'
        field= np.squeeze(readnc.readnc('TM'+origspecies,filename))
#        area = readnc.readnc('area',filename) # fraction of 4pi  # assume same as above
        brd1 = np.sum(field[:]*area[:]) * Rearth * Rearth *1.e-12 # kg -> Pg
#       print('Mass Pg[CO2] : ', date,brd0)

#       print('Mass change Pg[CO2] : ', brd1-brd0)

#       emissions during month
        filename=dir+'/'+expid+'/atm/hist/'+expid+'.cam.h0a.'+period+'.nc'
        field = np.squeeze(readnc.readnc('SF'+origspecies,filename))
#        area  = readnc.readnc('area',filename) # fraction of 4pi # assume same as above
        monthlength=getmonthlength.getmonthlength(year=year,month=month,calendar=calendar)
        emi = np.sum(field[:]*area[:]) * 86400 * monthlength * Rearth * Rearth * 1e-12 # kg/sec -> Pg/month
            
#       aircraft emissions            
        if ( origspecies == 'CO2' or origspecies == 'CO2_FFF' ) :
             field = np.squeeze(readnc.readnc('ac_CO2',filename))     
#            sum over verical dimension
             field=np.sum(field, axis=0)  
             emi_aircraft = np.sum(field[:]*area[:])*86400*monthlength*Rearth*Rearth*1e-12 # kg -> Pg

             emi = emi + emi_aircraft

#       print('Emission integral Pg[CO2] : ', date,emi)        
        print(origspecies, period, ' Difference Pg[CO2] per 30 years : ', str("%.6f"% ((brd1-brd0-emi)*30*12)))

        valuelist.append((brd1-brd0-emi))
        units='Pg[CO2] per month'
        yearlist.append(year)
        monthlist.append(month)
        timelist.append(year+(month-0.5)/12.)

        year=nextyear
        month=nextmonth
#
#   integrate over time
    ntime=len(timelist)
    if ( action == 'integratetime' ) : 
        for itime in range(1,ntime) :
            valuelist[itime]=valuelist[itime]+valuelist[itime-1]       
        units='Pg[CO2]' 

#       convert list into numpy array
    valuelist = np.array(valuelist)
    yearlist  = np.array(yearlist)
    monthlist = np.array(monthlist)
    timelist  = np.array(timelist)

    print('MEAN : ', np.mean(valuelist))
    print('MAX  : ', np.amax(valuelist))
    print('MIN  : ', np.amin(valuelist))
#
#   RETURN DATA
    newdata = {'expid'     : expid, \
               'variable'  : species, \
               'units'     : units, \
               'fileorigin': '', \
               'area'      : Aearth, \
               'areaglob'  : Aearth, \
               'areaunits' : 'm2', \
               'yearlist'  : yearlist, \
               'monthlist' : monthlist, \
               'timelist'  : timelist, \
               'valuelist' : valuelist, \
               'ntime'     : ntime \
              }
#
#   trim the data
#    newdata = trimseries.trimseries(data=newdata)
#
#   fill statistics
#   newdata = fillstatistics.fillstatistics(data=newdata, freqtype='monthly')

    return newdata

import netCDF4 as nc
import datetime
import numpy as np
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readnc

def main():
#----------
#
    Rearth = 6370e3
#
#   expid = 'n1850esm.ne16pg3_tn4.noresm3_0_beta10_20260120neuf'
#   expid = 'n1850esm.ne16pg3_tn4.noresm3_0_beta10_20260120onze' # year 251
    expid = 'n1850esm.ne16pg3_tn14.noresm3_0_beta10.SSP534.emisall.20260120c'
    dir   = '/datalake/NS9560K/noresm3/cases'

    specieslist = ['CO2','CO2_LND','CO2_OCN','CO2_FFF'] 
    specieslist = ['CO2_LND']


    year0=2015 ; year1=2024
    year0=2025 ; year1=2034
    year0=2035 ; year1=2044
    date0      = datetime.datetime(year0, 1, 1)
    date1      = datetime.datetime(year1,12,31)

#   PROBLEMATIC DAY
#    date0      = datetime.datetime(2016, 6,24)
#    date1      = datetime.datetime(2016, 6,24)
    offset     = '01800'
#   time_units = 'days since 251-01-01 00:00:00'
    time_units = 'days since 2015-01-01 00:00:00'
    calendar   = 'noleap'
    nstep      =  48   # 48 30-minutes timesteps per day    
#   delta      = 3 # hours
#   hx         = 'h1i'
    hx         = 'h2i'

    datelist=[]

    num0=nc.date2num(date0, time_units, calendar=calendar) # begin date -> begin moment
    num1=nc.date2num(date1, time_units, calendar=calendar)     # end date  -> end moment


    ndays=int(num1-num0+1)

    num=num0
    while ( num <= num1 ) :
        
        date=nc.num2date(num, time_units, calendar=calendar)

        cyear  = str("%4.4i"% (date.year))
        cmonth = str("%2.2i"% (date.month))
        cday   = str("%2.2i"% (date.day))        

        datelist.append(cyear+'-'+cmonth+'-'+cday+'-'+offset)
        
        num = num + 1 # add 1 day

    print(datelist)


#    datelist  = [ '0251-01-01-01800' , '0251-01-02-01800' , ... ]
#
#   LOOP OVER ALL SPECIES
    for species in specieslist :
#
        print('*********************')
        print('*** ', species, ' ***')
        print('*********************')
#
        emi_list     = []
        mss_list     = []
        mssdiff_list = []
        moment_list    = []

#       LOOP OVER ALL DAYS OF YEAR
        for date in datelist :
#
            filename = dir+'/'+expid+'/atm/hist/'+expid+'.cam.'+hx+'.'+date+'.nc'
#
            print('*** ', date, ' ***')

            area  = readnc.readnc('area',filename)        # fraction of 4pi
            TMCO2 = readnc.readnc('TM'+species,filename)  # read column burden
            SFCO2 = readnc.readnc('SF'+species,filename)  # read emissions 

            ntime_file, ncol = TMCO2.shape

            emi_tmplist     = np.zeros(ntime_file) # empty array of 48 elements
            mss_tmplist     = np.zeros(ntime_file) # empty array of 48 elements
#            mssdiff_tmplist = np.zeros(ntime_file) # empty array of 48 elements

            if ( nstep != ntime_file ) :
                    
                print('nstep      : ', nstep)
                print('ntime_file : ', ntime_file)

                quit()

#           LOOP OVER 48 TIMESTEPS
            for itime in range(0,ntime_file) :

                emi = np.sum(SFCO2[itime,:]*area[:])*Rearth*Rearth*1800 *1.e-12 # kg -> Pg
                mss = np.sum(TMCO2[itime,:]*area[:])*Rearth*Rearth      *1.e-12 # kg -> Pg 
#                psd = np.sum(PSDRY[itime,:]*area[:])
            
#                mssdiff = ( np.sum(TMCO2[itime,:]*area[:])-np.sum(TMCO2[itime-1,:]*area[:]) ) *Rearth*Rearth * 1.e-12

                emi_tmplist[itime]     = emi
                mss_tmplist[itime]     = mss
#                mssdiff_list[itime] = mssdiff

#
                moment_list.append(date)           
#
#           GLUE 48 TIMESTEPS
            emi_list = np.concatenate((emi_list, emi_tmplist)) # make list longer and longer
            mss_list = np.concatenate((mss_list, mss_tmplist)) # make list longer and longer


#                print(itime, 'Mass change / Emissions accumulation / diff : ', mssdiff*48*365*30, emi*48*365*30, (mssdiff-emi)*48*365*30)

        ntime=len(emi_list)

        mssdiff_list = np.zeros(ntime)
        mssdiff_list[1:ntime] = mss_list[1:ntime]- mss_list[0:ntime-1]

        balance_list = mssdiff_list - emi_list

#       OUTPUT UNITS
        factor = 48*365*30 ; units='Pg[CO2]/(30 yr)'
        factor = 1         ; units='Pg[CO2]'
        
        print('Max  : ', np.amax(np.absolute(mssdiff_list[1:ntime] - emi_list[1:ntime]))*factor, units)   
        print('Mean : ', np.mean(            mssdiff_list[1:ntime] - emi_list[1:ntime] )*factor, units)   

        for itime in range(1,ntime) :
            if ( np.abs((mssdiff_list[itime] - emi_list[itime] )*48*365*30) > 0.01 ) :
#                 or ( itime < 10 ) ) :
                print(moment_list[itime], ' ',itime % 48, ' ', (mssdiff_list[itime] - emi_list[itime] )*factor, \
                                                               (mssdiff_list[itime]                   )*factor, \
                                                               (                    - emi_list[itime] )*factor, \
                                                               units)

#       ORDER SIZE + PRINT 50 LARGEST ONES
        balance_list.sort()
        for i in range(50) :    
            print(balance_list[-1-i])

if __name__ == '__main__':
    main()

import numpy as np
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readnc

def main():
#----------
#
    expid='n1850esm.ne16pg3_tn4.noresm3_0_beta10_20260120'
    dir='/datalake/NS9560K/noresm3/cases'
    year0=251
    year1=280
    nyear=year1-year0+1
    nmonth=12
    hx='h0a'
#
    species='CO2_LND'
    species='CO2_OCN'
    species='CO2_FFF'
#
    for iyear in range(nyear) :
        for imonth in range(nmonth) :
            year=year0+iyear
            month=imonth+1

            date=str("%4.4i"% (year))+'-'+str("%2.2i"% (month))

            filename=dir+'/'+expid+'/atm/hist/'+expid+'.cam.'+hx+'.'+date+'.nc'
#
            area = readnc.readnc('area',filename) # fraction of 4pi
            TMCO2= np.squeeze(readnc.readnc('TM'+species,filename))
            SFCO2= np.squeeze(readnc.readnc('SF'+species,filename))
            PSDRY= np.squeeze(readnc.readnc('PSDRY',filename))

            emi = np.sum(SFCO2[:]*area[:])*1800
            brd = np.sum(TMCO2[:]*area[:])
            psd = np.sum(PSDRY[:]*area[:])
#        brd = np.sum(TMCO2[itime,:]*area[:])-np.sum(TMCO2[itime-1,:]*area[:])

#        print(itime, emi, brd, emi-brd)
            print(date,emi,brd,psd)

#    print(area[-2])
#    print(TMCO2)
#    print

if __name__ == '__main__':
    main()

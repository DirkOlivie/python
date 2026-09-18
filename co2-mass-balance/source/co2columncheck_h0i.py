import numpy as np
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import readnc
import readattributenc
import columnintegrationirregular

def main():
#----------
#
    Rearth=6370e3    

    dir       = '/datalake/NS9560K/noresm3/cases'


#   expid     = 'n1850esm.ne16pg3_tn4.noresm3_0_beta10_20260120dix'               ; hx='h0i' ; year0  = 251 ; month0 = 2 ; year1  = 260  ; month1 = 12
    expid     = 'n1850esm.ne16pg3_tn14.noresm3_0_beta10.SSP534.emisall.20260120b' ; hx='h1i' ; year0  = 2015; month0 = 2 ; year1  = 2064 ; month1 = 12
#
#   files to be used simultaneously
#    datelist  = ['0251-03-01-00000','0251-04-01-00000']
#    datelist2 = ['0251-03']
#
    specieslist=['CO2','CO2_LND','CO2_OCN','CO2_FFF']
#
    for species in specieslist :
        print('*** ',species,' ***')

        year  = year0
        month = month0

        valuelist=[]

#       restarts
        valuelist=[]
        while (year*100 + month <= year1*100+month1 ) :

#           find next month (nextmonth and nextyear)
            if ( month < 12 ) : nextmonth = month + 1 ; nextyear = year 
            else              : nextmonth = 1         ; nextyear = year + 1 

            yyyy = str("%4.4i"% (year))
            mm   = str("%2.2i"% (month))
            date     = yyyy+'-'+mm+'-01-00000'

#           instantaneous : begin of interval
            filename=dir+'/'+expid+'/atm/hist/'+expid+'.cam.'+hx+'.'+date+'.nc'
            area        = readnc.readnc('area',filename) # fraction of 4pi
            column = np.squeeze(readnc.readnc('TM'+species,filename))                    
            field = np.squeeze(readnc.readnc(species,filename))
            
            brd0        = np.sum(column[:]*area[:]) * Rearth * Rearth * 1.e-12 # kg -> Pg
#            print('Mass Pg[CO2] : ', date,brd0)

#            field3d = np.squeeze(readnc.readnc(species,filename))
            units   = readattributenc.readattributenc(species,filename,'units')
            psdry   = np.squeeze(readnc.readnc('PSDRY',filename))
            hyai    = np.squeeze(readnc.readnc('hyai',filename))
            hybi    = np.squeeze(readnc.readnc('hybi',filename))
            hyam    = np.squeeze(readnc.readnc('hyam',filename))
            hybm    = np.squeeze(readnc.readnc('hybm',filename))
            p0      = 1.e5
#
#
            offlinecolumn, newunits=columnintegrationirregular.columnintegrationirregular(var=species, field=field, unit=units, hyai=hyai, hybi=hybi, p0=p0, ps=psdry, ta=field, hyam=hyam, hybm=hybm, limit='', ptrop=None)

#
            brd1        = np.sum(offlinecolumn[:]*area[:]) * Rearth * Rearth * 1.e-12 # kg -> Pg
#            print('Mass Pg[CO2] : ', date,brd1)

            print('Mass Pg[CO2] : ', date, brd0, brd1) 
#            print(column)
#            print(offlinecolumn)



#            print('Emission integral Pg[CO2] : ', date,emi)        
#            print(period, ' Difference Pg[CO2] over 30 years : ', str("%.6f"% ((brd1-brd0-emi)*30*12)))

#            valuelist.append((brd1-brd0-emi)*30*12)

#           find next month (nextmonth and nextyear)
            if ( month < 12 ) : month = month + 1
            else              : month = 1         ; year = year + 1

#       convert list into 1-dim numpy array
        valuelist=np.array(valuelist)

        print('MEAN : ', np.mean(valuelist))
        print('MAX  : ', np.amax(valuelist))
        print('MIN  : ', np.amin(valuelist))


if __name__ == '__main__':
    main()

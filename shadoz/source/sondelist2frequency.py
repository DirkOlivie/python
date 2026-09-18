import numpy as np

def sondelist2frequency(sondelist, year0=1998, year1=2023):
#----------------------
    '''
    MODIFICATIONS
        (2024-03-05)

    INPUT
        list of sondes        

    RETURN
        
    '''

    nyear=year1-year0+1
    nmonth=12

    ntime=nyear*nmonth

#   empty
    yearlist       =np.zeros(ntime,dtype=int)
    monthlist      =np.zeros(ntime,dtype=int)
    decimalyearlist=np.zeros(ntime,dtype=float)
    frequencylist  =np.zeros(ntime,dtype=int)

#   initialize
    for iyear in range(0,nyear) :
        for imonth in range(0,nmonth) :
            i = iyear*nmonth + imonth
            yearlist[i]        = year0 + iyear
            monthlist[i]       = imonth+1     
            decimalyearlist[i] = float(year0) + float(iyear) + (float(imonth) +0.5) / float(nmonth)

#   loop over sondes
    for sonde in sondelist :

#       split filename
        line=sonde.split('_')   # e.g. costarica_20080611T14_SHADOZV06.dat
                                   #      costarica_20130913T12_SHADOZV06_corr.dat

        timestamp = line[1]     # 20080611T14
        year  = int(timestamp[0:4])
        month = int(timestamp[4:6])
        day   = int(timestamp[6:8])

        mask_year = np.where(yearlist  == year , 1, 0) # where does year agree
        mask_month= np.where(monthlist == month, 1, 0) # where does month agree

        frequencylist = frequencylist + mask_year * mask_month 
     

    data = { 'yearlist'           : yearlist, \
             'monthlist'          : monthlist, \
             'timelist'           : decimalyearlist, \
             'valuelist'          : frequencylist, \
             'representationtype' : 'series_monthly' }

    return data


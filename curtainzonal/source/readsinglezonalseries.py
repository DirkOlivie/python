import re
import numpy as np

import sys
sys.path.insert(0,'/nird/home/olivie/scripts-python')
import experimentdefinition

def readsinglezonalseries (expid=None, variable=None, typevar=None, year0=None, year1=None) :
#------------------------
    '''
    MODIFICATIONS
	(2022-01-16) : creation
        (2022-01-31) : will only read bewteen year0 and year1
    '''

#   synonymes for variables   
    expidinfo=experimentdefinition.getexpidinfo(expid=expid)
    chem=expidinfo['chem']
    globdatadir=expidinfo['globdatadir']
    if ( chem == 'fullchem') : 
        if   ( variable == 'SFisoprene')  : cvariable = 'SFISOP'  
        elif ( variable == 'SFmonoterp')  : cvariable = 'SFMTERP'  
        elif ( variable == 'cb_isoprene') : cvariable = 'cb_ISOP'  
        elif ( variable == 'cb_monoterp') : cvariable = 'cb_MTERP'  
        else : cvariable = variable
    elif ( chem == '' ) :
        if ( variable == 'cb_O3' ) : cvariable = 'ozone_columnburden'
        else : cvariable = variable
    else : cvariable='NOTPOSSIBLE'
#
#   empty dat
    nlatmax=200
    ntimemax=500*12  
    valuelist=np.zeros( (ntimemax,nlatmax) )

#   filename
#   filename='/nird/home/olivie/output/'+globdatadir+'-zonal/'+expid+'/'+cvariable+'.'+expid+'.h0.zonav.txt'
    filename='/datalake/NS2345K/olivie/output/'+globdatadir+'-zonal/'+expid+'/'+cvariable+'.'+expid+'.h0.zonav.txt' # 2026-05-23
    print(filename)

    f=open(filename)
   
    region=typevar

    itime=0

    for line in f:
#        print(repr(line))

        if 'VAR=' in line :          # variable
            line=line.split("=")
            cvariable=line[1].strip()
        elif ( 'UNIT=' in line and 'AREAUNIT=' not in line ) : # unit
            line=line.split("=")
            units=line[1].strip()
        elif 'FILEORIGIN=' in line : # fileorigin
            line=line.split("=")
            fileorigin=line[1].strip()
        elif 'NLAT=' in line :       # nlat
            line=line.split("=")         
            nlat=int(line[1].strip())       # removes also leading and trailing blanks
        elif 'AREA=' in line :       # area of various regions
            line=line.split("=")         
            line=line[1].strip()       # removes also leading and trailing blanks
            line=re.sub(' +',' ',line) # reduced blanks to single blanks
            arealist=line.split(" ")
        elif 'LATMID=' in line :         # latitudes of various zones
            line=line.split("=")         
            line=line[1].strip()       # removes also leading and trailing blanks
            line=re.sub(' +',' ',line) # reduced blanks to single blanks
            latitude=line.split(" ")
            if ( nlat != len(latitude) ) : print('NLAT not equal to # elememts in latitude list') ; print(nlat) ; print(len(latitude)) ; quit()
        elif 'NREGION=' in line :       # nlat
            line=line.split("=")
            nregion=float(line[1].strip())       # removes also leading and trailing blanks
        elif 'REGIONLIST=' in line :       # area of various regions
            line=line.split("=")
            line=line[1].strip()       # removes also leading and trailing blanks
            line=re.sub(' +',' ',line) # reduced blanks to single blanks
            regionlist=line.split(" ")
            if ( nregion != len(regionlist) ) : print('NREGION not equal to # elememts in region list') ; quit()
        elif 'AREAglob='     in line : line=line.split("=") ; line=line[1].strip() ; line=re.sub(' +',' ',line) ; areaglob=line.split(" ") 
        elif 'AREALAND='     in line : line=line.split("=") ; line=line[1].strip() ; line=re.sub(' +',' ',line) ; arealand=line.split(" ") 
        elif 'AREASEA='      in line : line=line.split("=") ; line=line[1].strip() ; line=re.sub(' +',' ',line) ; areasea =line.split(" ") 
        elif 'AREAUNIT='     in line : line=line.split("=") ; areaunits=line[1].strip()
        elif 'FRACTIONglob=' in line : line=line.split("=") ; line=line[1].strip() ; line=re.sub(' +',' ',line) ; fractionglob=line.split(" ") 
        elif 'FRACTIONLAND=' in line : line=line.split("=") ; line=line[1].strip() ; line=re.sub(' +',' ',line) ; fractionland=line.split(" ") 
        elif 'FRACTIONSEA='  in line : line=line.split("=") ; line=line[1].strip() ; line=re.sub(' +',' ',line) ; fractionsea =line.split(" ") 
        elif 'YYYY= MM= REGION=' in line :       # nlat
            print('Reading position YYYY MM REGION')
            line=line.strip()       # removes also leading and trailing blanks
            line=re.sub(' +',' ',line) # reduced blanks to single blanks
            contentlist=line.split(" ")   
            iyyyy=contentlist.index('YYYY=')
            imm=contentlist.index('MM=')
            iregion=contentlist.index('REGION=')
        else :
            line=line.strip()       # removes also leading and trailing blanks
            line=re.sub(' +',' ',line) # reduced blanks to single blanks
            content=line.split(" ")

            year=int(content[iyyyy])
            month=int(content[imm])             

            if ( ( content[iregion] == region ) \
             and ( year >= year0 ) \
             and ( year <= year1 ) ) :           
                if ( itime == 0 ) :
                    yyyylist=[year]         # start a list
                    mmlist=[month]          # start a list 
                else :
                    yyyylist.append(year)
                    mmlist.append(month)

                valuelist[itime,0:nlat]=content[3:3+nlat]

                itime=itime+1
#
    f.close()
#
#   zonal weight
    if ( region == 'glob' ) : areafraction=fractionglob ; area=areaglob ; areatotal=areaglob
    elif (region == 'SEA' ) : areafraction=fractionsea  ; area=areasea  ; areatotal=areaglob
    elif (region == 'LAND') : areafraction=fractionland ; area=arealand ; areatotal=areaglob
    else                    : print('no region recognized') ; quit()
#
       
# create a dictionary
    data={'expid'    : expid, \
          'variable' : variable, \
          'units'    : units, \
          'fileorigin' : fileorigin, \
          'areaunits': areaunits, \
          'yearlist' : np.array(yyyylist), \
          'monthlist': np.array(mmlist), \
          'valuelist': np.array(valuelist[0:itime,0:nlat]), \
          'ntime'    : itime, \
          'latitude' : np.array(latitude,dtype=float), \
          'nlat'     : nlat, \
          'area'     : area, \
          'areafraction' : areafraction, \
          'areatotal': areatotal, \
          'region' : region}
         
#
    print(data['units'])
#
    return data

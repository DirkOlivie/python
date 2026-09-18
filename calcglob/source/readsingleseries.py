import re
import numpy as np

import sys
sys.path.insert(0,'/nird/home/olivie/scripts-python')
import experimentdefinition

def readsingleseries (expid=None, variable=None, typevar=None, freqtype=None) :
#-------------------    
    '''
    AIM
        Reading from the ascii-files (containing global and regional means)

    INPUT
        expid
        variable
        typevar
        freqtype

    MODIFICATIONS
	    (2021-04-05) : creation
	    (2022-01-07) : added chemistry scheme
		    MTERP 
        (2025-08-13) : voltr has no 'glob' region
        (2026-05-04) : timeblocks-v2 : home directory to datalake/NS2345K

    '''

    print('+++ readsingleseries +++')
    print('expid : '+expid)
    print('variable : XXX'+variable+'XXX')

    expidinfo=experimentdefinition.getexpidinfo(expid=expid)
    print(expidinfo)
    chem=expidinfo['chem']
    year0=expidinfo['year0']
    year1=expidinfo['year1']
    globdatadir=expidinfo['globdatadir'] 
#
    if ( chem == 'fullchem') : 
        if   ( variable == 'SFisoprene')  : cvariable = 'SFISOP'  
        elif ( variable == 'SFmonoterp')  : cvariable = 'SFMTERP'  
        elif ( variable == 'cb_isoprene') : cvariable = 'cb_ISOP'  
        elif ( variable == 'cb_monoterp') : cvariable = 'cb_MTERP'  
        elif ( variable == 'SO2_CMXF' ) :
            if ( expid == 'FCHIST_f09_f09_mg17_20211217_test01' \
              or expid == 'FCHIST_f19_f19_mg17_20211217_test02' \
              or expid == 'FCHIST_f19_f19_mg17_20211217_test03' ) : cvariable = 'SO2_CLXF'
            else : cvariable = variable    
        else : cvariable = variable
    elif ( chem == '' ) :
        if ( variable == 'cb_O3' ) : cvariable = 'ozone_columnburden'
        else : cvariable = variable    
    else : cvariable='NOTPOSSIBLE'

#   SPAERO : 
    if ( variable == 'FSNT_SP'  or variable == 'FSNTC_SP'
      or variable == 'FSNT_SP2' or variable == 'FSNTCSP2'
      or variable == 'FSNT_SP3' or variable == 'FSNTCSP3') :
#       name of replacement variable        
        if   ( variable == 'FSNT_SP' )  : variable_replacement = 'FSNT' 
        elif ( variable == 'FSNTC_SP' ) : variable_replacement = 'FSNTC'
        elif ( variable == 'FSNT_SP2' ) : variable_replacement = 'FSNT' 
        elif ( variable == 'FSNTCSP2' ) : variable_replacement = 'FSNTC'
        elif ( variable == 'FSNT_SP3' ) : variable_replacement = 'FSNT' 
        elif ( variable == 'FSNTCSP3' ) : variable_replacement = 'FSNTC'
        else : 
            print('+++ readsingleseries +++ : no varible recognized = '+variable)
            quit()
#               
        if ( expid == 'NF1850norbc_f19_20190727len30' \
          or expid == 'NF1850norbc_aer2014_f19_20190727' \
          or expid == 'NF1850frc2norbc_f09_20200108' ) : cvariable=variable_replacement
        else : cvariable = variable

#   SPAERO : CDNUMCmulXCDNC_SP
    if ( variable == 'CDNUMCmulXCDNC_SP' ) :
        variable_replacement='CDNUMC'

        if ( expid == 'NF1850norbc_f19_20190727len30' \
          or expid == 'NF1850norbc_f19_20191025len30' ) : cvariable=variable_replacement
        else : cvariable = variable

#   filename='/nird/home/olivie/output/timeblocks-v2/'+expid+'/'+cvariable+'.'+expid+'.h0.globav.txt'
#   filename='/nird/home/olivie/output/'+globdatadir+'/'+expid+'/'+cvariable+'.'+expid+'.h0.globav.txt'
    filename='/datalake/NS2345K/olivie/output/'+globdatadir+'/'+expid+'/'+cvariable+'.'+expid+'.h0.globav.txt'
    print(filename)

    f=open(filename)
   
    region=typevar

    itime=0

    for line in f:
#   print(repr(line))

        if 'VAR=' in line :          # variable
            line=line.split("=")
            cvariable=line[1].strip()
        elif ( 'UNIT=' in line and 'AREAUNIT=' not in line ) : # unit
            line=line.split("=")
            units=line[1].strip()
        elif 'FILEORIGIN=' in line : # fileorigin
            line=line.split("=")
            fileorigin=line[1].strip()
        elif 'AREA=' in line :       # area of various regions
            line=line.split("=")         
            line=line[1].strip()       # removes also leading and trailing blanks
            line=re.sub(' +',' ',line) # reduced blanks to single blanks
            arealist=line.split(" ")
        elif 'AREAUNIT=' in line :
            line=line.split("=")
            areaunits=line[1].strip()
        elif  'YYYY= MM=' in line :   # reading all the regions
            line=line.strip()       # removes also leading and trailing blanks
            line=re.sub(' +',' ',line) # reduced blanks to single blanks
            contentlist=line.split(" ")   
            iyyyy=contentlist.index('YYYY=')
            imm=contentlist.index('MM=')
            iregion=contentlist.index('VALUE'+region+'=')     # index of region
            if ( variable != 'voltrocn'
             and variable != 'masstrocn' ) :
                iregionglob=contentlist.index('VALUE'+'glob'+'=') # index of 'global'
            else :
                iregionglob=2 # just take first value
        else :
            line=line.strip()       # removes also leading and trailing blanks
            line=re.sub(' +',' ',line) # reduced blanks to single blanks
            content=line.split(" ")

            yyyy=int(content[iyyyy])
            mm=int(content[imm])

            if ( yyyy >= year0 and yyyy <= year1 ) :

                if ( itime == 0 ) :
                    yyyylist=[yyyy]
                    mmlist=[mm]
                    valuelist=[float(content[iregion])]
                else :
                    yyyylist.append(yyyy)
                    mmlist.append(mm)
                    valuelist.append(float(content[iregion]))

                itime=itime+1
#
    f.close()
#
#    print(variable)
#    print(units)
#    print(fileorigin)
#    print(arealist)
#    print(areaunits)
#    print(contentlist)
#    print(content)
#    print(iyyyy)
#    print(imm)
#    print(iregion)
#    print(yyyylist)
#    print(mmlist)
#    print(valuelist)
#
# create a dictionary
    data={'expid'    : expid, \
          'variable' : variable, \
          'units'    : units, \
          'fileorigin' : fileorigin, \
          'area'     : float(arealist[iregion-2]), \
          'areaglob' : float(arealist[iregionglob-2]), \
          'areaunits': areaunits, \
          'yearlist' : np.array(yyyylist), \
          'monthlist': np.array(mmlist), \
          'timelist' : np.array(yyyylist)*1. + ( np.array(mmlist)*1. - 0.5 ) / 12., \
          'valuelist': np.array(valuelist), \
          'ntime'    : itime}
#
    print(data['units'])
#
    return data

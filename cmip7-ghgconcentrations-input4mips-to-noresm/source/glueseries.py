import sys
sys.path.insert(0,'/nird/home/olivie/code/python/cmip7-ghgconcentrations-input4mips/source')
import getemptydata

def glueseries(S0, S1):
#--------------------
    '''
    INPUT
	    S0 : data structure
        S2 : data structure

    RETURN 
        data structure

    CALLS
	    getemptydata (for the new final structure)

    '''
#-----------------------------
#
# 	check units and variable : should be the same
    if ( S0['unit'] != S1['unit'] \
      or S0['name'] != S1['name'] ) :
        print('+++ glueseries +++')
        print('Different names or units : ', S0['unit'], S1['unit'], S0['name'], S1['name'])
        quit()
#
    n0=S0['ntime']
    n1=S1['ntime']
#
#   check continuity
    date0 = S0['timelist'][-1] # last element
    year0 = date0 // 10000     # integer division
    mmdd0 = date0 % 10000      # modulo

    date1 = S1['timelist'][0]  # first element
    year1 = date1 // 10000     # integer division
    mmdd1 = date1 % 10000      # modulo

#   compare years
    if ( ( year0 + 1 ) != year1 ) :
        print('+++ glueseries +++')
        print('Data sets do not glue together : ', year0, year1)
        quit()

#   compare months+days : should both be the same (monthly)
    if ( mmdd0 == 1216 and mmdd1 == 116 ) : # monthly data
        print('ok')    
    elif ( mmdd0 == 701 and mmdd1 == 701 ) : # daily data
        print('ok')
    else :
        print('+++ glueseries +++')
        print('Two timeseries do not match nicely')
        print('First series (last date)   : ', date0)
        print('Second series (frist date) : ', date1)
        quit()
#
#   create new structure
    S=getemptydata.getemptydata(ntimemax=n0+n1,timestamp=S0['timestamp'])

#
#   fill the structure
    S['valuelist'][0 :n0   ,:] = S0['valuelist']
    S['valuelist'][n0:n0+n1,:] = S1['valuelist']

    S['timelist'][0 :n0   ] = S0['timelist']
    S['timelist'][n0:n0+n1] = S1['timelist']

    S['name']   = S0['name']
    S['units']  = S0['units']
    S['ntime']  = n0+n1


    S['timestamp'] = S0['timestamp']
    S['latitude']  = S0['latitude']
    S['nlat']      = S0['nlat'] 
    S['scenario']  = S0['scenario']+'_'+S1['scenario']
#
#   return
    return S

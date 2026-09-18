import insituread
import insituwrite

def insituextract(expid,variable,location):
#-----------------
#
    if ( location == 'AmsterdamIsland' ) : xlon=77.57 ; xlat=-37.8
    else :
        print('+++ insituextract +++')
        print('No location recognized : ', location)    
        quit()
#
# reade the data
    data=insituread.insituread(expid=expid, variable=variable, xlon=xlon, xlat=xlat)

# write the data
    insituwrite.insituwrite(D=data,location=location)

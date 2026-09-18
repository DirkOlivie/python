import getsondelist
import readsonde
import extractsondetuple
import standardizesondetuple

def readshadozprofile( station, season, xvar, yvar):
#--------------------
    '''
    MODIFICATIONS
        (204-02-21) creation

    CALLS
        getsondelist
        readsonde
        extractsondetuple
        standardizesondetuple
    '''

# get sondelist
    sondelist=getsondelist.getsondelist(station=station, season=season)

# make average sonde
    datalist=[]

# read all individual sondes
    for sonde in sondelist :
        print('Start reading sonde : '+sonde)
        data= readsonde.readsonde(sonde=sonde)                                          # read the data

        data= extractsondetuple.extractsondetuple(S=data, xvar=xvar, yvar=yvar) # extract x and y variables

        data= standardizesondetuple.standardizesondetuple(S=data)                                             # interpolate to standard grid

        datalist.append(data)

# return the data
    return datalist

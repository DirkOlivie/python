import numpy as np

def yearlist2blocklist(yearlist, activity, resolution):
#--------------------------
    '''
    METHOD
        - split yearlist in blocks (for reducing size of reading/manipulating data)
        - there is a maximum size of blocks : maxlen
        - consecutive years     : can end up in same block
        - non-consecutive years : should be in different blocks

    INPUT 
        yearlist : list of years
        activity
        resolution : ne16pg3, ne30pg2, 1.9x2.5, 0.9x1.25, ...

    REPORT
        (2026-04-16) : ne16pg3 nhist problems for ari and bb when maxlen=50 -> tried maxlen=20
        (2026-04-20) : added resolution as input data
    '''
#   
#   maximum size of block
    if   ( activity == 'air' ) : 
        if ( resolution == 'ne30pg3' ) : maxlen = 10 
        else                           : maxlen = 10 # problems for ne16pg3
    elif ( activity == 'bb'  )         : maxlen = 20 # problems for ne16pg3
    else                               : maxlen = 50

    nyear = len(yearlist)

    yearblocklist=[]

    yearblock=[]

    for iyear in range(nyear) :

        year    =    yearlist[iyear]

        if ( len(yearblock) == 0 ) :                 # attach
            yearblock.append(    year)               # add first element to shortlist
        elif ( yearblock[-1] + 1 == year and len(yearblock) < maxlen ) : # attach
            yearblock.append(    year)                                   # append consecutive year  
        elif ( ( len(yearblock) == maxlen ) \
            or ( yearblock[-1] + 1 != year ) )  :
            yearblocklist.append(yearblock)          # glue short list into overarching list
            yearblock     = [year]                   # start new short list with first element
        else : 
            print('+++ splityearlist +++')
            quit()

# possibly add last block if not empty
    if ( len(yearblock) != 0 ) :
        yearblocklist.append(yearblock)          # glue short list into overarching list
    
    return yearblocklist

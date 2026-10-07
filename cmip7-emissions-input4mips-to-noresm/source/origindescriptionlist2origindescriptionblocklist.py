import numpy as np
import origindescriptionlist_check_validity

def origindescriptionlist2origindescriptionblocklist(origindescriptionlist, activity, resolution):
#---------------------------------------------------
    '''
    METHOD
        - split yearlist in blocks (for reducing size of reading/manipulating data)
        - there is a maximum size of blocks : maxlen
        - consecutive years     : can end up in same block
        - non-consecutive years : should be in different blocks

    INPUT 
        origindescriptionlist : list of dictionaries
            [['year' : ..., 'i4mpdwnloadlist' : ..., 'origyearlist' : ..., 'origweightlist' : ...], 
             ...,
             ...
            ]
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

    blocklist=[]

    block=[]

    for origindescription in origindescriptionlist :

        if ( len(block) == 0 ) :                 # attach
            block.append(origindescription)      # add first element to shortlist
        elif ( ( len(origindescription['origyearlist']) == 1 ) \
           and ( len(block[-1]['origyearlist'])         == 1 ) \
           and ( block[-1]['origyearlist'][0] + 1       ==  origindescription['origyearlist'][0] ) \
           and ( len(block) < maxlen                     ) ): # attach i f
            block.append(origindescription)                                   # append consecutive year  
        elif ( ( len(origindescription['origyearlist']) != 1) \
            or ( block[-1]['origyearlist'][0] + 1       !=  origindescription['origyearlist'][0] ) 
            or ( len(block) == maxlen ) )  :
            origindescriptionlist_check_validity.origindescriptionlist_check_validity(block) # check format
            blocklist.append(block)          # glue short list into overarching list
            block     = [origindescription]  # start new short list with first element
        else :             
            print('+++ origindescriptionlist2origindescriptionblocklist +++')
            print('No situation recognized : origindescriptionlist')
            print(origindescriptionlist)
            print('block : ', block)
            print('blocklist : ', blocklist)
            quit()

# possibly add last block if not empty
    if ( len(block) != 0 ) :
        origindescriptionlist_check_validity.origindescriptionlist_check_validity(block) # check format
        blocklist.append(block)          # glue short list into overarching list
    
    return blocklist

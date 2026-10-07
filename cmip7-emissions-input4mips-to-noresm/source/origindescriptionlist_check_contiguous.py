def origindescriptionlist_check_contiguous(origindescriptionlist) :
#-----------------------------------------
    '''
    CONDITIONS
        (1) all contributing years are consecutive
        (2) all arrays have lenght 1 
                weights are [1.]
                contributingyears
                all i4mpdownloads are equal
                all scenarios are equal
    '''
    result = True
#
    n=len(origindescriptionlist)

#   check length : should all be of length 1
    for line in origindescriptionlist :

        if ( ( len(line['scenariolist'    ]) != 1 ) \
          or ( len(line['i4mpdownloadlist']) != 1 ) \
          or ( len(line['origyearlist'    ]) != 1 ) \
          or ( len(line['origweightlist'  ]) != 1 ) ) : result = False

#   check contiguous
    if ( result ) :
        origyearlist=[]    

        for line in origindescriptionlist :
            origyearlist.append(line['origyearlist'][0])

        for i in range(0,n-1) :
            if ( origyearlist[i+1] != origyearlist[i] +1 ) : result = False

#   
    return result

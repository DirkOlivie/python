def origindescriptionlist_check_average_contiguous(origindescriptionlist) :
#-------------------------------------------------
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

#   there should be only one contribution
    if ( n != 1 ) : result = False

    if ( result ) : 

        for line in origindescriptionlist :

            n = len(line['scenariolist']) # how many contributions to the average

#           same scenario / same i4mpdownload
            for i in range(0,n-1) :
                if ( line['scenariolist'    ][i+1] != line['scenariolist'    ][i]    ) : result = False
                if ( line['i4mpdownloadlist'][i+1] != line['i4mpdownloadlist'][i]    ) : result = False
                if ( line['origyearlist'    ][i+1] != line['origyearlist'    ][i] +1 ) : result = False
#   
    return result

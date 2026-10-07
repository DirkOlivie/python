def origindescriptionlist_check_average(origindescriptionlist) :
#-----------------------------------------
    '''
    CONDITIONS
        (1) has only 1 elements
        (2) all arrays have lenght 1 
                weights are [1.]
                contributingyears
                all i4mpdownloads are equal
                all scenarios are equal
    '''
    result = True
#
    n=len(origindescriptionlist)
#
    if ( n != 1 ) : result = False
#   
    return True

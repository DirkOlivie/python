def origindescriptionlist_check_validity(origindescriptionlist) :
#-----------------------------------------
    '''
    CONDITIONS
        (1) all contributing years are consecutive
        (2) all arrays have lenght 1 
        (3) sum of weights is 1
        (4) all weight are between 0 and 1
        (5) order of years should be increasing
    '''
#
    yearlist=[]
#
    for line in origindescriptionlist :

#       checkl length of arrays
        if ( ( len(line['scenariolist']) != len(line['i4mpdownloadlist']) ) \
          or ( len(line['scenariolist']) != len(line['origyearlist'    ]) ) \
          or ( len(line['scenariolist']) != len(line['origweightlist'  ]) ) ) : 

            print('+++ origindescriptionlist_check_validity +++')    
            print('Incoherent lenght of arrays : ')
            quit()

#       weight should add up to 1
        if ( sum(line['origweightlist']) < 0.999999 \
          or sum(line['origweightlist']) > 1.000001 ) : 
            print('+++ origindescriptionlist_check_validity +++')
            print('Weights do not add up to 1 : ', sum(line['origweightlist']))
            quit()

#       weight should be in interval [0,1]
        for weight in line['origweightlist'] :
            if ( weight < 0 or weight > 1 ) : 
                print('+++ origindescriptionlist_check_validity +++')
                print('Weight should be between 0 and 1 : ', weight)
                quit()
 
#       origyearlist should be consecutive
        lastyear=None
        for year in line['origyearlist'] :
            if ( lastyear != None ) :
                if ( year != ( lastyear  + 1 ) ) :
                    print('+++ origindescriptionlist_check_validity +++')
                    print('Origyearlist not consecutive : ', lastvalue)
                    quit()
                else :
                    lastyear =  year
#
        yearlist.append(line['year'])

# check that years are in increasing order
    lastyear=None
    for year in yearlist :
        if ( lastyear != None ) :
            if ( year <= lastyear ) :
                print('+++ origindescriptionlist_check_validity +++')
                print('Origyearlist not consecutive : ', lasvalue)
                quit()
            else :
                lastyear =  year

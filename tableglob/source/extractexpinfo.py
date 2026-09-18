def extractexpinfo (expdef) :
#-----------------
    '''
    MODIFICATIONS
    	(2021-11-27) : creation
        (2024-11-11) : allow for 1, 2, 3, or 4 experiments

            exp/w/date/xdiff
            exp/exp/w/w/date/date/xdiff
            exp/exp/exp/w/w/w/date/date/date/xdiff
            exp/exp/exp/exp/w/w/w/w/date/date/date/date/xdiff
    '''
#   count number of occurences of "/"
    nslash = expdef.count("/")

#   split based on "/"
    line=expdef.split("/")

#   
    if ( nslash != 3 and nslash != 6 and nslash != 9 and nslash != 12 ) :
        print('Syntax not correct : ', expdef)
        quit()

    n = nslash // 3 # integer division by 3 : because three datapieces, i.e., expid, weight, date

#   initialization
    expA='' ; wA=0. ; yrA0=-1 ; yrA1=-1 ; seasonA=''
    expB='' ; wB=0. ; yrB0=-1 ; yrB1=-1 ; seasonB=''
    expC='' ; wC=0. ; yrC0=-1 ; yrC1=-1 ; seasonC=''
    expD='' ; wD=0. ; yrD0=-1 ; yrD1=-1 ; seasonD=''
#        
#   experiment A
    if ( n >= 1 ) : expA=line[0] ; wA=float(line[n+0]) ; dateA=line[n*2+0] 
    if ( n >= 2 ) : expB=line[1] ; wB=float(line[n+1]) ; dateB=line[n*2+1]
    if ( n >= 3 ) : expC=line[2] ; wC=float(line[n+2]) ; dateC=line[n*2+2]
    if ( n >= 4 ) : expD=line[3] ; wD=float(line[n+3]) ; dateD=line[n*2+3]
    xdiff=line[n*3]

#   split dates
    if ( n >= 1 ) : line=dateA.split("-") ; yrA0=int(line[0]) ; yrA1=int(line[1]) ; seasonA=line[2]   # date A
    if ( n >= 2 ) : line=dateB.split("-") ; yrB0=int(line[0]) ; yrB1=int(line[1]) ; seasonB=line[2]   # date B
    if ( n >= 3 ) : line=dateC.split("-") ; yrC0=int(line[0]) ; yrC1=int(line[1]) ; seasonC=line[2]   # date C
    if ( n >= 4 ) : line=dateD.split("-") ; yrD0=int(line[0]) ; yrD1=int(line[1]) ; seasonD=line[2]   # date D
#
#   final return structure
    expinfo={'xdiff' : xdiff, \
             'n' : n }
#   
    if ( n >= 1) : expinfo.update({'expA' : expA, 'wA' : wA, 'yrA0' : yrA0, 'yrA1' : yrA1, 'seasonA' : seasonA})
    if ( n >= 2) : expinfo.update({'expB' : expB, 'wB' : wB, 'yrB0' : yrB0, 'yrB1' : yrB1, 'seasonB' : seasonB})
    if ( n >= 3) : expinfo.update({'expC' : expC, 'wC' : wC, 'yrC0' : yrC0, 'yrC1' : yrC1, 'seasonC' : seasonC})
    if ( n >= 4) : expinfo.update({'expD' : expD, 'wD' : wD, 'yrD0' : yrD0, 'yrD1' : yrD1, 'seasonD' : seasonD})

    return expinfo  

def writedistributionlist(datalist) :
#------------------------
    '''
str("%.6f"%

    '''
    ngroup = len(datalist)

    nbound = len(datalist[0]['boundlist'])

    for i in range(nbound) :
#       boundary
        line=''
        line=line+str("%3i"% (datalist[0]['boundlist'][i]))
        line=line+' -> '
        line=line+str("%3i"% (datalist[0]['boundlist'][i]))
        line=line+' :'
        for igroup in range(ngroup):
            line=line+' '
            line=line+str("%8.0f"% (datalist[igroup]['boundarydistributionlist'][i]))
        print(line)

#       interval
        if ( i < nbound -1 ) :
            line=''
            line=line+str("%3i"% (datalist[0]['boundlist'][i]))
            line=line+' -> '
            line=line+str("%3i"% (datalist[0]['boundlist'][i+1]))
            line=line+' :'
            for igroup in range(ngroup):
                line=line+' '
                line=line+str("%8.0f"% (datalist[igroup]['intervaldistributionlist'][i]))
            print(line)

import analyseshadozprofile
#
def loopanalyseshadozprofile2(expidlist, legendlist, varlist, year0list, year1list, seasonlist, stationlist, verticalaxislist, figlayout, code):
#----------------------------
#
    '''
    MODIFICATIONS
        (2024-02-20) : creation

    CALLS
        analyseshadozprofile
    '''
#
    print('+++ loopanalyseshadozprofile2 +++')
#
    if ( len(expidlist) != len(year0list) 
      or len(expidlist) != len(year1list) ) :
        print('expidlist : '+string(len(expidlist)))
        print('year0list : '+string(len(year0list)))
        print('year1list : '+string(len(year1list)))
        quit()
#
    for verticalaxis in verticalaxislist :

        for station in stationlist :

            for var in varlist :

                for season in seasonlist :
# 
                    analyseshadozprofile.analyseshadozprofile(expidlist=expidlist, legendlist=legendlist, var=var, year0list=year0list, year1list=year1list, season=season, verticalaxis=verticalaxis,station=station, figlayout=figlayout, code=code)   
#
    print('--- loopanalyseshadozmeanprofile2 ---')        

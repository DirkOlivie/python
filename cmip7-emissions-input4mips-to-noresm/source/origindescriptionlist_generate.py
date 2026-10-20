import numpy as np
import origindescriptionlist_check_validity

def origindescriptionlist_generate(data):
#----------------------------------------
    '''
    INPUT
        data : list of dictionaries

    OPTIONS for type of input :
        CONTIGUOUS
            descriptiontype : 'contiguous'
            period : 1849-2023-annual
                     2030-2100-halfdecadal
            i4mpdownload :    [NO "list" in key]
            scenario     :    [NO "list" in key]

        AVERAGE
            descrptiontype    : average
            year : 2005
            origyearlist      : 2002, 2003, 2004, 2005, 2006, 2007, 2008        
            i4mpdownloadlist  : 
            origscenarioslist :  CMIP
    '''        

    n= len(data)

    newdata=[]
    
    for line in data :
        print('line : ', line)


#       contiguous data
        if ( line['descriptiontype'] == 'contiguous' ) : 
            periodsplit=line['period'].split('-')
            if ( len(periodsplit) == 3 ) : 
                year0     = int(periodsplit[0])
                year1     = int(periodsplit[1])
                frequency =     periodsplit[2]
            else :
                print('+++ origindescription_generate +++')
                print('Period have yyyy-yyyy-xxx format : ', period)
                quit()
 
#           make list of years   
            if ( frequency == 'annual' ) :
                yearlist=np.arange(year0,year1+1) # list  of consecutive years

            else : 
                print('+++ origindescription_generate +++')
                print('No frequency recognized : ', frequency)
                quit()

            for year in yearlist :
                yearinfo = { 'year' : year, 'scenariolist': [line['scenario']], 'i4mpdownloadlist' : [line['i4mpdownload']], 'origyearlist':[year], 'origweightlist':[1.] }
                newdata.append(yearinfo)                
#
#       average data
        elif ( line['descriptiontype']  == 'average' ) : 
#           check length of arrays
            if ( ( len(line['scenariolist']) != len(line['i4mpdownloadlist'] ) ) \
              or ( len(line['scenariolist']) != len(line['origyearlist'] ) ) ) :
                print('+++ origindescription_generate +++')
                print('Different lengths for scenariolist, i4mpdownloadlist and origyearlist')
                print('scenariolist     : ', line['scenariolist'])
                print('i4mpdownloadlist : ', line['i4mpdownloadlist'])
                print('origyearlist     : ', line['origyearlist'])
                quit()
            
            nlen = len(line['scenariolist'])
    
            yearinfo={ 'year' : line['year'], 'scenariolist': line['scenariolist'], 'i4mpdownloadlist' : line['i4mpdownloadlist'], 'origyearlist':line['origyearlist'], 'origweightlist':[1./float(nlen)]*nlen }

            newdata.append(yearinfo)
#
#       not recognized
        else : 
            print('+++ origindescription_generate +++')
            print('No description recognized : ', line['description'])            
            quit()

#
#   check validity
    origindescriptionlist_check_validity.origindescriptionlist_check_validity(newdata)
#
    return newdata

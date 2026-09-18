import re
import gzip


def getdiagvaluelistsinglefile(filename, freqtype, budgettype, component, variable):
#-----------------------------
    '''
    INPUT



    '''

    print(filename)
    
    if   ( budgettype == 'area' )  : cbudgettype = 'NET AREA BUDGET' 
    elif ( budgettype == 'heat' )  : cbudgettype = 'NET HEAT BUDGET' 
    elif ( budgettype == 'water' ) : cbudgettype = 'NET WATER BUDGET' 
    else :
        print('+++ getdiagvaluelistsingle +++')
        print('No budgettype recognized : ', budgettype)
        quit()

    if ( variable == 'sum' ) : cvariable = '*SUM*'
    else                     : cvariable = variable

    if ( component == 'sum' ) : ccomp = '*SUM*'
    else                      : ccomp = component 



    print('filename : ', filename)
    print('freqtype : ', freqtype)
    print('budgettype : ', budgettype)
    print('ccomp : ', ccomp)
    print('cvariable : ', cvariable)

    if (filename[-3:] == '.gz' ) : f = gzip.open(filename, mode='rt')
    else                         : f = open(filename, 'r')


    looking_for_budgettype_and_freqtype=True
    looking_for_componentlist=False
    looking_for_value=False

    data={}

    for line in f :

#       gzip some read as bite -> has to be
#        if (filename[-3:] == '.gz' ) : line = line.decode('ascii').strip()
#        else                         : line = line.strip()

#        print(line)


        line = line.replace('ice nh', 'ice_nh')
        line = line.replace('ice sh', 'ice_sh')

#        line = line.replace("\n", '')

        line = line.strip()
        line = re.sub(' +',' ',line)

#        print(line)

#        line = line.split(' ')

#        print(line)

        if ( looking_for_budgettype_and_freqtype) : 
#            print('freqtype : ', freqtype)
#            print('budgettype : ', budgettype)         

            if ( freqtype+':' in line and cbudgettype in line ) : 
#                               
#                line = line.rstrip() # remove leading and trailing blanks
#                line = re.sub(' +',' ',line)
                line = line.split(' ')
                    
                ipos_date = line.index('date') + 2
                yyyymmdd = line[ipos_date]

                looking_for_budgettype_and_freqtype=False
                looking_for_componentlist=True

#                print('A')                

        elif ( looking_for_componentlist ) :

#            print(line)

            if ( 'atm' in line and 'lnd' in line and 'rof' in line and 'ocn' in line and 'ice_nh' in line and 'ice_sh' in line and 'glc' in line and '*SUM*' in line) :
#
#               blanco in "ice sh" and "ice nh" complicates -> replace by "ice_sh" and "ice_nh"                 
#                line = line.replace('ice nh', 'ice_nh')
#                line = line.replace('ice sh', 'ice_sh')

#                line = line.rstrip() # remove leading and trailing blanks
#                line = re.sub(' +',' ',line)
                line = line.split(' ')

                ipos_comp = line.index(ccomp) + 1
                
                looking_for_componentlist=False
                looking_for_value=True

#                print('B')

        elif ( looking_for_value ) :
            if ( cvariable in line ) :
#
#                line = line.rstrip() # remove leading and trailing blanks
#                print(line)
#                line = re.sub(' +',' ',line)
                line = line.split(' ')
#                print(line)
#                print('ipos_comp : ', ipos_comp)
#                print('line[ipos_comp] : ', line[ipos_comp])

                value = float(line[ipos_comp])

                data[yyyymmdd] = value

                looking_for_value=False
                looking_for_budgettype_and_freqtype=True

#                print('C')

        else :
            print('No choice recognized')
            quit()


#   CLOSE
    f.close()

    print(data)

#   RETURN DICTIONARY
    return data

    












import sys
import tableanalyse

def main():
#
    print('+++ tableglobloop +++')
    print('--- tableglobloop ---')

#   the name of the prgoram is al
    print(len(sys.argv))
    print(sys.argv)

    if ( len(sys.argv) != 2 ) : 
        print('Incorrect number of arguments')
        exit(0)
    else :
        description = sys.argv[1]
        filename='../description/description.'+description+'.txt'   

    print(filename)
#
#   open the file and read the lines
    f=open(filename)

    for line in f: 

        if line[0] == '#'  :
            continue

        elif 'BEGIN' in line :
            nexpid=0 
            print('2')
            info=[]
            print(info) 
            orientation='x(exp)-y(var)'  
            myformat="{0:.5e}"

        elif 'CODE=' in line :
            print('CODE')
            line=line.split('=')
            code=line[1].strip()
            print(code)

        elif 'ORIENTATION=' in line :
            print('ORIENTATION')
            line=line.split('=')
            orientation=line[1].strip()
            print(orientation)

        elif 'MYFORMAT=' in line :
            print('MYFORMAT')
            line=line.split('=')
            myformat=line[1].strip()
            print(myformat)

        elif 'EXP=' in line :

            line=line.split('=') # EXP=.... -> EXP <expid>
            expdef=line[1].strip()  # <expid>
            print('expdef : '+expdef)           
 
            if nexpid==0 :
               expdeflist=[expdef]
            else :
               expdeflist.append(expdef)

            nexpid=nexpid+1

#            print(line.strip())
            print('+++ expdeflist ++++ : ')  
            print(expdeflist)

        elif 'VARLIST' in line : 
            print('varlist')
            line=line.strip()              # skip \n
            line=line.split('=')
            varlist=line[1].split(',') 

        elif 'END' in line : 
            print('3')
            tableanalyse.tableanalyse(code=code, expdeflist=expdeflist, varlist=varlist, orientation=orientation, myformat=myformat)

    f.close()

if __name__ == '__main__':
    main()

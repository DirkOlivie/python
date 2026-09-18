import readseriesnoresmemissions

def generateseriesnoresmemissions(filelist, prefactorlist, freqtype):
#--------------------------------
    '''
    INPUT
        filelist
        prefactorlist

    RETURN
        structure containing timeseries of emissions

    '''
    
    if ( len(filelist) != len(prefactorlist) ) :
        print('+++ generateseriesnoresmemissions +++')
        print('length filelist      : ', len(filelist))
        print('length prefactorlist : ', len(prefactorlist))
        quit()

    nfile = len(filelist)

    for ifile in range(nfile) :
        file      = filelist[ifile]
        prefactor = prefactorlist[ifile]

        tmp = readseriesnoresmemissions.readseriesnoresmemissions(file=file, freqtype=freqtype)

        if ( ifile == 0 ) : 
            data = tmp
            data['valuelist'] =                     tmp['valuelist'] * prefactor
        else :
            data['valuelist'] = data['valuelist'] + tmp['valuelist'] * prefactor
            
    return data

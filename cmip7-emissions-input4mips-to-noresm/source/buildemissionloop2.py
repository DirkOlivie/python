import numpy as np

import buildemission

def buildemissionloop2(groupdescriptionlist,resolutionlist, vertintplist, periodlist, version, noresmversionlist, scenariolist, project, filelocation, overwrite):
#---------------------
    '''
    INPUT
        vertdist
        resolutionlist
        vertintplist
        activity : only 1 activity
        sectorliststring
        speciesliststring
        periodlist
        version
        noresmversionlist
        i4mpdownload_anthro
        i4mpdonwload_bb
        filelocation
        overwrite

    CALLED BY
        buildemissionloop

    CALLS
        buildemission

    '''
#
    print('+++ Starting : buildemissionloop2 +++')
#
    # convert speciesliststring -> specieslist
#    specieslist=speciesliststring.split('-')
    #
    for period in periodlist :
        for resolution in resolutionlist :
            for scenario in scenariolist :
                for vertintp in vertintplist :
                    for noresmversion in noresmversionlist :
                        for groupdescription in groupdescriptionlist :
                            activity         = groupdescription['activity']
                            vertdist         = groupdescription['vertdist']
                            sectorliststring = groupdescription['sectorliststring']
                            specieslist      = groupdescription['specieslist']
                            i4mpdownload     = groupdescription['i4mpdownload']
                            for species in specieslist :

                                print('Hallo')  

                                buildemission.buildemission(vertdist=vertdist,resolution=resolution,vertintp=vertintp, activity=activity,sectorliststring=sectorliststring,species=species,period=period, version=version, noresmversion=noresmversion, scenario=scenario, i4mpdownload=i4mpdownload, project=project, filelocation=filelocation, overwrite=overwrite)

import numpy as np

import buildemission

def buildemissionloop2(activitydescriptionlist,resolutionlist, vertintplist, periodlist, version, noresmversionlist, scenariohybrid, project, filelocation, overwrite):
#---------------------
    '''
    MODIFICATION
        (2026-09-27) : i4mpdownload replaced by origindescriptionlist

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
            for vertintp in vertintplist :
                for noresmversion in noresmversionlist :
                    for activitydescription in activitydescriptionlist :
                        activity         = activitydescription['activity']
                        vertdist         = activitydescription['vertdist']
                        sectorliststring = activitydescription['sectorliststring']
                        specieslist      = activitydescription['specieslist']
#                            i4mpdownload         = activitydescription['i4mpdownload']
                        origindescriptionlist = activitydescription['origindescriptionlist']
                        for species in specieslist :

                            print('Hallo')  

                            buildemission.buildemission(vertdist=vertdist,resolution=resolution,vertintp=vertintp, activity=activity,sectorliststring=sectorliststring,species=species,period=period, version=version, noresmversion=noresmversion, scenariohybrid=scenariohybrid, origindescriptionlist=origindescriptionlist, project=project, filelocation=filelocation, overwrite=overwrite)

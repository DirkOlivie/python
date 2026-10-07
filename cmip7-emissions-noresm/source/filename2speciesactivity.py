def filename2speciesactivity(filename):
#---------------------------
    '''
    EXAMPLE OF FILE : CONTAINS WHOLE FILEPATH
        /scratch/olivie/code/python/cmip7-emissions-input4mips-to-noresm/data/output/version20260927/individual/histclimo/1.9x2.5/emissions_cmip7_noresm3_HCOOH_anthrosurfgasALL_surface_histclimo_1850-2023_1.9x2.5_CEDS-CMIP-2025-04-18_version20260927.nc

    '''
#   split basded on "/"
    line=filename.split('/')[-1] # take only part after last "/"

#   split baded on "_"
    line=line.split('_')
#
#   check species
    species = line[3]   

#   check acitivity
    word = line[4]
    if   ( 'ALL' in word ) :
        activity = word.replace('ALL','')
    else :
        print('+++ filename2speciesactivity +++')
        print('No activity could be derived from : ', word)
        quit()
#
    return species, activity

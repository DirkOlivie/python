def getspeciesinfo(species, activity):
#---------------------------
    '''	
    MODIFICATIONS
        (2021-02-23) : perturbations passing via commonblock

    CALLED BY
        buildemission
    '''

#-----------------------------------------
#
#  so4frac=getvalue_commonblock(descriptor='so4frac')
#
    if   ( species == 'BC_N'  ) : origspecies='BC' ; weight = 0.9
    elif ( species == 'BC_AX' ) : origspecies='BC' ; weight = 0.1
    elif ( species == 'BC_NI' ) : origspecies='BC' ; weight = 1.0   
    elif ( species == 'OM_NI' ) : origspecies='OC' ; weight = 1.0
    elif ( species == 'SO2'   ) : origspecies='SO2'; weight = 0.975
# case so4frac of 
#                                           '0.000' : weight = 1.0 
#                                           '0.025' : weight = 0.975 
#                                           '0.075' : weight = 0.925 
#                                         endcase        & end
    elif ( species == 'SO4_PR' ) : origspecies='SO2' ; weight = 0.025
#& case so4frac of 
#                                           '0.000' : weight = 0.0 
#                                           '0.025' : weight = 0.025 
#                                           '0.075' : weight = 0.075 
#                                         endcase        & end
    else :
        print('No species recognized : ', species)
        quit()       

# data structure    
    data={'origspecies' : origspecies, \
        'weight'      : weight}
#
    return data

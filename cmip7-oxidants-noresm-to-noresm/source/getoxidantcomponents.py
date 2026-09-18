import numpy as np

def getoxidantcomponents(species):
#-----------------------
    '''
    INPUT
        species

    RETURN
        complist, weightlist

    MODIFICATIONS
        (2026-09-12) 
            added HALONS
            weighlist : conversion from list into numpy-array

    '''
#
    if ( species == 'H2O_EMIS' ) :
        complist   =          ['CH4_CHML']
        weightlist = np.array([2.], dtype=float)
    elif ( species == 'PS' \
        or species == 'HO2' \
        or species == 'NO3' \
        or species == 'OH'
        or species == 'O3' ) :
        complist   =          [species]
        weightlist = np.array([1.], dtype=float)
    elif ( species == 'HALONS' ) :
#                   method = "(CFC113*0.3+CFC114*0.31+CFC115*0.18+CCL4*0.13+CH3CCL3*0.06+CH3CL*0.01+HCFC22*0.2+HCFC141B*0.14+HCFC142B*0.2+CF2CLBR*0.3+CF3BR*0.32+H2402*0.33)/0.25
        complist   =          ['CFC113','CFC114','CFC115','CCL4','CH3CCL3','CH3CL','HCFC22','HCFC141B','HCFC142B','CF2CLBR','CF3BR','H2402']
        weightlist = np.array([ 0.3    , 0.31   , 0.18   , 0.13 , 0.06    , 0.01  , 0.2    , 0.14     , 0.2      , 0.3     , 0.32  , 0.33  ], dtype=float) / 0.25                
    else :
        print('+++ readmeanfieldoxidants +++')
        print('No species recognized : ', species)
        quit()
#
    if ( len(complist) != len(weightlist) ) :
        print('+++ readmeanfieldoxidants +++')
        print('Length complist   : ', len(complist))
        print('Length weihgtlist : ', len(weightlist))
        quit()

    return complist, weightlist

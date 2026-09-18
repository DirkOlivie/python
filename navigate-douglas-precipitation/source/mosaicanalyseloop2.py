import mosaicanalyse

def mosaicanalyseloop2(expiddescriptionlist, var, suptitle, addcolorbar, code):
#---------------------
    '''
    CALLED BY
        mosaicanalyseloop

    CALLS
        mosaicanalyse

    '''
    mosaicanalyse.mosaicanalyse(expiddescriptionlist=expiddescriptionlist, var=var, suptitle=suptitle, addcolorbar=addcolorbar, code=code)

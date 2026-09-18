def getlinestyle (linestyle, linestylescheme='default') :
#---------------
#'''
#    MODIFICATIONS
#        (2024-03-14)
#           
#    AIM 
#        conversion of number into linestyle of python
#        0 -> 'solid'
#        1 -> 'dotted'
#        2 -> 'dashed'
#        3 -> 'dashdot'
#
#    SEE
#        https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
#'''                  
    if ( linestylescheme == 'default' ) :
        linestylelist = ['solid', 'dotted', 'dashed', 'dashdot']
    elif ( linestylescheme == 'extended' ) :
        linestylelist = ['solid', 'dotted', 'dashed', 'dashdot', \
                         'loosely dotted', 'densely dotted', 'long dash with offset', 'loosely dashed', 'densely dashed', 'loosely dashdotted','dashdotted', 'densely dashdotted', 'dashdotdotted', 'loosely dashdotdotted']
    else : 
        print('No linestylescheme recognized : ', linestylescheme)
        quit()
#
    nlinestyle=len(linestylelist)

    name=linestylelist[linestyle % nlinestyle]
#
# column burden
    return name

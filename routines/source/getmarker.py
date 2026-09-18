def getmarker (marker, markerscheme='default') :
#------------
#'''
#    MODIFICATIONS
#        (2024-10-28)
#           
#    AIM 
#        conversion of number into marker of python
#        0 -> 'circle'
#        1 -> 'triangle_down'
#        2 -> 'triangle_up'
#        3 -> 'triangle_left'
#        4 -> 'triangle_right'
#        5 -> 'octagon'
#        6 -> 'square'
#        7 -> 'pentagon'
#        8 -> 'plus (filled)'
#        9 -> 'star'
#        10 -> 'hexagon1' 
#
#    SEE
#        https://matplotlib.org/stable/api/markers_api.html
#'''                  
    if ( markerscheme == 'default' ) :
        markerlist = ["o","v","^","<",">","8","s","p","P","*","h"]
    elif ( markerscheme == 'extended' ) :
        markerlist = ["o","v","^","<",">","8","s","p","P","*","h"] # not yet done
    else : 
        print('No markerscheme recognized : ', markerscheme)
        quit()
#
    nmarker=len(markerlist)

    name=markerlist[marker % nmarker]
#
# column burden
    return name

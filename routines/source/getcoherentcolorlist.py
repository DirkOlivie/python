def getcoherentcolorlist(legendlist, refcolorlist, reflegendlist):
#-----------------------

    if ( len(refcolorlist) != len(reflegendlist) ) :
        print('Different length for refcolorlist and reflegendlist : ')
        print('refcolorlist  : ', len(refcolorlist))
        print('reflegendlist : ', len(reflegendlist))
        quit()   

    colorlist=[]
    previouscolor=None

    for legend in legendlist :

        if ( legend == '' ) : 
             colorlist.append(previouscolor)
        else :
             color=refcolorlist[reflegendlist.index(legend)]
             colorlist.append(color)
             previouscolor=color
                   
    return colorlist     



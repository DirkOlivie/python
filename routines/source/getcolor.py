def getcolor (color, colorscheme='tableau') :
#-----------
#
# MODIFICATIONS
#       (2023-10-20)
#           adding keword for colorscheme : default = 'tableau'
#               'keyclim-wp6' : grey   : #4d4d4d
#                               red    : #e41a1c
#                               blue   : #377eb8
#                               green  : #4daf4a
#                               purple : #984ea3
#                               orange : #ff7f00
#                               brown  : #a65628
#           
#               'Tableau colors'
#                   

    if ( colorscheme == 'tableau' )       : colorlist=['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']
    elif ( colorscheme == 'keyclim-wp6' ) : colorlist=['#808080','#e41a1c','#377eb8','#4daf4a','#984ea3','#ff7f00','#a65628']
    elif ( colorscheme == 'idl' )         : colorlist=[[0,0,0],[1,0,0],[0,0,1],[0,1,0],[1,0,1],[0,1,1],[0.1,0.7,0.7],[0.6,0.9,0.2],[0.9,0.65,0.2],[0.5,0.5,0.5]]
    elif ( colorscheme == 'toar' )        : colorlist=[[50/256,205/256,50/256],[255/256,165/256,0],[0,0,255/256],[255/256,0,0],[0,255/256,255/256],[255/256,0,255/256],[138/256,43/256,226/256],[0,100/256,0]]
    else                                  : 
        print('No colorscheme recognized : ', colorscheme) 
        quit() 

    ncolor=len(colorlist)

    name=colorlist[color % ncolor]
#
# column burden
    return name

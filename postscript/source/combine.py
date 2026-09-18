import numpy as np

def combine(figlist, figdir, figout, nx, ny, figincludelist=None, inversion=0, ifirstfig=0):
#-------------
    '''
    MODIFICATIONS
	    (2019-11-21) creation

     CALLED BY
	    loopcombne

                        [ x1 ]
-------------------------------------------->
                      | ////////////////////  ^
                      | ////////////////////  |
                      | ////// figure //////  |
                      | ////////////////////  |
        [ x0 ]        | ////////////////////  |
--------------------->------------------------|
                      ^                       | y1
                      |                       |
                   y0 |                       |
                      |                       |
                      |                       | 

     INPUT
 	    figlist
	    figdir
        figout
        figincludelist
	    nx
	    ny
 	    inversion
    '''
    #-------------------------------------------------
#
#   figincludelist    
    if ( figincludelist == None) : figincludelist = np.zeros(len(figlist), dtype=int) + 1
    print('figincludelist : ', figincludelist)
#
#   figlist and figincludelist
    if ( len(figlist) != len(figincludelist) ) :
        print('Different array length for : ')
        print('figlist : ', len(figlist))
        print('figincludelist : ', len(figincludelist))
        quit()
#
#   number of figures
    nfig = len(figlist)

#   open final file
    fout = open('/scratch/olivie/code/python/postscript/data/output/'+figout, 'w')
#
#   empty list
    fin=[]

#   read first fig
    infile=figdir+'/'+figlist[ifirstfig]
    fid  = open(infile, 'r')
    for line in fid:
        fin.append(line)
    fid.close()
#
#   number of lines
    nline= len(fin) 

    iline=0  
#   I. search for %%BoundingBox
###############################
    while ( fin[iline].find('%%BoundingBox') == -1 ) :
        fout.write(fin[iline])                           # write unmodified line
        iline=iline+1       

#   this line contains '%%BoundingBox' 
    line=fin[iline]
    linesplit=line.split(' ')
#   original boundingbox : corners
    x0 = float(linesplit[1])
    y0 = float(linesplit[2])
    x1 = float(linesplit[3])
    y1 = float(linesplit[4])

    print('Original boundingbox : ')
    print('x0 : ', x0)
    print('y0 : ', y0) 
    print('x1 : ', x1)
    print('y1 : ', y1) 
#
#   original boundingbox : width
    dx = x1 - x0
    dy = y1 - y0
#
#   new boundingbox : keep original width, addapt the vertical positioning
    dx_new = dx
    dy_new = dy / float(nx) * float(ny)
#
#   new boundingbox : corners
    newx0 = x0
    newy0 = y1 - dy_new
    newx1 = x0 + dx_new
    newy1 = y1
#
    print('New boundingbox : ')
    print('x0 : ', newx0)
    print('y0 : ', newy0)
    print('x1 : ', newx1)
    print('y1 : ', newy1)
#
#   vertical extend of 1 new panel
    dypanel = ( newy1 - newy0 ) / float(ny)
#
    print('dy = ', dy)
    print('dy_new = ', dy_new)
    print('dypanel = ', dypanel)
#
#   write Boundingbox to final file
    fout.write('%%BoundingBox:' \
               +' '+str("%.2f"% newx0) \
               +' '+str("%.2f"% newy0) \
               +' '+str("%.2f"% newx1) \
               +' '+str("%.2f"% newy1))
    fout.write('\n')
#
#   II. search for "%%EndComments"
    iline=iline+1
    while ( fin[iline].find('%%EndComments') == -1 ) :
        fout.write(fin[iline])           # wrtie all these lines
        iline=iline+1
#   this line contains '%%EndComments'
    fout.write(fin[iline]) # line with %%Page: 1 1
    iline=iline+1

#   III. search for "%%Page: 1 1"
    iline=iline+1
    while ( fin[iline].find('%%Page: 1 1') == -1 ) :
        iline=iline+1    
#   this line contains '%%Page: 1 1'
    fout.write(fin[iline]) # line with %%Page: 1 1
    iline=iline+1
#   
    factor=1.
    scalex = 1./float(nx)

#   IV .read all other figures 
    for ifig in range(0,nfig) :
#
        if ( ifig == 0 ) :
#           absolute positioning of first figures  
            if ( inversion == 0 ) :
                deltax=0
#               deltay=0 + (dy - dypanel) / factor * float(nx)
                deltay=0 + dypanel * float(ny-1) * float(nx)
            elif ( inversion == 1 ) :
                deltax=0
                deltay=0 + (dy - (4 - ny) * dypanel) / factor * float(nx)
            else :
                print('No inversion recognized : ', inversion)
                quit()
#    
        else :
#           relative w.r.t. former panel : deltax
            if ( ifig % nx != 0 ) :   # modulo
                deltax= (x1-x0) / factor            
            else :
                deltax= - (nx-1) * (x1-x0) / factor
#           relative w.r.t. former panel : deltay
            if ( ifig % nx != 0 ) :
                deltay= 0.
            else :
                deltay= - (y1-y0) / factor
                if ( inversion == 1) : deltay= + (y1-y0) / factor # NEW
#
        if ( ifig == 0 ) : 
            fout.write(str("%.2f"% newx0)+' '+str("%.2f"% newy0)+' translate') ; fout.write('\n')
            fout.write(str("%.2f"% scalex )+' '+str("%.2f"% scalex )+' scale') ; fout.write('\n')

        print('delta x : ', deltax)
        print('delta y : ', deltay)

#       translate
#        if ( inversion == 0 ) :
#            fout.write(str("%.2f"% deltax)+' '+str("%.2f"% deltay)+' translate') ; fout.write('\n')
#        elif ( inversion == 1 ) :
#            fout.write(str("%.2f"% deltay)+' '+str("%.2f"% deltax)+' translate') ; fout.write('\n')
#        else :
#            print('No inversion recognized : ', inversion)
#            quit()        
#
        if ( figincludelist[ifig] == 1 ) :

#            infile=figdir+'/'+figlist[ifig]
#            fin = open(infile, 'r')

#           empty list
            fin=[]

            fout.write('%%% NEW FIGURE PANEL') ; fout.write('\n')

#           read first fig
            infile=figdir+'/'+figlist[ifig]
            fid  = open(infile, 'r')
            for line in fid:
                fin.append(line)
            fid.close()
            print(infile) 

            nline=len(fin)
#
#           skip last 3 lines
            fin=fin[0:nline-3]
            nline=len(fin)
#
#           search for "%%BeginProlog" : should not be wrtitten until there                
            iline=0
            line=fin[iline]
            while ( fin[iline].find('%%BeginProlog') == -1 ) :
                iline=iline+1

#           search for "%%EndProlog : everything should be written until there"
            line=fin[iline]
            while ( fin[iline].find('%%EndProlog') == -1 ) :
                fout.write(fin[iline])
                iline=iline+1
#           write "%%EndProlog line"
            fout.write(fin[iline])
            iline=iline+1

#           search for "%%Page: 1 1" : should not be written until there
            while ( fin[iline].find('%%Page: 1 1') == -1 ) :
                iline=iline+1
#           Page line should not be written
            iline=iline+1
  
#           search for "mpldict begin" : should be written 
            while ( fin[iline].find('mpldict begin') == -1 ) :
                iline=iline+1
#           Page line should not be written
            fout.write(fin[iline])
            iline=iline+1


##           search for "translate" : should not be written until there
            while ( fin[iline].find('translate') == -1 ) :
                iline=iline+1
#           Page line should not be written
            iline=iline+1

##          search for "translate" : should not be written until there
            while ( fin[iline].find('clipbox') == -1 ) :
                iline=iline+1
#           Page line should not be written
            iline=iline+1

#          translate
            if ( inversion == 0 ) :
                fout.write(str("%.2f"% deltax)+' '+str("%.2f"% deltay)+' translate') ; fout.write('\n')
            elif ( inversion == 1 ) :
                fout.write(str("%.2f"% deltay)+' '+str("%.2f"% deltax)+' translate') ; fout.write('\n')
            else :
                print('No inversion recognized : ', inversion)
                quit()

#           all other lines should be written until there            
            line=fin[iline]
            while ( iline < nline ) :
                fout.write(fin[iline])
                iline=iline+1

#       in case of last figure
        if ( ifig == nfig-1 ) :            
            fout.write('end') ; fout.write('\n')
            fout.write('showpage') ; fout.write('\n')
            fout.write('%%EOF') ; fout.write('\n')

#   close output file
    fout.close()

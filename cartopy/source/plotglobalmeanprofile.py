import matplotlib.pyplot as plt
import numpy as np

import experimentdefinition

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import getidlvar
import getidlregion
import getstandardunits
import getidlunits
import getcolor
import getlinestyle
import getprefix

'''
    MODIFICATIONS
        (2023-10-20) Adding colorlist and colorscheme
        (2024-11-28) Adding csv file output

    PLOTS WITH DIFFERENT SCALES
        https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html
'''

def plotglobalmeanprofile(datalist,legendlist,wlist,figlayout,code,colorlist=None,linestylelist=None) :
#--------------------------------------------------------------
#
    '''
    INPUT
        datalist
        legendlist
        wlist : not used
        figlayout
        code : string appearing in filename of plot
        colorlist : [0,1,2,...]
        linestylelist : [0,1,0,0,...]    

    CALLED BY

    CALLS

    '''
#
    print('+++ plotglobalmeanprofile +++')
#
    nexpid=len(datalist)

#   optional parameters
#   if ( colorlist == None ) : colorlist = np.zeros(nexpid,dtype=int) # all zeros
    if ( colorlist == None ) : colorlist = np.arange(0,nexpid)  
    if ( linestylelist == None ) : linestylelist = np.zeros(nexpid,dtype=int) # all zeros

#   use first experiment to get some information
    var=datalist[0]['var']            # use first experiment to obtain units
    units=getstandardunits.getstandardunits(datalist[0]['units'])
    region=datalist[0]['region']
    verticalaxis=datalist[0]['verticalaxis'] # 'height' | 'pressure'

    year0=datalist[0]['year0']
    year1=datalist[0]['year1']
    season=datalist[0]['season']

    timestamp=str("%4.4i"% (year0))+'-'+str("%4.4i"% (year1))+'-'+season # appears in name of plot


#   FILENAME FOR FIGURE
    filename='globalmeanprofile_'+var+'_'+timestamp+'_'+region+'_'+verticalaxis+figlayout.xtype+figlayout.code+figlayout.ysplit+'_'+code

    prefix=getprefix.getprefix(filename=filename) # Figure title needs a) , b) , ...



#   POSSIBLY CHANGE UNITS
    print('var : ', '...'+var+'...')
    print('units : ', '...'+units+'...')
    if ( ( var == 'O3' or var == 'ozone' \
        or var == 'm_O3_c_as_vmr_drytest' or 'm_ozone_c_as_vmr_drytest' ) and units =='mol mol-1' ) : 
        factor=1.e+6
        newunits='ppm'
    elif ( ( var == 'CH4' or var == 'ch4' ) and units =='mol mol-1' ) : 
        factor=1.e+9
        newunits='ppb'
    elif ( ( var == 'CO2' or var == 'm_CO2_c_as_vmr_drytest' or var == 'm_CO2_c_as_vmr' ) and units =='mol mol-1' ) : 
        factor=1.e+6
        newunits='ppm'
    elif ( var == 'hus' and getstandardunits.getstandardunits(units) =='kg kg-1' ) : 
        factor=28.964/18.0153 * 1.e+6
        newunits='ppmv'
    else :
       factor=1.
       newunits=units   
    print('newunigs : ', newunits)

    fig,ax =plt.subplots(figsize=[4,5],dpi=100)     
#   ax.set_ylabel('Pressure [Pa]')
    ax.set_xlabel('['+getidlunits.getidlunits(units=getstandardunits.getstandardunits(units=newunits))+']') # use first experiment to obtain units
#   ax.set_title(getidlvar.getidlvar(var=variable))                  # use first experiment to obtain units
#    ax.set_title(getidlvar.getidlvar(var))                                           # use first experiment to obtain units
    ax.set_title(prefix+getidlvar.getidlvar(var=var)) #+' ['+getidlregion.getidlregion(region=region)+']')

#   VERTICAL AXIS : pressure/height logarithmic/linear
    if ( verticalaxis == 'pressure' ) :

        desired_zunits='hPa'     
        ax.set_ylabel('Pressure ['+desired_zunits+']')

        if ( figlayout.ytype == 'log' ) : # logaritmic scale for Y-axis
            ax.set_yscale('log')
#            ymin=1.
#            ymax=1000.
            if   ( figlayout.ysplit == 'split400hPa' ) : ylimitslist=[[1000.,400.],[400.,1.]] # hPa
            elif ( figlayout.ysplit == 'above500hPa' ) : ylimitslist=[[ 500.,1.]] # hPa 
            elif ( figlayout.ysplit == 'above100hPa' ) : ylimitslist=[[ 100.,1.]] # hPa 
            elif ( figlayout.ysplit == 'above150hPa' ) : ylimitslist=[[ 150.,1.]] # hPa 
            elif ( figlayout.ysplit == 'above200hPa' ) : ylimitslist=[[ 200.,1.]] # hPa 
            elif ( figlayout.ysplit == '' )            : ylimitslist=[[1000.,1.]] # hPa 
            else                                       : quit()  
#            plt.ylim([ymax,ymin])
        elif ( figlayout.ytype == '' ) : # linear scale for Y-axis     
#            ymin=20.
#            ymax=1000.
            if   ( figlayout.ysplit == 'split400hPa' ) : ylimitslist=[[1000.,400.],[400.,20.]] # hPa
            elif ( figlayout.ysplit == 'above500hPa' ) : ylimitslist=[[ 500.,1.]] # hPa
            elif ( figlayout.ysplit == 'above100hPa' ) : ylimitslist=[[ 100.,1.]] # hPa
            elif ( figlayout.ysplit == 'above150hPa' ) : ylimitslist=[[ 150.,1.]] # hPa
            elif ( figlayout.ysplit == 'above200hPa' ) : ylimitslist=[[ 200.,1.]] # hPa
            elif ( figlayout.ysplit == '' )            : ylimitslist=[[1000.,20.]] # hPa 
            else                                       : quit()
#            plt.ylim([ymax,ymin])
          
#       absolute extremes
#        ngroup=len(ylimitslist)
#        y0=ylimitslist[0][0]
#        y1=ylimitslist[ngroup-1][1]
#        plt.ylim([y0,y1])


    elif ( verticalaxis == 'height' ) :

        desired_zunits='km'
        ax.set_ylabel('Height ['+desired_zunits+']')

        ylimitslist=[[0.,40.]] # 0-40 km
#        ylimitslist=[[0.,10.]] # 0-10 km
#        ylimitslist=[[0.,2.]]  # 0-2  km

    else :
         print('No verticalaxis recognized : '+verticalaxis)
         quit()

#   absolute extremes
    ngroup=len(ylimitslist)
    if ( figlayout.yrange != [-1.,-1.] ) :
        y0=figlayout.yrange[0]
        y1=figlayout.yrange[1]
    else :
        y0=ylimitslist[0][0]
        y1=ylimitslist[ngroup-1][1]

    plt.ylim([y0,y1])

#   HORIZONTAL AXIS : logarithmic/linear
    if ( figlayout.xtype == 'log' ) :
            ax.set_xscale('log')

#   IF NGROUP=2
    if ( ngroup == 2) : 
        ax2 = ax.twiny() # instantiate a second Axes that shares the same y-axis
        ax2.set_xlabel('['+getidlunits.getidlunits(units=getstandardunits.getstandardunits(units=newunits))+']') # use first experiment to obtain units)


#   INTIALISE csv file
    if ( figlayout.csvoutput == True ) :
        csvpath='/projects/NS9560K/users/olivie/csv'
        csvfile=csvpath+'/'+filename+'.csv'
        fcsv=open(csvfile,'w')
        fcsv.write('Experiment,Line,Height,'+var)  # title line
        fcsv.write('\n')
        fcsv.write(',,'+desired_zunits+','+getstandardunits.getstandardunits(units=newunits)) # line with units
        fcsv.write('\n')

#   LOOP OVER ALL EXPERIMENTS
    for iexpid in range(0,nexpid) : 
        print('iexpid : ', iexpid)    

#       modify units
        if ( datalist[iexpid]['zunits'] == 'Pa' and desired_zunits == 'hPa' ) : zfactor = 0.01
        elif ( datalist[iexpid]['zunits'] == 'm' and desired_zunits == 'km' ) : zfactor = 0.001       
        else :
            print('No zunits recognized : ', datalist[iexpid]['zunits'])
            quit()

#       plot only values that fall within y-axis range
        for igroup in range(ngroup) :  

            ymin=np.amin([ylimitslist[igroup][0],ylimitslist[igroup][1]])
            ymax=np.amax([ylimitslist[igroup][0],ylimitslist[igroup][1]])  

            iset = ( zfactor*datalist[iexpid]['zlist'] >= ymin ) * ( zfactor*datalist[iexpid]['zlist'] <= ymax ) # Array of True/False [True, True, True, ..., False]

            if ( igroup == 0 ) :                    

#               plot lines
                if ( legendlist[iexpid] == '' ) : ax.plot(factor * datalist[iexpid]['valuelist'][iset], zfactor*datalist[iexpid]['zlist'][iset],                           color=getcolor.getcolor(color=colorlist[iexpid],colorscheme=figlayout.colorscheme),linestyle=getlinestyle.getlinestyle(linestyle=linestylelist[iexpid]))
                else                            : ax.plot(factor * datalist[iexpid]['valuelist'][iset], zfactor*datalist[iexpid]['zlist'][iset], label=legendlist[iexpid], color=getcolor.getcolor(color=colorlist[iexpid],colorscheme=figlayout.colorscheme),linestyle=getlinestyle.getlinestyle(linestyle=linestylelist[iexpid]))
#
#               individual points
#                ax.scatter(factor * datalist[iexpid]['valuelist'][iset], zfactor*datalist[iexpid]['zlist'][iset], marker='o', color=getcolor.getcolor(color=colorlist[iexpid],colorscheme=figlayout.colorscheme), s=30)

            elif ( igroup == 1 ) : # always without legends
                    
                ax2.plot(factor * datalist[iexpid]['valuelist'][iset], zfactor*datalist[iexpid]['zlist'][iset],                           color=getcolor.getcolor(color=colorlist[iexpid],colorscheme=figlayout.colorscheme),linestyle=getlinestyle.getlinestyle(linestyle=linestylelist[iexpid]))
#
#       write to csv-file
        if ( figlayout.csvoutput == True ) :
            for iiset in range(len(iset)) :
                if ( iset[iiset] == True ) : 
                    print('iset = ',iset)
                    print('iiset = ',iiset)

                    fcsv.write(experimentdefinition.getexpidinfo(expid=datalist[iexpid]['expid'])['model'])
                    fcsv.write(',')
                    fcsv.write(str(linestylelist[iexpid]))
                    fcsv.write(',')
                    fcsv.write(str(zfactor*datalist[iexpid][    'zlist'][iiset]))
                    fcsv.write(',')
                    fcsv.write(str( factor*datalist[iexpid]['valuelist'][iiset]))
                    fcsv.write('\n')


#   close csv file
    if ( figlayout.csvoutput == True ) :
        fcsv.close()

#   PLOT X- AND Y-AXIS
#   ax.axhline(0,lw=1.0,color='tab:gray',linestyle='dashed') # not needed
    if ( figlayout.axvline != None ) : 
        for axvlinepos in axvline :
            if ( var != 'T' ) : ax.axvline(axvlinepos,lw=1.0,color='tab:gray',linestyle='dashed')
            
#    ax.legend() # fontsize=5
    ax.legend(fontsize=5)
#    ax.legend(fontsize=7)

#    timestamp=str("%4.4i"% (year0))+'-'+str("%4.4i"% (year1))+'-'+season
#
    print('*** plotglobalmeanprofile ***')
#
    path='/projects/NS2345K/www/people/olivie/plots'
    path='/projects/NS9560K/users/olivie/plots'
#   path='/datalake/NS2345K/olivie/plots'
#
#    fig.savefig(path+'/globalmeanprofile_'+var+'_'+timestamp+'_'+region+'_'+verticalaxis+figlayout.code+figlayout.ysplit+'_'+code+'.ps',  bbox_inches='tight')
#    fig.savefig(path+'/globalmeanprofile_'+var+'_'+timestamp+'_'+region+'_'+verticalaxis+figlayout.code+figlayout.ysplit+'_'+code+'.png', bbox_inches='tight')
    fig.savefig(path+'/'+filename+'.ps',  bbox_inches='tight')
    fig.savefig(path+'/'+filename+'.png', bbox_inches='tight')
#
    plt.close(fig)


#   #       2024-11-14 : commented out
#        vlen=len(datalist[iexpid]['valuelist'])      
#        zlen=len(datalist[iexpid]['zlist'])

#        minlen=np.amin([vlen, zlen])
#       if ( legendlist[iexpid] == '' ) : ax.plot(factor * datalist[iexpid]['valuelist'][0:minlen], zfactor*datalist[iexpid]['zlist'][0:minlen],                           color=getcolor.getcolor(color=colorlist[iexpid],colorscheme=figlayout.colorscheme),linestyle=getlinestyle.getlinestyle(linestyle=linestylelist[iexpid]))
#       else                            : ax.plot(factor * datalist[iexpid]['valuelist'][0:minlen], zfactor*datalist[iexpid]['zlist'][0:minlen], label=legendlist[iexpid], color=getcolor.getcolor(color=colorlist[iexpid],colorscheme=figlayout.colorscheme),linestyle=getlinestyle.getlinestyle(linestyle=linestylelist[iexpid]))







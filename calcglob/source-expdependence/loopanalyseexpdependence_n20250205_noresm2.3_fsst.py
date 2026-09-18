import loopanalyseexpdependence2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


generaldescription='varcommon-typevarcommon'
generalcode='n20250205_noresm2.3'

#figlayout=cfiglayout.CFigLayout()

grouplist=['freerun_hetfrz0.001','freerun_hetfrz1.0','nudged_hetfrz0.001','nudged_hetfrz1.0']

for group in grouplist :

    if ( group == 'freerun_hetfrz0.001' ) :
        # free-running hetfrz0.001 
        list2014=['NF1850norbc_aer2014_f19_f19_20241127_test01', \
                  'NF1850norbc_aer2014_f19_f19_20241127_test09', \
                  'NF1850norbc_aer2014_f19_f19_20241127_test10', \
                  'NF1850norbc_aer2014_f19_f19_20241127_test05']
        list1850=['NF1850norbc_f19_f19_20241127_test01', \
                  'NF1850norbc_f19_f19_20241127_test09', \
                  'NF1850norbc_f19_f19_20241127_test10', \
                  'NF1850norbc_f19_f19_20241127_test05']
        expyear0list=[ 5, 5, 5, 5]
        expyear1list=[30,30,30,30]
    elif ( group == 'freerun_hetfrz1.0' ) :
        # free-running hetfrz1.000
        list2014=['NF1850norbc_aer2014_f19_f19_20241127_test14', \
                  'NF1850norbc_aer2014_f19_f19_20241127_test15', \
                  'NF1850norbc_aer2014_f19_f19_20241127_test16', \
                  'NF1850norbc_aer2014_f19_f19_20241127_test17']
        list1850=['NF1850norbc_f19_f19_20241127_test14', \
                  'NF1850norbc_f19_f19_20241127_test15', \
                  'NF1850norbc_f19_f19_20241127_test16', \
                  'NF1850norbc_f19_f19_20241127_test17']
        expyear0list=[ 5, 5, 5, 5]
        expyear1list=[30,30,30,30]
    elif ( group == 'nudged_hetfrz0.001' ) :
        # nudged hetfrz0.001 
        list2014=['NF1850norbc_sdyn_aer2014_f19_f19_20241127_test01', \
                  'NF1850norbc_sdyn_aer2014_f19_f19_20241127_test09', \
                  'NF1850norbc_sdyn_aer2014_f19_f19_20241127_test10', \
                  'NF1850norbc_sdyn_aer2014_f19_f19_20241127_test05']
        list1850=['NF1850norbc_sdyn_f19_f19_20241127_test01', \
                  'NF1850norbc_sdyn_f19_f19_20241127_test09', \
                  'NF1850norbc_sdyn_f19_f19_20241127_test10', \
                  'NF1850norbc_sdyn_f19_f19_20241127_test05']
        expyear0list=[1971,1971,1971,1971]
        expyear1list=[1974,1974,1974,1974]
    elif ( group == 'nudged_hetfrz1.0' ) :
        # nudged hetfrz1.000
        list2014=['NF1850norbc_sdyn_aer2014_f19_f19_20241127_test14', \
                  'NF1850norbc_sdyn_aer2014_f19_f19_20241127_test15', \
                  'NF1850norbc_sdyn_aer2014_f19_f19_20241127_test16', \
                  'NF1850norbc_sdyn_aer2014_f19_f19_20241127_test17']
        list1850=['NF1850norbc_sdyn_f19_f19_20241127_test14', \
                  'NF1850norbc_sdyn_f19_f19_20241127_test15', \
                  'NF1850norbc_sdyn_f19_f19_20241127_test16', \
                  'NF1850norbc_sdyn_f19_f19_20241127_test17']
        expyear0list=[1971,1971,1971,1971]
        expyear1list=[1974,1974,1974,1974]
    else :
        print('No group recoginzed : ', group)
        quit()


    refyear0list=expyear0list
    refyear1list=expyear1list
    seasonlist=['YEA','YEA','YEA','YEA']
#
#   1. DIFFERENCE VALUES
#----------------------------------
#   x-axis
    expidlist=list2014
    refidlist=list1850
    wlist=[1.,-1.]
#
    xvaluelist=[0.005,0.0125,0.025,0.05]
    xtitle='SOA-yield'
    xunits=''

#   variables
    varlist=['FSLNT','SWCF','CDNUMC','CCN1_columnburden','CCN2_columnburden','CCN3_columnburden','CCN4_columnburden','CCN5_columnburden','CCN6_columnburden','CCN7_columnburden']
    typevarlist=['glob']
    legendlist=['']
    colorlist=[0]
    linestylelist=[0]
    description=generaldescription
# 
    code=generalcode+'_'+group+'_diff'
#
    figlayout=cfiglayout.CFigLayout()
#
    loopanalyseexpdependence2.loopanalyseexpdependence2(\
        expidlist=expidlist,refidlist=refidlist, \
        expyear0list=expyear0list,expyear1list=expyear1list,refyear0list=refyear0list,refyear1list=refyear1list,seasonlist=seasonlist, \
        wlist=wlist, \
        varlist=varlist,typevarlist=typevarlist,legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist, \
        xvaluelist=xvaluelist, xtitle=xtitle, xunits=xunits, \
        description=description,code=code,figlayout=figlayout)
#
#   2. ABSOLUTE VALUES IN 1850
#-----------------------------
#   x-axis
    expidlist=list1850
    refidlist=expidlist
    wlist=[1.,0.]
#
    xvaluelist=[0.005,0.0125,0.025,0.05]
    xtitle='SOA-yield'
    xunits=''
#
#   variables
    varlist=['FSLNT','SWCF','CDNUMC','CCN1_columnburden','CCN2_columnburden','CCN3_columnburden','CCN4_columnburden','CCN5_columnburden','CCN6_columnburden','CCN7_columnburden']
    typevarlist=['glob']
    legendlist=['']
    colorlist=[0]
    linestylelist=[0]
    description=generaldescription
# 
    code=generalcode+'_'+group+'_1850'
#
    figlayout=cfiglayout.CFigLayout()
#
    loopanalyseexpdependence2.loopanalyseexpdependence2(\
        expidlist=expidlist,refidlist=refidlist, \
        expyear0list=expyear0list,expyear1list=expyear1list,refyear0list=refyear0list,refyear1list=refyear1list,seasonlist=seasonlist, \
        wlist=wlist, \
        varlist=varlist,typevarlist=typevarlist,legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist, \
        xvaluelist=xvaluelist, xtitle=xtitle, xunits=xunits, \
        description=description,code=code,figlayout=figlayout)

#
#   2. ABSOLUTE VALUES IN 2014
#-----------------------------
#   x-axis
    expidlist=list2014
    refidlist=expidlist
    wlist=[1.,0.]
#
    xvaluelist=[0.005,0.0125,0.025,0.05]
    xtitle='SOA-yield'
    xunits=''
#
#   variables
    varlist=['FSLNT','SWCF','CDNUMC','CCN1_columnburden','CCN2_columnburden','CCN3_columnburden','CCN4_columnburden','CCN5_columnburden','CCN6_columnburden','CCN7_columnburden']
    typevarlist=['glob']
    legendlist=['']
    colorlist=[0]
    linestylelist=[0]
    description=generaldescription
# 
    code=generalcode+'_'+group+'_2014'
#
    figlayout=cfiglayout.CFigLayout()
#
    loopanalyseexpdependence2.loopanalyseexpdependence2(\
        expidlist=expidlist,refidlist=refidlist, \
        expyear0list=expyear0list,expyear1list=expyear1list,refyear0list=refyear0list,refyear1list=refyear1list,seasonlist=seasonlist, \
        wlist=wlist, \
        varlist=varlist,typevarlist=typevarlist,legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist, \
        xvaluelist=xvaluelist, xtitle=xtitle, xunits=xunits, \
        description=description,code=code,figlayout=figlayout)

#   3. ABSOLUTE VALUES
#-------------------
#   x-axis
    expidlist=list1850
    refidlist=expidlist
    wlist=[1.,0.]
#
    xvaluelist=[0.005,0.0125,0.025,0.05]
    xtitle='SOA-yield'
    xunits=''
#
# variables
    varlist=['CCN1_columnburden','CCN2_columnburden','CCN3_columnburden','CCN4_columnburden','CCN5_columnburden','CCN6_columnburden','CCN7_columnburden']
    typevarlist=['glob']
    legendlist=['0.02 %','0.05 %','0.1 %','0.15 %','0.2 %','0.5 %','1.0 %']
    colorlist=[0,1,2,3,4,5,6]
    linestylelist=[0,1,2,3,4,5,6]
    description='typevarcommon'
# 
#
    code=generalcode+'_'+group
#
    figlayout=cfiglayout.CFigLayout(ytype='log')
#
    loopanalyseexpdependence2.loopanalyseexpdependence2(\
        expidlist=expidlist,refidlist=refidlist, \
        expyear0list=expyear0list,expyear1list=expyear1list,refyear0list=refyear0list,refyear1list=refyear1list,seasonlist=seasonlist, \
        wlist=wlist, \
        varlist=varlist,typevarlist=typevarlist,legendlist=legendlist,colorlist=colorlist,linestylelist=linestylelist, \
        xvaluelist=xvaluelist, xtitle=xtitle, xunits=xunits, \
        description=description,code=code,figlayout=figlayout)



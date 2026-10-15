import loopanalyseseries2
import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout


figlayout=cfiglayout.CFigLayout(xrange=[1850,2100])


# GLOBAL MEAN : f09 and f19 together
#-----------------------------------
#
expidlist=[ \
            'NHIST_123_f19_tn14_20190625ext', \
            'NHISTfrc2_123_f09_tn14_20191001ext', \

            'NSSP126frc2_f19_tn14_20191014', \
            'NSSP245frc2_123_f19_tn14_20191014', \
            'NSSP370frc2_123_f19_tn14_20191014', \
            'NSSP585frc2_f19_tn14_20191014', \

            'NSSP126frc2_f09_tn14_20191105', \
            'NSSP245frc2_f09_tn14_20191105', \
            'NSSP370frc2_f09_tn14_20191105', \
            'NSSP585frc2_f09_tn14_20191105']
#
legendlist=['','','ssp1-2.6', \
                  'ssp2-4.5', \
                  'ssp3-7.0', \
                  'ssp5-8.5', \
                  '','','','']
#
refidlist=expidlist # become 1 object
#
wlist=[1.,0.]
#
smoothlist=[0,0, 0,0,0,0, 0,0,0,0]
shiftlist=[0,0, 0,0,0,0, 0,0,0,0]
colorlist     =   [0,0, 1,2,3,4, 1,2,3,4]
linestylelist =   [0,2, 0,0,0,0, 2,2,2,2]
linewidthlist =   [1,1, 1,1,1,1, 1,1,1,1]
ensembletypelist = ['minmax','minmax', \
                    '','minmax','minmax', '', \
                    '','','','']
#
# 
description='typevarcommon-varcommon'
variablelist=[\
              'ICEFRAC_as_fraction']  
typevarlist=['NH','73N90N7W49E','73N90N7W49ESEA','60N90NSEA']
freqtypelist=['YEA','SEP','MAR']
#
code='n20260917_noresm2_erik'
#
for freqtype in freqtypelist :
#
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist,ensembletypelist=ensembletypelist)

# GLOBAL MEAN : f19 alone
#-----------------------------------
#
expidlist=[ \
            'NHIST_123_f19_tn14_20190625ext', \
            \
            'NSSP126frc2_f19_tn14_20191014', \
            'NSSP245frc2_123_f19_tn14_20191014', \
            'NSSP370frc2_123_f19_tn14_20191014', \
            'NSSP585frc2_f19_tn14_20191014']
#
legendlist=['','ssp1-2.6', \
               'ssp2-4.5', \
               'ssp3-7.0', \
               'ssp5-8.5']
#
refidlist=expidlist # become 1 object
#
wlist=[1.,0.]
#
smoothlist=[0, 0,0,0,0]
shiftlist=[0, 0,0,0,0]
colorlist     =   [0, 1,2,3,4]
linestylelist =   [0, 0,0,0,0]
linewidthlist =   [1, 1,1,1,1]
ensembletypelist = ['minmax', \
                    '','minmax','minmax', '']
#
# 
description='typevarcommon-varcommon'
variablelist=[\
              'ICEFRAC_as_fraction']  
typevarlist=['NH','73N90N7W49E','73N90N7W49ESEA','60N90NSEA']
freqtypelist=['YEA','SEP','MAR']
#
code='n20260917_noresm2_erik_f19'
#
for freqtype in freqtypelist :
#
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist,ensembletypelist=ensembletypelist)

# GLOBAL MEAN : f09 alone
#-----------------------------------
#
expidlist=[ \
            'NHISTfrc2_123_f09_tn14_20191001ext', \
            \
            'NSSP126frc2_f09_tn14_20191105', \
            'NSSP245frc2_f09_tn14_20191105', \
            'NSSP370frc2_f09_tn14_20191105', \
            'NSSP585frc2_f09_tn14_20191105']
#
legendlist=['','ssp1-2.6', \
               'ssp2-4.5', \
               'ssp3-7.0', \
               'ssp5-8.5']
#
refidlist=expidlist # become 1 object
#
wlist=[1.,0.]
#
smoothlist=[0, 0,0,0,0]
shiftlist=[0, 0,0,0,0]
colorlist     =   [0, 1,2,3,4]
linestylelist =   [0, 0,0,0,0]
linewidthlist =   [1, 1,1,1,1]
ensembletypelist = ['minmax', \
                    '','','','']
#
# 
description='typevarcommon-varcommon'
variablelist=[\
              'ICEFRAC_as_fraction']  
typevarlist=['NH','73N90N7W49E','73N90N7W49ESEA','60N90NSEA']
freqtypelist=['YEA','SEP','MAR']
#
code='n20260917_noresm2_erik_f09'
#
for freqtype in freqtypelist :
#
    loopanalyseseries2.loopanalyseseries2(expidlist=expidlist,refidlist=refidlist,wlist=wlist,legendlist=legendlist,shiftlist=shiftlist,smoothlist=smoothlist,variablelist=variablelist,typevarlist=typevarlist,freqtype=freqtype,description=description,code=code,figlayout=figlayout,colorlist=colorlist,linestylelist=linestylelist,linewidthlist=linewidthlist,ensembletypelist=ensembletypelist)

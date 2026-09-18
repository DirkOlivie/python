import mosaicanalyseseriesloop2

import sys
sys.path.insert(0,'/nird/home/olivie/code/python/routines/source')
import cfiglayout

'''
    CALLS
        mosaicanalyseloop2

'''

# expidlist
expidlist=[ \
           'N1850frc2esm_IMPOSE_C1a_23_f19_tn14_20200316pre', \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_123_f19_tn14_20250730pre', \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens123apre', \
           'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens123apre']

# refidlist
refidlist=['N1850_f19_tn14_20190730esm', \
           'N1850_f19_tn14_20190730esm', \
           'N1850_f19_tn14_20190730esm', \
           'N1850_f19_tn14_20190730esm']

nexpid=len(expidlist)

dorefaverage=True
#
wlist=[1.,-1.]

ensembletypelist=['minmax','minmax','minmax','minmax']
ensembletypelist=['smoothminmax','smoothminmax','smoothminmax','smoothminmax']
#
legendlist=['CDR', \
            'CDR+SAI(TR)', \
            'CDR+SAI(NH)', \
            'CDR+SAI(SH)']
#
smoothlist=[5,5,5,5]
colorlist=[7,1,2,0] # [7,3,2,0]
linestylelist=[0,0,0,0]
shiftlist=[-1849,-1849,-1849,-1849]
#
freqtype='YEA'
#
# atmosphere
code='n20260413_navigate_esm_trnhsh_ref'
variablelist=['PRECCPRECL']*nexpid

#############
# 1. Six panels : Global, Tropics. NH,
##############

# figlayout
figlayout0=cfiglayout.CFigLayout(axhline=[0], axvline=[100,200], axvlinestyle='dotted', xrange=[0,400], xlabel='year', title='(a) Global')
figlayout1=cfiglayout.CFigLayout(axhline=[0], axvline=[100,200], axvlinestyle='dotted', xrange=[0,400], xlabel='year', title='(b) Tropics')
figlayout2=cfiglayout.CFigLayout(axhline=[0], axvline=[100,200], axvlinestyle='dotted', xrange=[0,400], xlabel='year', title='(c) Northern hemisphere')
figlayout3=cfiglayout.CFigLayout(axhline=[0], axvline=[100,200], axvlinestyle='dotted', xrange=[0,400], xlabel='year', title='(d) Southern hemisphere')
figlayout4=cfiglayout.CFigLayout(axhline=[0], axvline=[100,200], axvlinestyle='dotted', xrange=[0,400], xlabel='year', title='(e) Land')
figlayout5=cfiglayout.CFigLayout(axhline=[0], axvline=[100,200], axvlinestyle='dotted', xrange=[0,400], xlabel='year', title='(f) Ocean')

ncol=2
code='ALL'
suptitle='' # 'Precipitation change'
expiddescriptionlist=[\
#                     global
                      {'expidlist'        : expidlist, \
                       'refidlist'        : refidlist, \
                       'wlist'            : [1.,-1], \
                       'legendlist'       : legendlist, \
                       'shiftlist'        : shiftlist, \
                       'smoothlist'       : smoothlist, \
                       'variablelist'     : variablelist, \
                       'typevarlist'      : ['glob']*nexpid, \
                       'freqtype'         : freqtype, \
                       'dorefaverage'     : dorefaverage, \
                       'colorlist'        : colorlist, \
                       'linestylelist'    : linestylelist, \
                       'ensembletypelist' : ensembletypelist, \
                       'title'            : '(a) Global', \
                       'figlayout'        : figlayout0}, \
#                     28S28N
                      {'expidlist'        : expidlist, \
                       'refidlist'        : refidlist, \
                       'wlist'            : [1.,-1], \
                       'legendlist'       : legendlist, \
                       'shiftlist'        : shiftlist, \
                       'smoothlist'       : smoothlist, \
                       'variablelist'     : variablelist, \
                       'typevarlist'      : ['28S28N']*nexpid, \
                       'freqtype'         : freqtype, \
                       'dorefaverage'     : dorefaverage, \
                       'colorlist'        : colorlist, \
                       'linestylelist'    : linestylelist, \
                       'ensembletypelist' : ensembletypelist, \
                       'title'            : '(b) Tropics', \
                       'figlayout'        : figlayout1}, \
#                     NH
                      {'expidlist'        : expidlist, \
                       'refidlist'        : refidlist, \
                       'wlist'            : [1.,-1], \
                       'legendlist'       : legendlist, \
                       'shiftlist'        : shiftlist, \
                       'smoothlist'       : smoothlist, \
                       'variablelist'     : variablelist, \
                       'typevarlist'      : ['NH']*nexpid, \
                       'freqtype'         : freqtype, \
                       'dorefaverage'     : dorefaverage, \
                       'colorlist'        : colorlist, \
                       'linestylelist'    : linestylelist, \
                       'ensembletypelist' : ensembletypelist, \
                       'title'            : '(c) Northern hemisphere', \
                       'figlayout'        : figlayout2}, \
#                     SH
                      {'expidlist'        : expidlist, \
                       'refidlist'        : refidlist, \
                       'wlist'            : [1.,-1], \
                       'legendlist'       : legendlist, \
                       'shiftlist'        : shiftlist, \
                       'smoothlist'       : smoothlist, \
                       'variablelist'     : variablelist, \
                       'typevarlist'      : ['SH']*nexpid, \
                       'freqtype'         : freqtype, \
                       'dorefaverage'     : dorefaverage, \
                       'colorlist'        : colorlist, \
                       'linestylelist'    : linestylelist, \
                       'ensembletypelist' : ensembletypelist, \
                       'title'            : '(d) Southern hemisphere', \
                       'figlayout'        : figlayout3}, \
#                     Land
                      {'expidlist'        : expidlist, \
                       'refidlist'        : refidlist, \
                       'wlist'            : [1.,-1], \
                       'legendlist'       : legendlist, \
                       'shiftlist'        : shiftlist, \
                       'smoothlist'       : smoothlist, \
                       'variablelist'     : variablelist, \
                       'typevarlist'      : ['LAND']*nexpid, \
                       'freqtype'         : freqtype, \
                       'dorefaverage'     : dorefaverage, \
                       'colorlist'        : colorlist, \
                       'linestylelist'    : linestylelist, \
                       'ensembletypelist' : ensembletypelist, \
                       'title'            : '(e) Land', \
                       'figlayout'        : figlayout4}, \
#                     Ocean
                      {'expidlist'        : expidlist, \
                       'refidlist'        : refidlist, \
                       'wlist'            : [1.,-1], \
                       'legendlist'       : legendlist, \
                       'shiftlist'        : shiftlist, \
                       'smoothlist'       : smoothlist, \
                       'variablelist'     : variablelist, \
                       'typevarlist'      : ['SEA']*nexpid, \
                       'freqtype'         : freqtype, \
                       'dorefaverage'     : dorefaverage, \
                       'colorlist'        : colorlist, \
                       'linestylelist'    : linestylelist, \
                       'ensembletypelist' : ensembletypelist, \
                       'title'            : '(f) Ocean', \
                       'figlayout'        : figlayout5}] 

mosaicanalyseseriesloop2.mosaicanalyseseriesloop2(expiddescriptionlist=expiddescriptionlist, suptitle=suptitle, code=code, ncol=ncol)


#############
# 2. One panels : Global, Tropics. NH,
##############

# figlayout
figlayout=cfiglayout.CFigLayout(axhline=[0], axvline=[100,200], title='Global')

ncol=1
code='GLOB'
suptitle='' # 'Precipitation change'
expiddescriptionlist=[\
#                     global
                      {'expidlist'        : expidlist, \
                       'refidlist'        : refidlist, \
                       'wlist'            : [1.,-1], \
                       'legendlist'       : legendlist, \
                       'shiftlist'        : shiftlist, \
                       'smoothlist'       : smoothlist, \
                       'variablelist'     : variablelist, \
                       'typevarlist'      : ['glob']*nexpid, \
                       'freqtype'         : freqtype, \
                       'dorefaverage'     : dorefaverage, \
                       'colorlist'        : colorlist, \
                       'linestylelist'    : linestylelist, \
                       'ensembletypelist' : ensembletypelist, \
                       'title'            : '(a) Global', \
                       'figlayout'        : figlayout}]

mosaicanalyseseriesloop2.mosaicanalyseseriesloop2(expiddescriptionlist=expiddescriptionlist, suptitle=suptitle, code=code, ncol=ncol)






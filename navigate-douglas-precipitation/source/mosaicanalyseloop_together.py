import mosaicanalyseloop2

'''
    CALLS
        mosaicanalyseloop2

'''

var='PRECT'
code='ALL'
suptitle='' # 'Precipitation change'
addcolorbar=1
expiddescriptionlist=[\
#                     year 81-100
                      {'expid':'N1850frc2esm_ZECMIP_B3_123_f19_tn14_20200316', \
                       'refid':'N1850_f19_tn14_20190730esm', \
                       'wlist':[1.,-1], \
                       'year0':1930, \
                       'year1':1949, \
                       'season':'YEA', \
                       'legend' : '(a) CDR (years 81-100)'}, \
#                     year 181-200   
                      {'expid':'N1850frc2esm_IMPOSE_C1a_123_f19_tn14_20200316', \
                       'refid':'N1850_f19_tn14_20190730esm', \
                       'wlist':[1.,-1], \
                       'year0':2030, \
                       'year1':2049, \
                       'season':'YEA', \
                       'legend' : '(b) CDR (years 181-200)'}, \
#                     tropical
#                     year 81-100
                      {'expid':'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_123_f19_tn14_20250721', \
                       'refid':'N1850_f19_tn14_20190730esm', \
                       'wlist':[1.,-1], \
                       'year0':1930, \
                       'year1':1949, \
                       'season':'YEA', \
                       'legend' : '(c) CDR + SAI(TR) (years 81-100)'}, \
#                     year 181-200
                      {'expid':'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_123_f19_tn14_20250730', \
                       'refid':'N1850_f19_tn14_20190730esm', \
                       'wlist':[1.,-1], \
                       'year0':2030, \
                       'year1':2049, \
                       'season':'YEA', \
                       'legend' : '(d) CDR + SAI(TR) (years 181-200)'}, \
#                     NH
#                     year 81-100
                      {'expid':'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens123', \
                       'refid':'N1850_f19_tn14_20190730esm', \
                       'wlist':[1.,-1], \
                       'year0':1930, \
                       'year1':1949, \
                       'season':'YEA', \
                       'legend' : '(e) CDR + SAI(NH) (years 81-100)'}, \
#                     year 181-200
                      {'expid':'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15n60n_f19_tn14_20251022_ens123a', \
                       'refid':'N1850_f19_tn14_20190730esm', \
                       'wlist':[1.,-1], \
                       'year0':2030, \
                       'year1':2049, \
                       'season':'YEA', \
                       'legend' : '(f) CDR + SAI(NH) (years 181-200)'}, \
#                     SH 
#                     year 81-100
                      {'expid':'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251112_ens123', \
                       'refid':'N1850_f19_tn14_20190730esm', \
                       'wlist':[1.,-1], \
                       'year0':1930, \
                       'year1':1949, \
                       'season':'YEA', \
                       'legend' : '(g) CDR + SAI(SH) (years 81-100)'}, \
#                     year 181-200
                      {'expid':'N1850frc2esm_B3C1atoB4_cutoff2009_1.5TgSperRF_15s60s_f19_tn14_20251118_ens123a', \
                       'refid':'N1850_f19_tn14_20190730esm', \
                       'wlist':[1.,-1], \
                       'year0':2030, \
                       'year1':2049, \
                       'season':'YEA', \
                       'legend' : '(h) CDR + SAI(SH) (years 181-200)'}]
mosaicanalyseloop2.mosaicanalyseloop2(expiddescriptionlist=expiddescriptionlist, var=var, suptitle=suptitle, addcolorbar=addcolorbar, code=code)

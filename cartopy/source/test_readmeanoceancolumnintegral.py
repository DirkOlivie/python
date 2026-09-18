import readmeanoceancolumnintegral

expid='N1850_f19_tn14_20231204_test02'
var='templvl'
#date='1600-12'
year0=1600
year1=1600
season='DEC'


a=readmeanoceancolumnintegral.readmeanoceancolumnintegral(expid=expid, var=var, year0=year0, year1=year1, season=season)

print(a['field'][:,180])
#print(a['field'][:,50,1])
#print(a['field'][:,50,2])

#print('LATITUDE')
#print(a['x'])
#print('ALTITUDE')
#print(a['y'])
#print('FIELD')
#print(a['z'])

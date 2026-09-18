import readsinglezonalmean

expid='NF1850norbc_f19_20191025'
var='OH'
date='0001-12'

a=readsinglezonalmean.readsinglezonalmean(expid=expid, var=var, date=date)

#print(a['field'][:,50,0])
#print(a['field'][:,50,1])
#print(a['field'][:,50,2])

print('LATITUDE')
print(a['x'])
print('ALTITUDE')
print(a['y'])
print('FIELD')
print(a['z'])

import getexternalfield

expid='NF1850norbc_f19_20191025'
var='OH'
date='0001-12'

a=getexternalfield.getexternalfield(expid=expid, var=var, date=date)

print(a['field'][:,50,0])
print(a['field'][:,50,1])
print(a['field'][:,50,2])

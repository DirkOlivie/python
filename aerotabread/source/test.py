import readaerotable

a=readaerotable.readaerotable(version='AeroTab_8jun17', shortfilename='kcomp1.out')
a=readaerotable.readaerotable(version='AeroTab_8jun17', shortfilename='kcomp5.out')

print(a['ndim'])
print(a['dimsizelist'])
print(a['dimnamelist'])
print(a['xvaluelist'])

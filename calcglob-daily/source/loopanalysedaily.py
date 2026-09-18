import loopanalysedaily2

#datelist=[             '0018-01-02','0018-01-03','0018-01-04','0018-01-05','0018-01-06','0018-01-07','0018-01-08','0018-01-09','0018-01-10', \
#          '0018-01-11','0018-01-12','0018-01-13','0018-01-14','0018-01-15','0018-01-16','0018-01-17','0018-01-18','0018-01-19','0018-01-20', \
#          '0018-01-21','0018-01-22','0018-01-23','0018-01-24','0018-01-25','0018-01-26','0018-01-27','0018-01-28','0018-01-29','0018-01-30', \
#          '0018-01-31', \
#          '0018-02-01','0018-02-02','0018-02-03','0018-02-04','0018-02-05','0018-02-06','0018-02-07','0018-02-08','0018-02-09','0018-02-10', \
#          '0018-02-11','0018-02-12','0018-02-13','0018-02-14','0018-02-15','0018-02-16','0018-02-17','0018-02-18','0018-02-19','0018-02-20', \
#          '0018-02-21','0018-02-22','0018-02-23','0018-02-24','0018-02-25','0018-02-26','0018-02-27','0018-02-28', \
#          '0018-03-01','0018-03-02','0018-03-03','0018-03-04','0018-03-05','0018-03-06','0018-03-07','0018-03-08','0018-03-09','0018-03-10', \
#          '0018-03-11','0018-03-12','0018-03-13','0018-03-14','0018-03-15','0018-03-16','0018-03-17','0018-03-18','0018-03-19','0018-03-20', \
#          '0018-03-21','0018-03-22','0018-03-23']

# TOMAS SIMULATION
date0='0018-01-02'
date1='0018-03-23'
calendar='no_leap'

varlist=['TREFHT','cb_BC_AX','cb_BC','FSDS','FSDSC','AODVISdivDAYFOC']
#varlist=['FSDSC']
#varlist=['FLNT','FSNT','FLNT','FSNT','FLNT','FSNT','FLNT']
expid='n1850.ne30_tn14.noresm3_0_alpha03d.20250528_branch6'
directory='/nird/datalake/NS2345K/olivie/noresm/cases-group/noresm2.5-test'

code='branch6'

#loopanalysedaily2.loopanalysedaily2(varlist=varlist, expid=expid, directory=directory, date0=date0, date1=date1, calendar=calendar, code=code)

# GHG2 SIMULATION
date0='0003-01-02'
date1='0004-01-01'
calendar='no_leap'

varlist=['cb_BC']
expid='n1850.ne30_tn14.hybrid_fates-nocomp.3.0a03d.20250605_ghg2'
#directory='/nird/datalake/NS2345K/olivie/noresm/cases-group/noresm2.5-test'
directory='/nird/datalake/NS9560K/noresm3/cases'

code='ghg2'

#loopanalysedaily2.loopanalysedaily2(varlist=varlist, expid=expid, directory=directory, date0=date0, date1=date1, calendar=calendar, code=code)

# MOVMTN
date0='0002-01-01'
date1='0007-04-01'
calendar='no_leap'

varlist=['cb_BC_AX']
expid='n1850.ne30_tn14.noresm3_0_alpha03d.20250528_movmtn'
directory='/nird/datalake/NS2345K/olivie/noresm/cases-group/noresm2.5-test'

code='movmtn'

#loopanalysedaily2.loopanalysedaily2(varlist=varlist, expid=expid, directory=directory, date0=date0, date1=date1, calendar=calendar, code=code)


# NO BC_AX
date0='0001-04-02'
date1='0005-05-25'
calendar='no_leap'

varlist=['cb_BC_AX']
expid='n1850.ne30_tn14.noresm3_0_alpha03d.20250528_nobcax'
directory='/nird/datalake/NS2345K/olivie/noresm/cases-group/noresm2.5-test'

code='nobcax'

loopanalysedaily2.loopanalysedaily2(varlist=varlist, expid=expid, directory=directory, date0=date0, date1=date1, calendar=calendar, code=code)



#!/Users/jblue/anaconda2/bin/python
import random
import numpy
import math

## set number of accounts & fraud pct ##
accounts=100000    ### total number of frauds
fraud_rate=0.05  ### pct of accounts will be tagged as fraud
trans_rate=0.1  ### pct of days that should have a transaction
days=100        ### how many days of 'history'

### output file names ###
modeling='model.csv'  ### this is where the modeling dataset will be written ###

###########################################
########  TRANSACTION DATA ################
###########################################
transDB = {}
fraudDB = []
for i in range(0,accounts):
  ### generate transactions ###
  transDB[i]={}
  trans = random.sample(range(days+1),numpy.random.poisson(int(trans_rate*days)))
  for a in trans:
	transDB[i][a]=round(100*numpy.random.exponential(),2)
	
  ### create fraud tag ###
  if random.random()<fraud_rate:
	fraudDB.append(i)
  	fTrans = random.sample(range(days+1),numpy.random.poisson(int(trans_rate*days)))
  	for b in fTrans:
	  transDB[i][b]=round(100*numpy.random.exponential(),2)
	

###########################################
###########  MODELING DATA ################
###########################################
### format: ACCT ID,TAG,DSLT
### DSLT = days since last transaction
f = open(modeling, 'w')
for x in transDB:
  fraud=0
  if x in fraudDB: fraud=1
  sortDays =  sorted(transDB[x],reverse=True)
  if len(sortDays)>1: dslt = math.log(sortDays[0]-sortDays[1])
  else: dslt = 0.0
  f.write(str(x)+","+str(fraud)+","+str(dslt)+'\n')

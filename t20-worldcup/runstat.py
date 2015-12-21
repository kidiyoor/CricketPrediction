f = input("1. Cluster no or \n2. Batsman name\n")


bat = open('batCluster.tsv','r')
bowl = open('bowlCluster.tsv','r')

dbat = {}
dbowl = {}

for i in bat.readlines():
	d = i.split(",")
	for i in d[1:]:
		dbat[i.strip()] = d[0]

for i in bowl.readlines():
	d = i.split(",")
	for i in d[1:]:
		dbowl[i.strip()] = d[0]



if f == 1 :
	a = input("batsman cluster : ")
	b = input("bowler cluster : ")
else:
	aa = input("Batsman name : ")
	bb = input("Bowler name : ")
	a = dbat[aa]
	b = dbat[bb]


import os
os.chdir('clusteredData')
f = open(str(a)+":"+str(b), 'r')

a0 = 0
a1 = 0
a2 = 0
a3 = 0
a4 = 0
a6 = 0

tballs = 0

for i in f:
	d = i.split(",")
	if d[3] == '1':
		a1 = a1 + 1
	elif d[3] == '2':
		a2 = a2 + 1
	elif d[3] == '3':
		a3 = a3 + 1
	elif d[3] == '4':
		a4 = a4 + 1
	elif d[3] == '6':
		a6 = a6 + 1
	elif d[3] == '0':
		a0 = a0 + 1
	tballs = tballs +1
print('''
	Probability of 0 : %s
	Probability of 6 : %s
	Probability of 4 : %s
	Probability of 3 : %s
	Probability of 2 : %s
	Probability of 1 : %s
	'''%((float(a0)/tballs),float(a6)/tballs,float(a4)/tballs,float(a3)/tballs,float(a2)/tballs,float(a1)/tballs))
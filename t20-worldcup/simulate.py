import os
import yaml

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




def maxamg(p0,p1,p2,p3,p4,p6):
	m = p0
	out = 0
	if p1 > m :
		out = 1
		m = p1
	if p2 > m :
		out = 2
		m = p1
	if p3 > m :
		out = 3
		m = p1
	if p4 > m :
		out = 4
		m = p1
	if p6 > m :
		out = 6
		m = p1
	return out


data = yaml.load(open('sample.txt','r').read())
count = 0
trun = 0
for row in data['data1']:
	count = count + 1
	a = dbat[row['batsman']]
	b = dbowl[row['bowler']]

	f = open('clusteredData/'+str(a)+":"+str(b), 'r')

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
		
	a1 = a1 * 1
	a4 = a4 * 4
	a6 = a6 * 2	
	p0 = float(a0)/tballs
	p1 = float(a1)/tballs
	p2 = float(a2)/tballs
	p3 = float(a3)/tballs
	p4 = float(a4)/tballs
	p6 = float(a6)/tballs


	p = maxamg(p0,p1,p2,p3,p4,p6)
	trun = trun + p
	print("------------")
	print("Ball : " + str(count) )
	print("\nRun : " + str(p) + '\n' )
	print("------------")

print("---------------------------------------")
print("\n\t\t\tTarget  : " + str(trun))
print("---------------------------------------")

count = 0
trun = 0

for row in data['data2']:
	count = count + 1
	a = dbat[row['batsman']]
	b = dbowl[row['bowler']]

	f = open('clusteredData/'+str(a)+":"+str(b), 'r')

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
		
	a1 = a1 * 1
	a4 = a4 * 4
	a6 = a6 * 2	
	p0 = float(a0)/tballs
	p1 = float(a1)/tballs
	p2 = float(a2)/tballs
	p3 = float(a3)/tballs
	p4 = float(a4)/tballs
	p6 = float(a6)/tballs


	p = maxamg(p0,p1,p2,p3,p4,p6)
	trun = trun + p
	print("------------")
	print("Ball : " + str(count) )
	print("\nRun : " + str(p) + '\n' )
	print("------------")


print("---------------------------------------")
print("\n\t\t\tScore  : " + str(trun))
print("---------------------------------------")


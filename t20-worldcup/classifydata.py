f = open('newdata','r')
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


for i in f.readlines():
	d = i.split(",")
	a = dbat[d[0]]
	b = dbowl[d[1]]
	open(a+":"+b,'a+').write(i)
	



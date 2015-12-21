f = open('bowler.csv','r')

a = 'A Bhattarai'
out = open('bowlerClusterInput.csv','w')
s = ''
total = 0
a0 = 0
a1 = 0
a2 = 0
a3 = 0
a4 = 0
a6 = 0

def reset():
	global a0
	global a1
	global a2
	global a3
	global a4
	global a6
	
	a0 = 0
	a1 = 0
	a2 = 0
	a3 = 0
	a4 = 0
	a6 = 0


for i in f.readlines():

	d = i.split(",")
	
	d[0] = d[0].strip()
	d[1] = d[1].strip()
	
	if d[0] == a :
		if d[1] == '1':
			a1 = a1 + 1
		elif d[1] == '2':
			a2 = a2 + 1
		elif d[1] == '3':
			a3 = a3 + 1
		elif d[1] == '4':
			a4 = a4 + 1
		elif d[1] == '6':
			a6 = a6 + 1
		elif d[1] == '0':
			a0 = a0 + 1
		
		total = total + int(d[1])
		#write
	else:
		out.write(a+","+str(total)+","+str(a0)+","+str(a1)+","+str(a2)+","+str(a3)+","+str(a4)+","+str(a6)+"\n")
		a = d[0]
		reset()
		if d[1] == '1':
			a1 = a1 + 1
		elif d[1] == '2':
			a2 = a2 + 1
		elif d[1] == '3':
			a3 = a3 + 1
		elif d[1] == '4':
			a4 = a4 + 1
		elif d[1] == '6':
			a6 = a6 + 1
		elif d[1] == '0':
			a0 = a0 + 1


		total = int(d[1])
		
out.write(a+","+str(total)+","+str(a0)+","+str(a1)+","+str(a2)+","+str(a3)+","+str(a4)+","+str(a6)+"\n")
out.close()
f.close()
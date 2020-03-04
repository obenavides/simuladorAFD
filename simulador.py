d={
0:{'1':1},
1:{'1':2},
2:{'1':3},
3:{'1':1}
}

def AFD(d,q0,F,cinta):
	q=q0
	for simbolo in cinta:
		q=d[q][simbolo]
	return q in F

mensaje={True:'Aceptada',False:'Rechazada'}

for cinta in ['','1','11','111','1111','11111','111111']:
	print('La entrada',cinta," es ",mensaje[AFD(d,0,{3},cinta)])

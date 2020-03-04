d={
0:{'1':1},
1:{'1':2},
2:{'1':3},
3:{'1':1}
}

q=0
F={3}
for simbolo in '111111111':
	q=d[q][simbolo]
print(q in F)

#!/usr/bin/python3
# $which python3
# darle permiso de ejecucion: $chmod u+x simulador.py ; y correr como $./simulador.py
d={}
F=set()
programa=open('programa.txt')
for linea in programa:
    q,s,n=linea.split()
    if '*' in q:
        q=q.strip('*')
        F.add(q)
    d[q,s]=n
programa.close()

def AFD(d,q0,F,cinta):
    q=q0
    for simbolo in cinta:
        q=d[q,simbolo]
    return q in F

mensaje={True:'Aceptada',False:'Rechazada'}

cintas=open('cintas.txt')
for cinta in cintas:
    cinta=cinta.strip()
    print('La entrada',cinta," es ",mensaje[AFD(d,'0',F,cinta)])
cintas.close()

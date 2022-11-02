

#J# Riempi una lista di 10 numeri casuali (utilizza un ciclo for) e stampa solo i numeri pari
import random 
ultima = []
for x in range (10) :
    ultima.append(random.randrange(0,200))
for n in ultima :
    z = int(n/2)
    if (z*2)==n:
        print (n)
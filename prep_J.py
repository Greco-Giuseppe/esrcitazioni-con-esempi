#Riempi una lista di 10 numeri casuali (utilizza un ciclo for) e stampa solo i numeri pari
import random
lista = []

for x in range(10) :
    lista.append( random.randrange(0,100))
for y in lista :
    n = int (y/2)
    if (n*2)==y :
        print (y)

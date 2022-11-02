#Riempi una lista di 5 numeri e stampa il minore.
import random 
lista = []
for x in range (5) :
    lista.append(random.randrange(0,100))
for n in lista :
    print(n)
    print ("-")
y = lista [0]
for n in lista :
    if n < y :
        y=n 
print (y)

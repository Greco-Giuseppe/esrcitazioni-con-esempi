#C Chiedi all’utente di inserire 5 numeri e stampa solo i numeri pari in ordine inverso

lista = []

for x in range (5) : 
    n = int(input("dammi un numero: "))
    z = int(n/2)
    if (z*2)==n :
        lista.append(n)
lista.reverse()
print (lista)

     
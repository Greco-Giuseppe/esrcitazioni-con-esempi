#B Chiedi all’utente di inserire 5 numeri e stampa i numeri in ordine inverso
lista = []
for x in range (5) : 
    n = int(input("dammi un numero: "))
    lista.append(n)
lista.reverse()
print (lista)

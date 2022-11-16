#B Chiedi all’utente di inserire 5 numeri e stampa i numeri in ordine inverso
lista = []
for x in range (5) :
    lista.append(int(input("inserire un numero:" )))
lista.reverse()  # lista.sort() li ordina , lista.reverse() al contrario
print(lista)


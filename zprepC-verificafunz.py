#C Chiedi all’utente di inserire 5 numeri e stampa solo i numeri pari in ordine inverso

lista = []
for x in range (5) :
    lista.append(int(input("inserire un numero:" )))
lista.reverse()
for e in lista :
     z = int ( e/2 )
     if (z*2) == e :
          print (e)
     
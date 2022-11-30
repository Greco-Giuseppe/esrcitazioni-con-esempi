#B Chiedi all’utente di inserire 5 numeri e stampa i numeri in ordine inverso
gigio = []

for x in range(5) : 
    n = int(input("dammi un numero :"))
    gigio.append(n)
gigio.reverse()
print (gigio)

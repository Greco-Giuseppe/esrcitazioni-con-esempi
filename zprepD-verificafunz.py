#D Chiedi all’utente quanti numeri vuole inserire. Leggi tutti i numeri in input. Stampa tutti i numeri inseriti al quadrato


num=int(input("quanti numeri:"))
lista = []
for x in range (num) :
    y = int(input("immetti un numero:"))
    z = int(y*y)
    lista.append(z)
print(lista)
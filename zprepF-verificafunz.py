#Scrivi una funzione che, data una lista di numeri in input, 
#fornisce in output un istogramma basato su questi numeri, usando asterischi per disegnarlo.


num=int(input("quanti numeri:"))
lista = []
for x in range (num) :
    y = int(input("immetti un numero:"))
    lista.append(y)
 
def istogramma(lista) :
    for x in lista :
        print ("*"*x)
istogramma(lista)        
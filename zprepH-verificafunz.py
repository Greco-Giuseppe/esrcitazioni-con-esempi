lista = []
num=int(input("quanti numeri:"))
for x in range (num) :
    y = int(input("immetti un numero:"))
    lista.append(y)
def parametri(n) :  
    for x in range (0,len(n)+1) :
        if x==3 or x==4 :
            print (n[x])
parametri(lista)
#A#Riempi 5 variabili con nomi di Animali, stampa i nomi

a = "leone"
b = "farfalla"
c = "tigre"
d = "cane"
e = "gatto"

#print ( a , b , c ,d ,e )

#B#Riempi due variabili (x e y) con dei valori. Se x è maggiore di y stampa “ciao”.
# Se x è minore o uguale a y stampa “arrivederci”

x = 5
y = 6
if x>y :
    print("ciao")
else :
    print("arrivederci")

#C#Riempi tre variabili (x, y ,z) con dei valori. Se x è maggiore di y e maggiore di z stampa ‘X è il numero maggiore’ 
x=6
y=5
z=3
if x>y and x>z :
    print ("x è il numero maggiore")

#D#Rifai l’esercizio C stampando il nome della variabile con il valore maggiore
x=6
y=50
z=330

if x>y and x>z :
    print (x)
elif y>x and y>z : 
    print (y)
else :
    print (z)

#E#Crea due vettori uno con il nome di città e uno con il nome di persone.
#Stampa usando dei cicli for per ogni città tutti i nomi degli abitanti
#es: [‘torino’, ‘milano’ ] | [‘gino’, ‘lino’]
#stampa: torino - gino | torino - lino | milano - gino | milano - lino

citta = ["Milano" , "Parigi" , "Pisa" , "Roma"]
persone = ["Luca","Paolo","Giovanni"]
for x in citta :
    for y in persone : 
        print (x,y)

#F#Riempi una lista di 5 numeri. E una variabile x. Stampa solo  i numeri maggiori di x
lista = [10 , 5 , 6 , 220 , 3543]
x=14
for y in lista :
    if y>x :
        print (y)

#G#Riempi una lista di 5 numeri e stampa il minore.
cinquenumeri = [12 , 22 , 45 , 56 , 66]
x= cinquenumeri[0]

for y in cinquenumeri : 
    if y<x :
        x=y       
print(x)

#H#Riempi una lista con 5 nomi di Animali e stampa la lista in ordine inverso
animali = ["a","b","c","d","e"]
animali.reverse()
print (animali)

#I#Dichiara due liste. Una con nomi di animali e l’altra con numeri. Aggiungi tutti gli elementi della seconda lista alla prima.
#Stampa soltanto i numeri maggiori di 5

animali = ["leone","falco","lucertola","farfalla"]
numeri = [1,5,7,3,87,34,231,547,234,435435,43]
z = numeri + animali
for x in z :
    if x<=5 :
        continue
print (z)
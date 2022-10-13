#creo le variabili 
x = 5
y = "Jhon"

#stampo le variabili 
print (x)
print (y)

#alla riassegnazione di una nuova variabile py riesce comunque a leggerla ( come l'ultima assegnazione data)
x=4
x="Sally"
print (x)

#trasforma quello che c'è dentro in quello che si specifica 
x = str(3)
print (x)
x = int(3)
print (x)
x = float (3)
print (x)

#per farti specificare il tipo di variabile 
x = 5
y = "john"
print (type(x))
print (type(y))

#le stringhe possono essere dichiarate sia con singole che con doppie virgolette 
x = "John"
x = 'John'  #sono la stessa cosa
 
#due variabili che hanno stessa lettera ma formato opposto ( maiuscolo o minuscolo) sono due variabili differenti 
a= 5
A= "John"
print (a)
print (A)

#Riempi tre variabili (x, y ,z) con dei valori. Se x è maggiore di y e maggiore di z stampa ‘X è il numero maggiore’ 
import random
x= random.randrange(1,10)
y= random.randrange(1,10)
z= random.randrange(1,10)

if x>y and x>z :
    print ("x è il numero maggiore")
elif y>x and y>z :
    print ("y è il numero maggiore")
else :
    print ("z è il numero maggiore")
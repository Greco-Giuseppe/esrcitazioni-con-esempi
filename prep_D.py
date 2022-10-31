#Rifai l’esercizio C stampando il nome della variabile con il valore maggiore
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
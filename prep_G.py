#Riempi una lista di 5 numeri e stampa il minore.
numeri = [1,4,6,45,0]
x = numeri[0]
for y in numeri :
    if y < x :
        x=y
print (x)
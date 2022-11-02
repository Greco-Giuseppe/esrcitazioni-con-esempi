#Dichiara due liste. Una con nomi di animali e l’altra con numeri. Aggiungi tutti gli elementi della seconda lista alla prima.
#Stampa soltanto i numeri maggiori di 5


animali = ["lucertola","cane","gatto","pipistrello","farfalla"]
numeri = [35 , 41 , 56 , 4 , 2 ]
z = animali + numeri 
print (z)
for x in numeri :
    if x > 5 :
        print (x)
        
# for 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 

# le lettere  contenute in una parola 
for x in "banana":
  print(x)

for x in "ciao come stai" :
    print(x)

#break 
#break , fermati nella lista quando x==

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break
#se break però viene messo prima del comando stampa , si fermeraà prima di stampare x==

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) 

# continue 
# elencando la lista , a differenza del break , salta l' x== ma continua ad elencare gli altri elementi della lista 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 

#range 
# specificato un numero , partendo da zero , ripeterà la stampa fino ad attonere la quantità di numeri spercificata 

for x in range(6):
  print(x)

#è possibile stabilire un numero di partenza con es . (2,6)
# si fermera però prima dell'ultimo numero specificato 

for x in range(2, 6):
  print(x)

#può essere specificato un altro numero che spefica di quanto saltare dal numero precedente
# (2,30,3) , ci stamperà i numeri da 2 a 29 saltando di 3 in 3 

for x in range(2, 30, 3):
  print(x)

#else nel gruppo for 
# una volta finito , posso comunicare che se nuo può stampare più nient'altro . "else" gli comunico di stampare qualcosa 

for x in range(6):
  print(x)
else:
  print("Finally finished!")

# The else block will NOT be executed if the loop is stopped by a break statement.

#break nel loop
# è posssibile fermare il loop prima di un determinato valore 
# ELSE , PERò , NON VERRà ESGUITO 

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#possono essere combinati due elementi di liste differenti tramite "x" e "y" , verranno fatte tutte le combinazioni possibili 

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#possibile utilizzo del "pass" , come in if (RIVEDERE ESEMPIO)

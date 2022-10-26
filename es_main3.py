# if , else

#condizioni matematiche
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

a = 33
b = 200

if b > a:
  print("b is greater than a")
# SE 'PRINT' VIENE MESSO IN CORRISPONDENZA DI 'IF' VERRA' SEGNALATO UN ERRORE 

# elif
#per aggiungere una condizione nel caso in cui non sia veriteria la precedente 'elif'
a = 33
b = 200

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# else 
# in caso in cui nessuna delle precedenti condizioni sia verificata 

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#scrivere in maniera più compatta 

if a > b: print("a is greater than b")

#oppure con else 
a = 2
b = 330
print("A") if a > b else print("B")

#si possono avere anche multipli ''elese''
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#and , operatore logico , si usa per accostare due condizioni 
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#or , operatore logico , o una condizione o l'altra

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#nasted if , concatenazione di if in caso in cui sia verificato il primo if 

#pass , non si può lasciare vuoto dopo if , quindi si mette  ''pass''







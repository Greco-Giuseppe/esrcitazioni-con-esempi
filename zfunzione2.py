#FUNZIONI 

#creare una funzione 
# utilizzare "def"
def my_function():
  print("Hello from a function")
#stampare gli elementi della funzione 
my_function()

# argomenti 
# creo un avariabile ("fname" , POSSO CHIAMARLA IN QUALSIASI MODO ) che conterrà le informazioni 
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# creare due argomenti e assegnargli diversi nomi 
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
# se immetto due argomenti ma ne assegno solo uno mi da errore 
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")  #ERRORE 

# utilizzo "*" 
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
#il numero tra le parentesi quadre corrisponde al numero dell'elemnto partendo da 0

#assegno ad ogni argomento un elemento 
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
#notare come assegnando ad ogni argomernto un nome non necessariamente bisogni utilizzare gli ordini degli argomenti 

# utilizzo "*" numero variabile di argomenti , a differenza del singolo asterisco(per le liste) in cui ci si accede con il numero (es. [2]) , in questo caso 
# ( nel dizionario ) vi accedo tramite nome 
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


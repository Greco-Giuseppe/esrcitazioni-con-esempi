#cpntrollare se un numero è un "int"
x = isinstance(5, int)

print(x)
#isinstance(object, type)
#se il tipo concide con l'oggetto risulterà il vero 

#utilizzabili anche più informazioni sul tipo
x = isinstance("Hello", (str, float, int, str, list, dict, tuple))

print(x)

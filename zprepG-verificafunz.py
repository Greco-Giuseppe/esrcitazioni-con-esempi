#Definisci una funzione che calcoli in modo ricorsivo la sequenza di Fibonacci di un numero passato come parametro

def fib(n) :
    if n == 1 : return 1
    if n == 0 : return 0
    return fib(n-1) + fib(n-2)
print(fib(8))
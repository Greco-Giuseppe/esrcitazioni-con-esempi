#E Definisci una funzione chiamata ‘primo’ che riceva come parametro un numero intero e ritorni true in caso il numero fosse primo
# Chiedi all’utente di inserire un numero. Stampa “primo” nel caso si tratti di un numero primo.

def primo(n):
    for x in range (2,n):
        check = int (n/x)
        if check*x==n :return False
    return true
primo(7)
if def primo(n) == true :
    print ("primo")
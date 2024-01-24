'''
Elencare i primi n numeri primi, chiedendo n all'utente e 
implementando l'algoritmo del "Crivello di Eratostene"
'''
import numpy as np 

def n_primo(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
    
n = int(input("Inserisci n: "))

ar = np.arange(2,n)
b = ar
for x in ar:
    if not n_primo(x):
       # print(x)
        idx = np.where(ar % x == 0)
       # print(idx)
        ar = np.delete(ar, idx)
print(ar)
      


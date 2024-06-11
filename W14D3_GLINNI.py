#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Esercizio Abbiamo una lista di liste: mat = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]] Che tipo di struttura dati o matematica potrebbe rappresentare? Notare che tutte le liste "interne" sono della stessa dimensione Come facciamo per accedere ad un elemento in particolare?

#  La struttura dati fornita, mat = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]], rappresenta una matrice in forma di lista di liste. In matematica, una matrice è una griglia rettangolare di numeri disposti in righe e colonne.

# Per accedere a un elemento specifico della matrice, usiamo due indici: uno per la riga e uno per la colonna. L'indice della riga è il primo indice e l'indice della colonna è il secondo indice. Gli indici in Python iniziano da 0.

# Definizione della matrice
mat = [
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14]
]

# Accesso e stampa di vari elementi della matrice
print(f"Primo elemento della prima riga (mat[0][0]): {mat[0][0]}")
print(f"Ultimo elemento dell'ultima riga (mat[2][4]): {mat[2][4]}")
print(f"Quarto elemento della seconda riga (mat[1][3]): {mat[1][3]}")
print(f"Terzo elemento della terza riga (mat[2][2]): {mat[2][2]}")
print(f"Secondo elemento della prima riga (mat[0][1]): {mat[0][1]}")

# Stampa dell'intera matrice per conferma
print("\nIntera matrice:")
for row in mat:
    print(row)


# In[ ]:


# Esercizio Importiamo il modulo math e proviamo a usare le funzioni .sin() .cos() .factorial() e la variabile .pi la riconoscete?

# possiamo importare il modulo math e utilizzare le funzioni sin(), cos(), factorial() e la variabile pi. Ecco un esempio:

mport math

# Utilizzo della funzione sin()
angle_rad = math.pi / 2  # 90 gradi in radianti
sin_value = math.sin(angle_rad)
print(f"sin({angle_rad}) = {sin_value}")

# Utilizzo della funzione cos()
angle_rad = 0  # 0 gradi in radianti
cos_value = math.cos(angle_rad)
print(f"cos({angle_rad}) = {cos_value}")

# Utilizzo della funzione factorial()
number = 5
factorial_value = math.factorial(number)
print(f"{number}! = {factorial_value}")

# Utilizzo della variabile pi
print(f"Valore di pi: {math.pi}")


# In[ ]:


# Esercizio Proviamo a eseguire math.degrees(math.pi) Qual è e cosa significa il risultato? Per saperne di più su questa funzione possiamo usare help(math.degrees)

import math

# Convertire pi radianti in gradi
degrees_value = math.degrees(math.pi)
print(f"math.degrees(math.pi) = {degrees_value}")

# Per saperne di più sulla funzione math.degrees(), usiamo help()
help(math.degrees)

# Quando eseguiamo questo codice, il risultato di math.degrees(math.pi) sarà:
math.degrees(math.pi) = 180.0
#Questo significa che  π radianti sono equivalenti a 180 gradi.


# In[ ]:


# Esercizio L'azienda Object SpA ha creato una lista di quanti oggetti ha venduto ogni mese nell'ultimo anno: lst = [2000, 5500, 7200, 4320, 1280, 1900, 2500, 3900, 6410, 8150, 7100, 5350] trasformiamola in un array NumPy (casting): lst = np.array(lst) e rispondiamo alle domande del CEO della Object SpA: • qual è stata la vendita massima mensile? E quella minima? • quali sono le vendite mensili maggiori di 4999 oggetti? E quante ne sono? • quali sono le vendite minori di 3000 oggetti?

import numpy as np

# Trasformare la lista in un array NumPy
lst = [2000, 5500, 7200, 4320, 1280, 1900, 2500, 3900, 6410, 8150, 7100, 5350]
sales = np.array(lst)

# Vendita massima e minima
max_sales = np.max(sales)
min_sales = np.min(sales)

# Vendite mensili maggiori di 4999 oggetti
high_sales = sales[sales > 4999]
num_high_sales = len(high_sales)

# Vendite mensili minori di 3000 oggetti
low_sales = sales[sales < 3000]

print(f"Vendita massima mensile: {max_sales}")
print(f"Vendita minima mensile: {min_sales}")
print(f"Vendite mensili maggiori di 4999 oggetti: {high_sales}")
print(f"Numero di vendite mensili maggiori di 4999 oggetti: {num_high_sales}")
print(f"Vendite mensili minori di 3000 oggetti: {low_sales}")


# In[ ]:


# Esercizio Consideriamo il seguente dizionario: fatturati_dict = {1997: 12_000, 1998: 15_000, 1999: 20_000, 2000: 23_000, 2001: 25_000, 2002: 17_000, 2003: 14_000, 2004: 21_000} Consideriamo ora la seguente Series: fatturati_series = pd.Series([12_000, 15_000, 20_000, 23_000, 25_000, 17_000, 14_000, 21_000], index=range(1997, 2005)) Possiamo accedere alle stesse informazioni nello stesso modo: fatturati_dict[1997] fatturati_series[1997] Dunque qual è la differenza tra i due tipi di dato? Cosa potremmo fare con la Series che non possiamo fare con il dizionario?

import pandas as pd
import matplotlib.pyplot as plt

# Dizionario dei fatturati
fatturati_dict = {1997: 12000, 1998: 15000, 1999: 20000, 2000: 23000, 2001: 25000, 2002: 17000, 2003: 14000, 2004: 21000}

# Series dei fatturati
fatturati_series = pd.Series([12000, 15000, 20000, 23000, 25000, 17000, 14000, 21000], index=range(1997, 2005))

# Operazioni con Series
incremented_series = fatturati_series * 1.10
print("Fatturati incrementati del 10%:\n", incremented_series)

average_revenue = fatturati_series.mean()
print(f"La media dei fatturati è: {average_revenue}")

high_revenues = fatturati_series[fatturati_series > 20000]
print("Fatturati maggiori di 20000:\n", high_revenues)

# Visualizzazione
fatturati_series.plot(kind='bar')
plt.xlabel('Anno')
plt.ylabel('Fatturato')
plt.title('Fatturato Annuale')


# In[ ]:


# Esercizio L'azienda Object SpA ha un dataset con tutti gli stipendi dei dipendenti, memorizzato in un ndarray: import numpy as np stipendi = np.array( [100, 200, 300, 400, 500,  600, 700, 800, 900, 1000] ) L'azienda ci chiede di raddoppiare tutti gli stipendi; facciamolo in due modi: • con un ciclo for 7 • con il masking

import pandas as pd
import matplotlib.pyplot as plt

# Dizionario dei fatturati
fatturati_dict = {1997: 12000, 1998: 15000, 1999: 20000, 2000: 23000, 2001: 25000, 2002: 17000, 2003: 14000, 2004: 21000}

# Series dei fatturati
fatturati_series = pd.Series([12000, 15000, 20000, 23000, 25000, 17000, 14000, 21000], index=range(1997, 2005))

# Operazioni con Series
incremented_series = fatturati_series * 1.10
print("Fatturati incrementati del 10%:\n", incremented_series)

average_revenue = fatturati_series.mean()
print(f"La media dei fatturati è: {average_revenue}")

high_revenues = fatturati_series[fatturati_series > 20000]
print("Fatturati maggiori di 20000:\n", high_revenues)

# Visualizzazione
fatturati_series.plot(kind='bar')
plt.xlabel('Anno')
plt.ylabel('Fatturato')
plt.title('Fatturato Annuale')
plt.show()  # Visualizza il grafico


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Individuiamo tre task di qualsiasi tipo (fare la spesa, studiare un concetto, riempire il serbatoio dell'auto, 

# acquistare uno snack da un distributore automatico, o qualunque altra cosa); Scriviamo un algoritmo (in forma 
# testuale), cioè i passi necessari, per ognuno dei task selezionati.

# Fare la spesa
# Avere soldi
# Andare al supermercato
# Prendere gli oggetti
# Pagare

# Riempire il serbatoio dell'auto
# Andare al benzinaio
# Aprire il serbatoio
# Prendere la pompa
# Selezionare l'importo da versare
# Versare il contenuto nel serbatoio

# acquistare uno snack da un distributore automatico
# Arrivare al distributore
# Individuare il numero corrispondente allo snack
# Versare l'importo corrispondente
# Prelevare lo snack


# In[ ]:


# Abbiamo 25 studenti; memorizzare questo dato in una variabile.

# Creiamo una lista di 25 studenti
studenti = [ "Studente1", "Studente2", "Studente3", "Studente4", "Studente5",
    "Studente6", "Studente7", "Studente8", "Studente9", "Studente10",
    "Studente11", "Studente12", "Studente13", "Studente14", "Studente15",
    "Studente16", "Studente17", "Studente18", "Studente19", "Studente20",
    "Studente21", "Studente22", "Studente23", "Studente24", "Studente25" ]


# In[ ]:


# Abbiamo 25 studenti; memorizzare questo dato in una variabile e stampare.

# Creiamo una lista di 25 studenti
studenti = [ "Studente1", "Studente2", "Studente3", "Studente4", "Studente5",
    "Studente6", "Studente7", "Studente8", "Studente9", "Studente10",
    "Studente11", "Studente12", "Studente13", "Studente14", "Studente15",
    "Studente16", "Studente17", "Studente18", "Studente19", "Studente20",
    "Studente21", "Studente22", "Studente23", "Studente24", "Studente25" ]

# Stampiamo la lista di studenti
print(studenti)


# In[ ]:


# Esercizio Abbiamo 25 studenti; memorizzare questo dato in una variabile. Arrivano altri 3 studenti; memorizzare questo dato in un'altra variabile.

studenti = [ "Studente1", "Studente2", "Studente3", "Studente4", "Studente5",
    "Studente6", "Studente7", "Studente8", "Studente9", "Studente10",
    "Studente11", "Studente12", "Studente13", "Studente14", "Studente15",
    "Studente16", "Studente17", "Studente18", "Studente19", "Studente20",
    "Studente21", "Studente22", "Studente23", "Studente24", "Studente25" ]

studenti2 = [ "Studente26", "Studente27", "Studente28"]


# In[7]:


# Esercizio Abbiamo 25 studenti; memorizzare questo dato in una variabile. Arrivano altri 3 studenti; memorizzare questo dato in un'altra variabile. Creare un'altra variabile ancora che conterrà la somma delle prime due, poi stamparla a video.

studenti1 = [ "Studente1", "Studente2", "Studente3", "Studente4", "Studente5",
    "Studente6", "Studente7", "Studente8", "Studente9", "Studente10",
    "Studente11", "Studente12", "Studente13", "Studente14", "Studente15",
    "Studente16", "Studente17", "Studente18", "Studente19", "Studente20",
    "Studente21", "Studente22", "Studente23", "Studente24", "Studente25" ]

studenti2 = [ "Studente26", "Studente27", "Studente28"]

studenti1_2 = [studenti1 + studenti2]

print(studenti1_2)


# In[9]:


# Creare una variabile che contiene la stringa "Epicode", quindi stamparla a video.

epicode = "Epicode"

print(epicode)


# In[19]:


# Esercizio Abbiamo la variabile: x = 10 Incrementarla di 2 e poi moltiplicarla per 3.

x = 10
x = x+2
x = x*3

print(x)

y = ((10+2)*3)

print(y)


# In[29]:


# Verificare, per ognuna delle seguenti stringhe, se il numero di caratteri è compreso tra 5 e 8:str1 = "Windows" • str2 = "Excel" • str3 = "Powerpoint" • str4 = "Word"

str1 = "Windows"
str2 = "Excel"
str3 = "Powerpoint"
str4 = "Word"

# Verifichiamo se il numero di caratteri è compreso tra 5 e 8 per ciascuna stringa.

#La funzione len() restituisce la lunghezza della stringa str1!

risultato_str1 = 5 <= len(str1) <= 8
risultato_str2 = 5 <= len(str2) <= 8
risultato_str3 = 5 <= len(str3) <= 8
risultato_str4 = 5 <= len(str4) <= 8

# Stampiamo i risultati. f prima delle virgolette stampa la variabile indicata come stringa; subito dopo inserisce TRUE o FALSE a seconda del risultato. 
# Verifica quindi se risultato_str1 ecc sono tra 5 e 8, e in caso mette TRUE o FALSE.
# f permette quindi di inserire variabili ed espressioni direttamente all'interno della stringa.

print(f"str1 ('Windows'): {risultato_str1}")
print(f"str2 ('Excel'): {risultato_str2}")
print(f"str3 ('Powerpoint'): {risultato_str3}")
print(f"str4 ('Word'): {risultato_str4}")


# In[25]:


# Esercizio Calcolare e stampare a video quanti secondi ci sono in un anno non bisestile.

# Definiamo il numero di secondi in un minuto, minuti in un'ora e ore in un giorno

secondi_in_un_minuto = 60
minuti_in_un_ora = 60
ore_in_un_giorno = 24
giorni_in_un_anno_non_bisestile = 365

# Calcoliamo il numero totale di secondi in un anno non bisestile, moltiplicando i vari operatori.

secondi_in_un_anno_non_bisestile = (
    secondi_in_un_minuto * 
    minuti_in_un_ora * 
    ore_in_un_giorno * 
    giorni_in_un_anno_non_bisestile
)

# Stampiamo il risultato. Sarà stampato il risultato della funzione!

print(f"Il numero di secondi in un anno non bisestile è: {secondi_in_un_anno_non_bisestile}")


# In[33]:


# Definiamo la stringa dell'esercizio
stringa_esercizio = "I am studying Python"

# Trasformiamo tutti i caratteri in maiuscolo utilizzando il metodo preimpostato .upper()
stringa_upper = stringa_esercizio.upper()
print(f"Uppercase: {stringa_upper}")

# Trasformiamo tutti i caratteri in minuscolo utilizzando il metodo preimpostato .lower()
stringa_lower = stringa_esercizio.lower()
print(f"Lowercase: {stringa_lower}")

# Sostituiamo la sottostringa "Python" con "a lot" utilizzando il metodo preimpostato .replace()
stringa_replaced = stringa_esercizio.replace("Python", "a lot")
print(f"Replaced: {stringa_replaced}")

# Utilizziamo il metodo .strip() (non necessario in questo caso perché non ci sono spazi bianchi all'inizio o alla fine della stringa)
stringa_stripped = stringa_esercizio.strip()
print(f"Stripped: {stringa_stripped}")

# Verifichiamo se .strip() cambia qualcosa (in questo caso, non cambierà nulla)
print(f"Original and stripped are the same: {stringa_esercizio == stringa_stripped}")


# In[ ]:





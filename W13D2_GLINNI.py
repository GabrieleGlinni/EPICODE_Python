#!/usr/bin/env python
# coding: utf-8

# In[3]:


# nome_scuola = "Epicode" Stampare ogni carattere della stringa, uno su ogni riga, utilizzando un costrutto while.

nome_scuola = "Epicode"
i = 0

while i < len(nome_scuola):
    print(nome_scuola[i])
    i += 1 # i incrementa ad ogni giro, percorrendo tutta la stringa!


# In[ ]:


# Stampare a video tutti i numeri da 0 a 20 utilizzando il costrutto while. Utilizzeremo: • un ciclo while • la funzione print() • una variabile, che dovrà essere inizializzata • una procedura di incremento

# Inizializzare la variabile contatore
numero = 0

# Utilizzare un ciclo while per iterare finché il contatore è minore o uguale a 20
while numero <= 20:
    # Stampare il valore del contatore
    print(numero)
    # Incrementare il contatore di 1
    numero += 1


# In[5]:


# Calcolare e stampare tutte le prime 10 potenze di 2 (e.g., 2⁰, 2¹, 2², …) utilizzando un ciclo while.

# Inizializzare la variabile contatore
i = 0

# Utilizzare un ciclo while per iterare finché il contatore è minore di 10
while i < 10:
    # Calcolare la potenza di 2
    potenza = 2 ** i
    # Stampare il risultato
    print(f"2^{i} = {potenza}") # La f prima della stringa indica che si tratta di una f-string e permette di inserire variabili ed espressioni tra le parentesi graffe {} all'interno della stringa. Quindi ci riporta a che punto è i, uguale e risultato della potenza.
    # Incrementare il contatore di 1
    i += 1


# In[5]:


# Calcolare e stampare tutte le prime 10 potenze di 2 (e.g., 2⁰, 2¹, 2², …) utilizzando un ciclo while.

# Inizializzare la variabile contatore
i = 0

# Utilizzare un ciclo while per iterare finché il contatore è minore di 10
while i < 10:
    # Calcolare la potenza di 2
    potenza = 2 ** i
    # Stampare il risultato
    print(f"2^{i} = {potenza}") # La f prima della stringa indica che si tratta di una f-string e permette di inserire variabili ed espressioni tra le parentesi graffe {} all'interno della stringa. Quindi ci riporta a che punto è i, uguale e risultato della potenza.
    # Incrementare il contatore di 1
    i += 1


# In[7]:


# Calcolare e stampare tutte le prime N potenze di 2 utilizzando un ciclo while, domandando all'utente di inserire N.

# Chiedere all'utente di inserire il valore di N
N = int(input("Inserisci il numero di potenze di 2 da calcolare: ")) #input è una funzione preimpostata che costituisce, appunto, la possibilità dell'utente di inserire l'input

# Inizializzare la variabile contatore
i = 0

# Utilizzare un ciclo while per iterare finché il contatore è minore di N
while i < N:
    # Calcolare la potenza di 2
    potenza = 2 ** i
    # Stampare il risultato
    print(f"2^{i} = {potenza}")
    # Incrementare il contatore di 1
    i += 1
    


# In[ ]:


# Calcolare e stampare tutte le potenze di 2 minori di 25000.

# Inizializzare la variabile contatore
i = 0
# Calcolare la prima potenza di 2
potenza = 2 ** i

# Utilizzare un ciclo while per iterare finché la potenza è minore di 25000
while potenza < 25000:
    # Stampare il risultato
    print(f"2^{i} = {potenza}")
    # Incrementare il contatore di 1
    i += 1
    # Calcolare la prossima potenza di 2
    potenza = 2 ** i


# In[1]:


# Abbiamo due liste, una di studenti e una di corsi. Aggiungere i dati mancanti alla lista corsi. Aggiungeremo i dati mancanti uno alla volta con il metodo per appendere in coda alle liste, poi verificheremo che sono della stessa lunghezza e se lo sono stamperemo la lista corsi. Se alcuni dati sono già presenti non vanno aggiunti 

# Liste originali
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend"]

# Dati mancanti
dati_mancanti = [("Emma", "Data Analyst"), ("Faith", "Backend"), ("Grace", "Frontend"), ("Henry", "Cybersecurity")]

# Aggiungi i dati mancanti uno alla volta se non sono già presenti
for studente, corso in dati_mancanti:
    if studente in studenti and studenti.index(studente) >= len(corsi):
        corsi.append(corso)

# Verifica che le due liste abbiano la stessa lunghezza
if len(studenti) == len(corsi):
    print("La lista dei corsi è:", corsi)
else:
    print("Le liste non hanno la stessa lunghezza.")


# In[5]:


# Scriviamo un programma che chiede in input all'utente una stringa e visualizza i primi 3 caratteri, seguiti da 3 punti di sospensione e quindi gli ultimi 3 caratteri, similmente all'esercizio della lezione scorsa. Stavolta facciamo attenzione a tutti i casi particolari, ovvero implementare soluzioni ad hoc per stringhe di lunghezza inferiore a 6 caratteri.

# Chiedere in input all'utente una stringa.
input_string = input("Inserisci una stringa: ")

# Determina la lunghezza della stringa
length = len(input_string)

# Gestisce i vari casi
if length < 6:
    # Se la stringa ha meno di 6 caratteri, stampa la stringa intera
    print(input_string)
else:
    # Se la stringa ha almeno 6 caratteri, costruisce la stringa richiesta
    result = input_string[:3] + "..." + input_string[-3:] #ossia, :3 estrae i primi tre caratteri, "..." è il concatena, -3  estrae gli ultimi 3 caratteri
    print(result)


# In[ ]:


# Esercizio Memorizza e stampa tutti i fattori di un numero dato in input. Esempio: • input: 150 • output: [2, 3, 5, 5]

def fattori_primi(n):
    # Lista per memorizzare i fattori primi
    fattori = []

    # Divide per 2 finché è possibile
    while n % 2 == 0: # finché è divisibile per due
        fattori.append(2) # aggiungi 2
        n = n // 2 # dividi per due intero

    # Divide per i numeri dispari a partire da 3
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            fattori.append(i)
            n = n // i

    # Se n è un numero primo maggiore di 2, aggiungilo alla lista
    if n > 2:
        fattori.append(n)


# In[ ]:


# Esercizio Abbiamo la stringa: nome_scuola = "Epicode" Stampare ogni carattere della stringa, uno su ogni riga, utilizzando un costrutto for.

# Stringa data
nome_scuola = "Epicode"

# Utilizza un ciclo for per iterare su ogni carattere della stringa
for carattere in nome_scuola:
    print(carattere)


# In[ ]:


# Esercizio Calcolare e stampare tutte le prime 10 potenze di 2 utilizzando un ciclo. Utilizzeremo: • un ciclo per generare i primi 10 numeri, e.g.: range_numerico = list()  # init num = 1  # init while num <= 10: range_numerico.append(num) num += 1

# Inizializza una lista vuota per memorizzare i numeri
range_numerico = []

# Inizializza il numero di partenza
num = 1

# Utilizza un ciclo while per generare i primi 10 numeri
while num <= 10:
    range_numerico.append(num)
    num += 1

# Calcola e stampa le prime 10 potenze di 2 utilizzando i numeri nella lista
for n in range_numerico:
    potenza_di_due = 2 ** n
    print(f"2^{n} = {potenza_di_due}")


# In[ ]:


# Esercizio Calcolare (ma non stampare) le prime N potenze di K; ognuna di esse andrà memorizzata in coda a una lista. Alla fine, stampare la lista risultante. Proviamo con diversi valori di K, oppure facciamola inserire all'utente. Realizzare due versioni: • con un ciclo while, • con un ciclo for.

# Chiede all'utente di inserire il valore di K e N
K = int(input("Inserisci il valore di K: "))
N = int(input("Inserisci il numero di potenze da calcolare: "))

# Inizializza una lista vuota per memorizzare le potenze di K
potenze = []

# Utilizza un ciclo for per calcolare le prime N potenze di K e memorizzarle nella lista
for i in range(1, N + 1):
    potenze.append(K ** i)

# Stampa la lista risultante
print("Le prime", N, "potenze di", K, "sono:", potenze)


# In[ ]:


# Esercizio Abbiamo una lista con i guadagni degli ultimi 12 mesi: guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50] usando un costrutto for, calcolare la media dei guadagni e stamparla a video.

# Lista dei guadagni degli ultimi 12 mesi
guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]

# Inizializza la somma dei guadagni a 0
somma = 0

# Utilizza un ciclo for per iterare su ogni guadagno nella lista
for guadagno in guadagni:
    somma += guadagno  # Aggiunge il guadagno corrente alla somma

# Calcola la media dividendo la somma per il numero totale di mesi
media = somma / len(guadagni)

# Stampare la media dei guadagni
print("La media dei guadagni degli ultimi 12 mesi è:", media)


# In[ ]:


# Esercizio Abbiamo una lista di parole: parole = ["Albergo", "Sedia", "Borgo", "Petalo", "Eremo", "Belvedere", "Semestre", "Esteta", "Sosta", "Orpello", "Abete", "Orologio", "Cesta", "Ermellino"] stampiamo, per ogni parola, quante volte appare la lettera "e"; facciamo attenzione al fatto che appare sia maiuscola che minuscola.

# Lista delle parole
parole = ["Albergo", "Sedia", "Borgo", "Petalo", "Eremo", "Belvedere", "Semestre", "Esteta", "Sosta", "Orpello", "Abete", "Orologio", "Cesta", "Ermellino"]

# Utilizza un ciclo for per iterare su ogni parola nella lista
for parola in parole:
    # Conta quante volte appare la lettera 'e' (sia maiuscola che minuscola) nella parola corrente
    conteggio_e = parola.lower().count('e')
    
    # Stampare il risultato
    print(f"Nella parola '{parola}' la lettera 'e' appare {conteggio_e} volte.")


# In[ ]:


# Esercizio Creiamo un dizionario che assegni ad ogni proprietario la sua auto, sapendo che: • Ada guida una Punto • Ben guida una Multipla • Charlie guida una Golf • Debbie guida una 107 Stampiamo il dizionario per intero, e poi l'auto associata a Debbie.

# Creazione del dizionario proprietario-auto
dizionario_auto = {
    "Ada": "Punto",
    "Ben": "Multipla",
    "Charlie": "Golf",
    "Debbie": "107"
}

# Stampa del dizionario completo
print("Dizionario proprietario-auto:")
print(dizionario_auto)

# Stampare l'auto associata a Debbie
auto_debbie = dizionario_auto.get("Debbie")
print("\nL'auto associata a Debbie è:", auto_debbie)


# In[ ]:


# Esercizio Abbiamo un dizionario che assegna ad ogni proprietario la sua auto: dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107"} Con un ciclo, e usando il metodo .values(), stampiamo a video tutte le auto che non sono una Multipla.

# Dizionario proprietario-auto
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107"}

# Utilizza un ciclo for per iterare su ogni auto nel dizionario
for auto in dizionario_auto.values():
    if auto != "Multipla": # se l'auto non è multipla...
        print(auto)


# In[ ]:


# Esercizio Abbiamo due dizionari che assegnano ad ogni proprietario la propria auto: dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107", "Emily": "A1"} nuovi_proprietari = {"Ben": "Polo", "Fred": "Octavia", "Grace": "Yaris", "Hugh": "Clio"} Aggiornare il dizionario dizionario_auto con i dati contenuti in nuovi_proprietari e stamparlo. Cosa è successo a Ben?

# Dizionari proprietario-auto
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107", "Emily": "A1"}
nuovi_proprietari = {"Ben": "Polo", "Fred": "Octavia", "Grace": "Yaris", "Hugh": "Clio"}

# Aggiorna il dizionario dizionario_auto con i dati contenuti in nuovi_proprietari
dizionario_auto.update(nuovi_proprietari)

# Stampa il dizionario aggiornato
print("Dizionario proprietario-auto aggiornato:")
print(dizionario_auto)

# Cosa è successo a Ben?
# Dopo l'aggiornamento del dizionario, il valore associato alla chiave "Ben" è stato modificato da "Multipla" a "Polo", poiché nel dizionario nuovi_proprietari il valore associato a "Ben" era "Polo". Quindi, "Ben" ora guida una "Polo" anziché una "Multipla".


# In[ ]:


# Esercizio Scrivere un programma che, data una lista di numeri, fornisca in output il minimo e il massimo (possiamo usare o meno le funzioni built-in min() e max()).

# Funzione per calcolare il valore minimo di una lista di numeri
def minimo(lista):
    if not lista:  # Controlla se la lista è vuota
        return None
    min_val = lista[0]  # Assegna il primo elemento come minimo iniziale
    for numero in lista:
        if numero < min_val:  # Se il numero corrente è minore del minimo attuale, aggiorna il minimo
            min_val = numero
    return min_val

# Funzione per calcolare il valore massimo di una lista di numeri
def massimo(lista):
    if not lista:  # Controlla se la lista è vuota
        return None
    max_val = lista[0]  # Assegna il primo elemento come massimo iniziale
    for numero in lista:
        if numero > max_val:  # Se il numero corrente è maggiore del massimo attuale, aggiorna il massimo
            max_val = numero
    return max_val

# Lista di numeri di esempio
numeri = [10, 5, 20, 15, 8, 25]

# Calcola il valore minimo e massimo utilizzando le funzioni definite sopra
minimo_valore = minimo(numeri)
massimo_valore = massimo(numeri)

# Stampa il risultato
print("Valore minimo:", minimo_valore)
print("Valore massimo:", massimo_valore)


# In[ ]:


# Esercizio Scrivere un programma che, data una lista di numeri, fornisca in output i tre numeri più grandi; gestire il caso in cui la lista sia più corta di tre, e quando uno o più dei numeri selezionati sono uguali.

def tre_numeri_piu_grandi(lista):
    if len(lista) < 3:  # Se la lista ha meno di tre numeri
        return "La lista deve contenere almeno tre numeri."
    
    # Rimuove i duplicati dalla lista e la ordina in ordine decrescente
    lista_ordinata = sorted(set(lista), reverse=True)
    
    if len(lista_ordinata) == 1:  # Se tutti i numeri nella lista sono uguali
        return f"I tre numeri più grandi sono: {lista_ordinata[0]} (tutti uguali)"
    
    # Se ci sono solo due numeri unici nella lista
    if len(lista_ordinata) == 2:
        return f"I tre numeri più grandi sono: {lista_ordinata[0]}, {lista_ordinata[1]} (due numeri unici)"
    
    # Altrimenti, ci sono tre o più numeri unici nella lista
    return f"I tre numeri più grandi sono: {lista_ordinata[0]}, {lista_ordinata[1]}, {lista_ordinata[2]}"

# Lista di numeri di esempio
numeri = [10, 5, 20, 15, 8, 25]

# Stampa i tre numeri più grandi
print(tre_numeri_piu_grandi(numeri))


# In[ ]:


# Esercizio Scrivere un programma che • in input acquisisce una lista di numeri e un numero K • in output, dovrà restituire la media di tutti i numeri nella lista maggiori o uguali a K • se non ce ne dovesse essere nessuno, dovrà stampare a schermo un messaggio adeguato.

def media_numeri_maggiore_uguale(lista, K):
    # Filtra la lista per ottenere solo i numeri maggiori o uguali a K
    numeri_filtrati = [numero for numero in lista if numero >= K]
    
    # Se non ci sono numeri maggiori o uguali a K nella lista
    if not numeri_filtrati:
        return "Non ci sono numeri maggiori o uguali a K nella lista."
    
    # Calcola la media dei numeri filtrati
    media = sum(numeri_filtrati) / len(numeri_filtrati)
    return media

# Input della lista di numeri e del numero K
lista_numeri = [10, 5, 20, 15, 8, 25]
K = 12  # Numero K di esempio

# Calcola e stampa la media dei numeri maggiori o uguali a K
print("La media dei numeri maggiori o uguali a", K, "è:", media_numeri_maggiore_uguale(lista_numeri, K))


# In[ ]:


# Esercizio Scrivere un programma che, data una lista di numeri, come output stamperà lo stesso numero di asterischi su righe diverse, ottenendo una semplice visualizzazione grafica Esempio, supponendo di avere il seguente input: numeri = [5, 2, 3, 4] L'output sarà: ***** ** *** ****

numeri = [5, 2, 3, 4]

# Utilizza un ciclo for per iterare su ogni numero nella lista
for numero in numeri:
    # Stampa l'asterisco '*' tante volte quanto il numero corrente
    print("*" * numero)


# In[ ]:


# Esercizio Abbiamo una lista di codici fiscali: lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"] • trovare i codici fiscali che contengono "95", metterli in una lista, e alla fine stamparla; • inoltre, per ognuno di essi, stampare a video i caratteri relativi al nome e quelli relativi al cognome.

# Lista dei codici fiscali
lista_cf = [
    "ABCDEF95G01A123B",
    "GHIJKL91M02A321C",
    "MNOPQR89S03A456D",
    "STUVWX95Z04A654E",
    "XYZABC01D05A789F",
    "DEFGHI95J06A987G"
]

# Lista per memorizzare i codici fiscali che contengono "95"
cf_contenenti_95 = []

# Utilizza un ciclo for per iterare su ogni codice fiscale nella lista
for cf in lista_cf:
    if "95" in cf:
        # Aggiungi il codice fiscale alla lista cf_contenenti_95 se contiene "95"
        cf_contenenti_95.append(cf)

# Stampa i codici fiscali che contengono "95"
print("Codici fiscali che contengono '95':", cf_contenenti_95)

# Per ogni codice fiscale che contiene "95", stampa i caratteri relativi al nome e quelli relativi al cognome
for cf in cf_contenenti_95:
    # Estrai i caratteri relativi al nome (prime tre lettere)
    nome = cf[:3]
    # Estrai i caratteri relativi al cognome (tre lettere successive dopo "95")
    cognome = cf[cf.index("95") + 2:cf.index("95") + 5]
    print("Nome:", nome, "Cognome:", cognome)


# In[7]:


# Esercizio Abbiamo tre liste della stessa lunghezza, dove ogni elemento nella medesima posizione si riferisce ai dati dello stesso studente: studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"] corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend", "Frontend", "Cybersecurity"] edizioni = [1, 2, 3, 2, 2, 1, 3, 3] • Stampare a video tutti e soli gli studenti che frequentano una prima edizione; non tutti i dati potrebbero essere necessari. 25 • Riuscite a vedere una similarità con la logica che si usa in SQL e le tabelle relazionali?

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]

for i in range(len(studenti)):
    if edizioni[i] == 1:
        print(studenti[i])

# La richiesta di stampare solo gli studenti che frequentano una prima edizione è simile a una query SQL con una clausola WHERE. In SQL, potremmo scrivere qualcosa del genere:
# SELECT studenti
# FROM tabella_studenti
# WHERE edizioni = 1;


# In[ ]:


# Esercizio Abbiamo una lista di stringhe di prezzi in dollari, che erroneamente sono stati scritti con il simbolo dell'euro: prezzi = ["100 €", "200 €", "500 €", "10 €", "50 €", "70 €"] cambiare il simbolo dell'euro (€) in quello del dollaro ($) per ogni stringa nella lista; il risultato sarà memorizzato in un'altra lista.

# Lista dei prezzi con il simbolo dell'euro
prezzi = ["100 €", "200 €", "500 €", "10 €", "50 €", "70 €"]

# Lista per memorizzare i prezzi con il simbolo del dollaro
prezzi_dollaro = []

# Itera su ogni stringa nella lista prezzi
for prezzo in prezzi:
    # Sostituisci il simbolo dell'euro con il simbolo del dollaro
    prezzo_dollaro = prezzo.replace("€", "$")
    # Aggiungi il prezzo con il simbolo del dollaro alla lista prezzi_dollaro
    prezzi_dollaro.append(prezzo_dollaro)

# Stampa la lista dei prezzi con il simbolo del dollaro
print("Prezzi con il simbolo del dollaro:")
print(prezzi_dollaro)


# In[ ]:


# Esercizio Abbiamo una lista di studenti: studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry", "Isabelle", "John"] vogliamo dividere gli studenti in due squadre per un campionato di Uno nel seguente modo: selezioneremo i nomi in posizione pari per un squadra, e i nomi in posizione dispari per l'altra. Creiamo due liste per ogni squadra, e alla fine visualizziamole.

# Lista degli studenti
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry", "Isabelle", "John"]

# Inizializza le liste per le due squadre
squadra_pari = []
squadra_dispari = []

# Utilizza un ciclo for per iterare attraverso la lista degli studenti
for i, studente in enumerate(studenti):
    if i % 2 == 0:
        # Se la posizione è pari, aggiungi lo studente alla squadra_pari
        squadra_pari.append(studente)
    else:
        # Altrimenti, aggiungi lo studente alla squadra_dispari
        squadra_dispari.append(studente)

# Stampa le due squadre
print("Squadra Pari:", squadra_pari)
print("Squadra Dispari:", squadra_dispari)


# In[ ]:


# Esercizio Abbiamo una lista con i guadagni degli ultimi 12 mesi (supponiamo da Gennaio a Dicembre): guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50] dobbiamo confrontare, stampando tutto a video, il guadagno di ogni mese con la media dei guadagni precedenti, e specificare nell'output se il guadagno attuale è maggiore o minore della media dei precedenti. Esempio di un possibile output: Mese 1: 100 € Mese 2: 90 € (media prec: 100 € - il guadagno attuale è minore)

# Lista dei guadagni degli ultimi 12 mesi
guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]

# Utilizza un ciclo for per iterare attraverso ogni mese
for i, guadagno in enumerate(guadagni):
    # Calcola la media dei guadagni precedenti
    media_precedenti = sum(guadagni[:i]) / i if i > 0 else 0
    
    # Confronta il guadagno attuale con la media dei guadagni precedenti
    confronto = "maggiore" if guadagno > media_precedenti else "minore"
    
    # Stampa il guadagno del mese e il confronto con la media dei guadagni precedenti
    print(f"Mese {i + 1}: {guadagno} € (media prec: {media_precedenti:.2f} € - il guadagno attuale è {confronto})")


# In[ ]:





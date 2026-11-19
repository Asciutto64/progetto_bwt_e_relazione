


    #funzione per aggiungere il dollaro alla fine
def aggiungi_dollaro(parola):
    # Aggiunge il '$' alla fine della stringa
    parola_con_dollaro = parola + "$"
    
    # Converte la stringa in una lista di singoli caratteri
    lista_caratteri = list(parola_con_dollaro)
    
    # Ritorna la lista di caratteri
    return lista_caratteri

def rotazioni_bwt(lista_caratteri):
    #trasformo la stringa di caratteri ìin una stringa normale
    testo="".join(lista_caratteri)
    lunghezza = len(testo)

    # Tutte le rotazioni possibili, spostando il carattere in fondo

    rotazioni = []
    for i in range(lunghezza):
        rotazione = testo[i:] + testo[:i]
        rotazioni.append(rotazione)

    return rotazioni 

#funzione che si occupa di ordinare le rotazioni alfabeticamente
def ordina_rotazioni(rotazioni):
    rotazioni_ordinate = sorted(rotazioni)
    return rotazioni_ordinate

    #funzione che prende l'ultima lettere di ogni rotazione e la salva
def estrai_ultima_colonna(rotazioni_ordinate):
    ultima_colonna = ""
    #ciclo che scorre per prendere l'ultimo carattere di ogni rotazione
    for riga in rotazioni_ordinate:
        ultima_colonna += riga[-1]

        return ultima_colonna

# prende tutte le funzioni e le mette tutta in una unica
def calcola_bwt(parola):
    lista = aggiungi_dollaro(parola)
    rotazioni =rotazioni_bwt(lista)
    ordinate = ordina_rotazioni(rotazioni)
    risultato = estrai_ultima_colonna(ordinate)
    return risultato

if __name__ == "__main__":

    while True:
        # viene inserito dall'utente una stringa in input 
        input_utente = input("Inserisci la stringa in input: ")
        
        # .strip() rimuove spazia all'inizio ed alla fine
        input_utente = input_utente.strip()
        
        # verifica se la lunghezza della parola è 0 
        if len(input_utente) == 0:
            print("Errore: Non hai inserito nessuna parola.\n")
            
        # Controlla se c'è uno spazio dentro l'input 
        elif " " in input_utente:
            print(f"Errore: Hai inserito più parole ('{input_utente}').\n")
            
        else:
            bwt_calcolo = calcola_bwt(input_utente)
            print(f"Risultato BWT: {bwt_calcolo}")
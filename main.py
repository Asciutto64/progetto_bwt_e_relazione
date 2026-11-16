
#FUNZIONE PER L'INPUT e per la validità dell'input
def richiedi_input_valido():

    while True:
        # Chiede all'utente di scrivere qualcosa e lo salva nella variabile 'input_utente'
        input_utente = input("Inserisci la stringa in input (una sola parola): ")
        
        # .strip() taglia via gli spazi invisibili all'inizio e alla fine della parola
        input_utente = input_utente.strip()
        
        # Controlla se la lunghezza della parola è 0 
        if len(input_utente) == 0:
            print("Errore: Non hai inserito nessuna parola. Riprova.\n")
            
        # Controlla se c'è uno spazio dentro l'input 
        elif " " in input_utente:
            print(f"Errore: Hai inserito più parole ('{input_utente}'). Te ne serve solo una. Riprova.\n")
            
        # Se non è vuoto e non ha spazi
        else:
            # Ritorna la parola valida a chi ha chiamato la funzione ed esce dal ciclo
            return input_utente


# 2. FUNZIONE PER AGGIUNGERE IL DOLLARO
def aggiungi_dollaro(parola):
    """Questa funzione prende la parola e le attacca il simbolo terminatore $."""
    # Aggiunge il carattere '$' alla fine della stringa
    parola_con_dollaro = parola + "$"
    
    # Converte la stringa in una lista di singoli caratteri (es. "ciao" -> ['c','i','a','o'])
    lista_caratteri = list(parola_con_dollaro)
    
    # Ritorna la lista di caratteri
    return lista_caratteri



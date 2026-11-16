
#FUNZIONE PER L'INPUT
def richiedi_input_valido():
    """Questa funzione gestisce solo la richiesta dell'input e i controlli."""
    # Inizia un ciclo infinito. Ne usciremo solo quando l'input è corretto.
    while True:
        # Chiede all'utente di scrivere qualcosa e lo salva nella variabile 'input_utente'
        input_utente = input("Inserisci la stringa in input (una sola parola): ")
        
        # .strip() taglia via gli spazi invisibili all'inizio e alla fine della parola
        input_utente = input_utente.strip()
        
        # Controlla se la lunghezza della parola è 0 (l'utente ha premuto solo Invio)
        if len(input_utente) == 0:
            print("Errore: Non hai inserito nessuna parola. Riprova.\n")
            
        # Controlla se c'è uno spazio dentro l'input (significa che ci sono più parole)
        elif " " in input_utente:
            print(f"Errore: Hai inserito più parole ('{input_utente}'). Te ne serve solo una. Riprova.\n")
            
        # Se non è vuoto e non ha spazi, l'input è perfetto!
        else:
            # Ritorna la parola valida a chi ha chiamato la funzione ed esce dal ciclo
            return input_utente


def burrows_wheeler_transform(testo: str) -> str:

    #se alla fine del testo non è presente il dollaro  entra nel 
    if not testo.endswith('$'):
        testo += '$'
    
    n = len(testo)
    
    # 1. Generazione di tutte le rotazioni cicliche
    rotazioni = [testo[i:] + testo[:i] for i in range(n)]
    
    # 2. Ordinamento lessicografico
    rotazioni_ordinate = sorted(rotazioni)
    
    # 3. Stampa di ogni rotazione ordinata a capo
    print("\n--- Matrice delle rotazioni ordinate ---")
    for rotazione in rotazioni_ordinate:
        print(rotazione)
    print("---------------------------------------\n")
    
    # 4. Estrazione dell'ultima colonna
    trasformata = "".join(rotazione[-1] for rotazione in rotazioni_ordinate)
    
    return trasformata



stringa_input=input("inserisci la stringa in input: ")

risultato= burrows_wheeler_transform(stringa_input)
print(f"Stringa originale con '$': {stringa_input}")

print(f"Trasformata di Burrows-wheeler: {risultato}")

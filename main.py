def divisione_stringa ():
    if not stringa:
        return ""

    stringa_splittata=stringa.split()
    return stringa_splittata

def aggiunta_dollaro():
    for stringa in divisione_stringa():
        stringa=stringa+"$"
        print(stringa)
    return stringa    

def traslazione_caratteri_e_salvataggio_in_lista():
    for stringa in aggiunta_dollaro():
        temp_salva_carattere=stringa[0]
        print(aggiunta_dollaro()[1:])
    return 0    

stringa=input("inserisci la stringa in input: ")
#divisione_stringa()
#aggiunta_dollaro()

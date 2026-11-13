def aggiunta_dollaro(stringa_dollaro_finale):
    stringa_dollaro_finale += "$"
    bwt_lista = list(stringa_dollaro_finale)
    return bwt_lista

def rotazione_lista (lista_dollaro):
    lista_dollaro = aggiunta_dollaro(lista_dollaro)
    
    contaCarattere=len(lista_dollaro)
    
    lista_rotata=[]

    for rotazione in range(contaCarattere) :
        temp = lista_dollaro[rotazione]
        lista_dollaro = lista_dollaro [1::]
        lista_dollaro.append(temp)
        lista_rotata += lista_dollaro
        print(lista_dollaro)
    return lista_rotata


stringa_input=input("inserisci la stringa in input: ")
rotazione_lista(stringa_input)

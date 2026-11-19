import socket

#importo la funzione che calcola tutta la bwt

from main import calcola_bwt

HOST = "127.0.0.1" #indirizzo del mio pc
PORT = 38555

#funzione che si occupa di mettere in ascolto il server
def apri_server(host, porta):
    #creo il socket TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #inserisco indirizzo e porta
    server.bind((host,porta))

    #metto il server in attesa di una chiamta dal client con .listen
    server.listen()
    print("server avviato. Attesa risposta client: ")
    return server

#funzione cHe riceve la parola inviata dal client
def ricevi_parola(connesione):
    #leggo i dati in byte e li trasformo in testo normale
    dati = connesione.recv(1024)
    parola = dati.decode("utf-8")
    return parola 

#funzione che riceve la parola dal client
def invia_risultato(connessione, risultato):
    #trasforma il testo in byte e lo invia
    connessione.sendall(risultato.endcode("utf-8"))

#funzione principale del server
def main():
    server = apri_server(HOST,PORT)

    #si aspetta che un client accetti e si colleghi
    connesione, indirizzo_client = server.accept()
    print(f"client collegato da: {indirizzo_client}")

    parola = ricevi_parola(connesione)
    print(f"Parola ricevuta: {parola}")

    risultato_bwt = calcola_bwt(parola)
    print(f"BWT calcolata: {risultato_bwt}")

    invia_risultato(connesione,risultato_bwt)

    #chiudo la connnesione ed il server
    connesione.close()
    server.close()

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
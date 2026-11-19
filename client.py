import socket

HOST = "127.0.0.1"
PORT = 38555

#funzione per creare il client e collegarlo al server
def collegamento_server(host,porta):
    #creao il socket TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #collegamento con il server
    client.connect((host,porta))
    return client

def invia_parola(client, parola):
    #converto la parola in byte e la invio
    client.sendall(parola.endcode("utf-8"))

# Funzione che riceve la risposta dal server
def ricevi_risposta(client):
    #risposta in byte e la ritrasformo in testo
    dati = client.recv(1024)
    risposta = dati.decode("utf-8")
    return risposta
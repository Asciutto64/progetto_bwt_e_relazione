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

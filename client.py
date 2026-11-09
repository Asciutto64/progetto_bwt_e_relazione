import socket

def run_client():
    HOST = '127.0.0.1' 
    PORT = 65432        
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
        client_sock.connect((HOST, PORT))
        
        messaggio = input("Inserisci il testo da inviare al server: ")
        
        client_sock.sendall(messaggio.encode('utf-8'))

        
        data = client_sock.recv(1024)
        risposta_server = data.decode('utf-8')
        
        print("\n--- RISULTATO RICEVUTO ---")
        
        
        if "|" in risposta_server:
            stringa_bwt, indice = risposta_server.split("|", 1)
            print(f"Stringa BWT: {stringa_bwt}")
            print(f"Indice BWT : {indice}")
        else:
            
            print(f"Risposta grezza: {risposta_server}")

if __name__ == '__main__':
    run_client()


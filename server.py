import socket

from main import  burrows_wheeler_transform

def run_server():
    HOST = '127.0.0.1'
    PORT = 32000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.bind((HOST, PORT))
        server_sock.listen()
        print(f"[*] Server in ascolto su {HOST}:{PORT}...")

        conn, addr = server_sock.accept()
        with conn:
            print(f"[+] Connessione stabilita con {addr}")
            
            data = conn.recv(1024)
            if data:
                messaggio = data.decode('utf-8')
                print(f"[*] Ricevuto dal client: {messaggio}")

                trasformata = burrows_wheeler_transform(messaggio)
                print(f"[*] Trasformata di Burrows-Wheeler applicata.")

                conn.sendall(trasformata.encode('utf-8'))

    print("[*] Server chiuso.")

if __name__ == '__main__':
    run_server()

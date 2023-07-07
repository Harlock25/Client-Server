import socket
import sys

def invia_comandi(s, comando):
    s.send(comando.encode())
    print("Messaggio inviato correttamente:", comando)

    data = s.recv(4096)
    if data:
        print("Risposta dal server:", data.decode())
    else:
        print("Nessuna risposta dal server")

def connessione_al_server(indirizzo_server):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(indirizzo_server)
        print(f"Connessione al server {indirizzo_server} stabilita")
    except socket.error as errore:
        print(f"Qualcosa è andato storto, sto uscendo...\n{errore}")
        sys.exit()
    
    while True:
        comando = input("Inserisci il comando: ")
        invia_comandi(s, comando)

if __name__ == "__main__":
    connessione_al_server(("192.168.40.1", 15000))

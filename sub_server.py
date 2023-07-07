import socket
import sys
import bot_promemoria

def ricevi_comandi(conn):
    while True:
        richiesta = conn.recv(4096)
        if not richiesta:
            break
        comando = richiesta.decode().strip()
        response = bot_promemoria.response(comando)
        conn.sendall(response.text.encode())

def sub_server(indirizzo, porta):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((indirizzo, porta))
    s.listen(1)
    print(f"Server inizializzato, in ascolto su {indirizzo}:{porta}")

    while True:
        conn, indirizzo_client = s.accept()
        print(f"Connessione stabilita con {indirizzo_client}")
        ricevi_comandi(conn)
        conn.close()

if __name__ == "__main__":
    sub_server("192.168.40.1", 15000)

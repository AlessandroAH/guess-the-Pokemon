import socket
import threading
from Quiz import Quiz
from thread import ClientThread

def main():
    LOCALHOST = "127.0.0.1"
    PORT = 8080
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((LOCALHOST, PORT))
    print("Server in ascolto")

    #quiz = Quiz()

    while True:
        server.listen(4)
        client_socket, client_address = server.accept()
        print("Nuova connessione da:", client_address)
        # Creazione di un nuovo thread per gestire la connessione
        new_thread = ClientThread(client_address, client_socket)
        new_thread.start()

if __name__ == "__main__":
    main()

import socket
import threading
from Quiz import Quiz

# Classe per gestire i client in modo concorrente
class ClientThread(threading.Thread):
    # Costruttore
    def __init__(self, client_address, client_socket):
        # Inizializzazione del thread
        threading.Thread.__init__(self)
        self.csocket = client_socket
        self.client_address = client_address
        #self.quiz = Quiz()
        print("Nuova connessione aggiunta:", client_address)
    
    # Metodo per eseguire il thread    
    def run(self):
        print("Connessione da:", self.client_address)
        print("CIAOOO")
        #Il gioco dura 10 round
        # for _ in range(10):
        #     question = self.quiz.get_next_question()
        #     if question is None:
        #         break
        #     # Invia la domanda al client come stringa
        #     question_str = ' '.join(question)
        #     self.csocket.send(question_str.encode())
            
        #     # Ricevi la risposta dal client e controlla se è corretta
        #     answer = self.csocket.recv(1024).decode()
            
        #     if answer == self.quiz.correct_answer:
        #         self.csocket.send("Corretto!".encode())
        #         points += 1
        #     else:
        #         self.csocket.send(f"Sbagliato! La risposta corretta era {self.quiz.correct_answer}.".encode())
        
        self.csocket.close()

# # Configurazione del server
# LOCALHOST = "127.0.0.1"
# PORT = 8080
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server.bind((LOCALHOST, PORT))
# print("Server in ascolto")

# # In attesa di connessioni
# while True:
#     # Accettare la connessione
#     server.listen(4)
#     (client_socket, client_address) = server.accept()
#     # Creazione di un nuovo thread per gestire la connessione
#     new_thread = ClientThread(client_address, client_socket)
#     new_thread.start()
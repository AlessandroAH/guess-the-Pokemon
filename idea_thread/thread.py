import socket
import threading
from Quiz import Quiz

# Classe per gestire i client in modo concorrente
class ClientThread(threading.Thread):
        
    # Costruttore
    def __init__(self, client_address, client_socket):
        threading.Thread.__init__(self)
        self.csocket = client_socket
        self.client_address = client_address
        self.running = True
        self.c_answer = ""
        print("Nuova connessione aggiunta:", client_address)
    
    # Metodo per inviare una domanda al client
    def send_question(self, question_str,correct_answer):
        self.csocket.send(question_str.encode())
        self.c_answer = correct_answer
    
    # Metodo per eseguire il thread    
    def run(self):
        while self.running:
            try:
                answer = self.csocket.recv(1024).decode()
                if answer:
                    if answer == self.c_answer:
                        self.csocket.send("Corretto!".encode())
                        print(f"Risposta ricevuta da {self.client_address}: {answer}")
                        break
                    else :
                        self.csocket.send(f"Sbagliato! La risposta corretta era {quiz.correct_answer}.".encode())
                        print(f"Risposta ricevuta da {self.client_address}: {answer}")
                        break
            except Exception as e:
                print(f"Errore nella connessione con {self.client_address}: {e}")
                break        
    
    # Metodo per fermare il thread
    def stop(self):
        self.running = False
        self.csocket.close()
        print("Connessione chiusa con:", self.client_address)
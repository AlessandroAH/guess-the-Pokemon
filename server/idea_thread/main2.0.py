import socket
import threading
import time
from Quiz import Quiz
from thread import ClientThread

# Metodo per gestire la risposta del client
def handle_answer(thread, quiz):
    answer = thread.csocket.recv(1024).decode()
    
    if answer == quiz.correct_answer:
        thread.csocket.send("Corretto!".encode())
    else:
        thread.csocket.send(f"Sbagliato! La risposta corretta era {quiz.correct_answer}.".encode())
    
    #thread.points += 1

# Main
def main():
    # Costanti
    LOCALHOST = "127.0.0.1"
    PORT = 8080
    players = 0
    
    # Creazione del server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((LOCALHOST, PORT))
    print("Server in ascolto")
    
    # Creazione di una lista di thread client
    client_threads = []

    while players < 1:  # in realta dovrebbe essere 2
        server.listen(4)
        client_socket, client_address = server.accept()
        print("Nuova connessione da:", client_address)
        # Creazione di un nuovo thread per gestire la connessione
        new_thread = ClientThread(client_address, client_socket)
        new_thread.start()
        client_threads.append(new_thread)
        players += 1
        time.sleep(5)
    
    print("Il gioco sta per iniziare!")
    
    #Inizia il gioco
    quiz = Quiz()
    
    for _ in range(10):
        print("Domanda")
        question = quiz.get_next_question()
        if question is None:
            break
        
        question_str = ' '.join(question)
        for thread in client_threads:
            thread.send_question(question_str, quiz.correct_answer)
        
        # Ricevi la risposta dai client e controlla se è corretta
        for thread in client_threads:
            threading.Thread(target=handle_answer, args=(thread, quiz)).start()

    # Chiudere i thread client
    for thread in client_threads:
        thread.stop()


if __name__ == "__main__":
    main()
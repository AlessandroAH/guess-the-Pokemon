from flask import Flask, jsonify, request
from flask_cors import CORS
from Quiz import Quiz

app = Flask(__name__)  # Crea un'applicazione Flask
quiz = Quiz()  # Crea un'istanza della classe Quiz
CORS(app)  # Abilita le richieste CORS per l'applicazione Flask
points = 0  # Inizializza i punti a zero

# Inizializza il quiz
@app.post('/gioca')
def start_quiz():
    question, options, image_url = quiz.get_next_question()  # Ottiene la prossima domanda
    if question:
        return jsonify({"question": question, "options": options, "image_url": image_url}), 200  # Ritorna la domanda, le opzioni e l'URL dell'immagine in formato JSON
    else:
        return jsonify({"message": "No more questions"}), 400  # Ritorna un messaggio di errore se non ci sono più domande

# Invia la risposta dell'utente
@app.post('/invia')
def submit_answer():
    answer = request.json.get('answer')  # Ottiene la risposta dal corpo della richiesta
    correct, question, options, image_url = quiz.submit_answer(answer)  # Invia la risposta e ottiene i risultati
    if quiz.turns == 10:
        return jsonify({"correct": correct, "finished": True, "score": quiz.score, "turns": quiz.turns})  # Se il quiz è terminato, ritorna il punteggio finale
    return jsonify({"correct": correct, "question": question, "options": options, "image_url": image_url, "score": quiz.score, "turns": quiz.turns})  # Ritorna i risultati della risposta corrente

# Riavvia il quiz
@app.post('/restart')
def restartQuiz():
    quiz.reset()  # Resetta lo stato del quiz
    return 'Quiz riavviato', 200  # Ritorna un messaggio di conferma

if __name__ == '__main__':
    #Inserisci l'indirizzo IP del tuo PC
    app.run(host='xxx.xxx.xxx.xxx', port=8000, debug=True)  # Avvia l'applicazione Flask

# Nota sulla rete: Assicurati che il tuo PC e il tuo telefono siano sulla stessa rete.
# Se stai cercando di connetterti attraverso Internet, potrebbe essere necessario configurare il port forwarding sul tuo router.
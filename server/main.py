from flask import Flask, jsonify, request
from flask_cors import CORS
from Quiz import Quiz

app = Flask(__name__)
quiz = Quiz()
CORS(app)  
points = 0

# Inizializza il quiz
@app.post('/gioca')
def start_quiz():
    question = quiz.get_next_question()
    return jsonify({"question": question}), 200

# Invia la risposta dell'utente
@app.post('/invia')
def submit_answer():
    answer = request.json.get('answer')
    correct, question = quiz.submit_answer(answer)
    if correct:
        return jsonify({"correct": True, "question": question, "score": quiz.score, "turns": quiz.turns})
    else:
        return jsonify({"correct": False, "question": question, "score": quiz.score, "turns": quiz.turns})

if __name__ == '__main__':
     app.run(host='172.22.169.183', port=8000, debug=True)
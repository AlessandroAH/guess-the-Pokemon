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
    question, options  = quiz.get_next_question()
    return jsonify({"question": question, "options":options}), 200

# Invia la risposta dell'utente
@app.post('/invia')
def submit_answer():
    answer = request.json.get('answer')
    correct, question, options = quiz.submit_answer(answer)
    if correct:
        return jsonify({"correct": True, "question": question, "options":options, "score": quiz.score, "turns": quiz.turns})
    else:
        return jsonify({"correct": False, "question": question, "options":options, "score": quiz.score, "turns": quiz.turns})

if __name__ == '__main__':
     app.run(host='192.168.228.220', port=8000, debug=True)
from flask import Flask, jsonify, request
from Quiz import Quiz

app = Flask(__name__)
quiz = Quiz()
points = 0

# Inizializza il quiz
@app.post('/gioca')
def start_quiz():
    question = quiz.get_next_question()
    return jsonify({"question": question})

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
    app.run(debug=True)
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
    question, options, image_url   = quiz.get_next_question()
    if question:
        return jsonify({"question": question, "options": options, "image_url": image_url}), 200
    else:
        return jsonify({"message": "No more questions"}), 400

# Invia la risposta dell'utente
@app.post('/invia')
def submit_answer():
    answer = request.json.get('answer')
    correct, question, options, image_url = quiz.submit_answer(answer)
    if correct:
        return jsonify({"correct": True, "question": question, "options":options, "image_url": image_url, "score": quiz.score, "turns": quiz.turns})
    else:
        return jsonify({"correct": False, "question": question, "options":options, "image_url": image_url, "score": quiz.score, "turns": quiz.turns})

@app.post('/restart')
def restartQuiz():
    quiz.reset()

if __name__ == '__main__':
     app.run(host='192.168.1.27', port=8000, debug=True)
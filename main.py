from flask import Flask, jsonify
from Quiz import Quiz

app = Flask(__name__)
quiz = Quiz()

@app.route('/')
def get_next_question():
    question = quiz.get_next_question()
    if question is None:
        return jsonify({"error": "No more questions available"}), 404
    else:
        return jsonify({"question": question})

if __name__ == '__main__':
    app.run(debug=True)

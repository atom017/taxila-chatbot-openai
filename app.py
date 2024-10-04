from flask import Flask, request, jsonify, render_template
from chatbot import answer_question

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.json['question']
    answer = answer_question(user_question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)

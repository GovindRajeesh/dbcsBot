from flask import Flask, render_template, request,jsonify
from bot import get_response

app = Flask(__name__)


# Define the homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Define the chatbot endpoint
@app.route('/chat', methods=['POST'])
def chatbot():
    data = request.get_json()
    message = data['message']

    # Call OpenAI API to generate chatbot response
    response = get_response(message)

    return jsonify(response=response)

if __name__ == '__main__':
    app.run(debug=True)

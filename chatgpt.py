from flask import Flask, request, jsonify
import openai

openai.api_key = 'SUA_CHAVE_DE_API_AQUI'

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data['message']
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        temperature=0.7
    )
    reply = response.choices[0].text.strip()
    return jsonify({'message': reply})

if __name__ == '__main__':
    app.run()

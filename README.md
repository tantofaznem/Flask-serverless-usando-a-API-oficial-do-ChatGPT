# Flask serverless usando a API oficial do ChatGPT
Para criar um ChatGPT serverless usando a API oficial do ChatGPT com Python, você precisará seguir estas etapas:

1. Obter uma chave de API

2. Configurar o ambiente
Criar um novo ambiente virtual para isolar as dependências do projeto
```
python -m venv chatgpt-env
```

Ativar o ambiente virtual:
Win:
```
chatgpt-env\Scripts\activate
```

Linux / MAC:
```
source chatgpt-env/bin/activate
```

3. Instalar as bibliotecas necessárias
```
pip install openai
pip install flask
```

4. Criar o arquivo 'chatgpt.py'

5. Importar as bibliotecas necessárias
```python
from flask import Flask, request, jsonify
import openai
```

6. Configurar a chave de API
```python
openai.api_key = 'SUA_CHAVE_DE_API_AQUI'
```

7. Criar uma instancia Flask
```python
app = Flask(__name__)
```

8. Definir a rota para a API
```python
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

9. Executar o servidor Flask
if __name__ == '__main__':
    app.run()
```

E PRONTO! O servidor Flask está pronto para receber solicitações POST na rota '/chat' e gerar respostas usando o modelo de linguagem do ChatGPT. Não se esqueça de substituir 'SUA_CHAVE_DE_API_AQUI' pela sua chave de API real.

Para testar seu servidor, você pode usar uma ferramenta como o cURL ou o Postman para enviar solicitações POST para a rota '/chat' com um corpo JSON contendo a mensagem do usuário. O servidor responderá com uma resposta gerada pelo modelo do ChatGPT.

EXEMPLO:
```JSON
{
  "message": "Como usar o Flask?"
}
```

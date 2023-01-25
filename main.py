from flask import Flask, request
from utils import sentimento_gpt3

app = Flask(__name__)


@app.route('/analise/', methods=['GET', 'POST'])
def analise_sentiment(content=None):
    if content:
        text = content.text
    else:
        try:
            content = request.get_json()
            text = content.get('text')
        except:
            return '\nErro ao tentar retirar informações do JSON'
    return sentimento_gpt3(text)[0] + '--' + sentimento_gpt3(text)[1]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, threaded=True)

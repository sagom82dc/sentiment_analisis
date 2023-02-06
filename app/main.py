from flask import Flask, request
from app.utils.functions import sentimento_gpt3
from fastapi import FastAPI, Request, Response
import json
import logging


def create_app():
    app = FastAPI()

    @app.get('/menssagem/{text}')
    async def sentiment(text: str):
        try:
            logging.info(f'Recibendo menssagem:{text}')
            response = sentimento_gpt3(text)
        except ValueError:
            return Response(status_code=500, content="Falha aplicando o analisis de sentimento")
        return json.dumps(response)

    return app

'''
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
'''
import requests


def analises_sentimento():
    r = requests.get(url='http://localhost:5050/menssagem/odeio seu serviço')
    assert r.status_code == 200
    print(r.content)


analises_sentimento()
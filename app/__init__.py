import json
from cryptography.fernet import Fernet
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(ROOT_DIR, '.key'), 'rb') as filekey:
    key = filekey.read()
fernet = Fernet(key)

with open(f'app/setup.json', 'rb') as enc_file:
    encrypted = enc_file.read()
decrypted = fernet.decrypt(encrypted)
SETUP = json.loads(decrypted.decode())

req_temp_sent = SETUP['GPT3']['sentiment_analysis']['setup']['temperature']
req_max_sent = SETUP['GPT3']['sentiment_analysis']['setup']['max_tokens']
req_stop_sent = SETUP['GPT3']['sentiment_analysis']['setup']['stop']
req_best_of_sent = SETUP['GPT3']['sentiment_analysis']['setup']['best_of']
req_top_p_sent = SETUP['GPT3']['sentiment_analysis']['setup']['top_p']
req_n_sent = SETUP['GPT3']['sentiment_analysis']['setup']['n']

GPT3_USER_SENT = os.getenv('GPT3_USER_SENT')
GPT3_PSWD_SENT = os.getenv('GPT3_PSWD_SENT')
GPT3ENDPOINT = os.getenv('GPT3ENDPOINT')
sent_source = SETUP['GPT3']['sentiment_analysis']['setup']['source']
req_model_sent = SETUP['GPT3']['sentiment_analysis']['setup']['model']
req_engine_sent = SETUP['GPT3']['sentiment_analysis']['setup']['engine']
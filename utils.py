from app import *
from requests import post
from datetime import datetime

# mlm = MainLoggerManager()


# def sent2_gpt3(text: str, context: 'Context', test_uni: bool = False) -> str:
def sentimento_gpt3(text: str):
    """Esta função usa GPT3 para escolher a frase mais coerente com a
     polaridade e a emoção do texto de entrada ou feedback do cliente.

    Arguments:
       text: Deve ser uma string com um texto contendo a mensagem do usuário.

    Return:
       Retorna uma resposta em string coerente com a emoção e polaridade identificada,
       caso não encontre nenhuma emoção ou polaridade considera a mensagem como neutra.

    Raises:
       Error: 'erro chamando a função sent2gpt3'

    Dependencies: GPT3
    """

    '''
    if not test_uni:

        if context.user_id == '123456789' or context.test_local or \
                not enable_gpt3_sent:
            return "Análise de Sentimento do GPT-3", 'neutro'
    '''

    print('call function: '+str(datetime.today()))  # --------------------

    # respostas que predeterminadas para cada emoção identificada
    resp_emotion = {'satisfação': 'Que bom que você ficou satisfeito. Seja sempre bem-vindo.',
                    'insatisfação': 'Lamento que sua experiência não tenha correspondido às suas expectativas. Vou me '
                                    'esforçar para melhorar o atendimento no futuro.',
                    'felicidade': 'Muito obrigado pelo seu feedback. Fico feliz em saber que você está gostando do '
                                  'meu atendimento.',
                    'tristeza': 'Lamento que você tenha tido uma experiência ruim. Vou me esforçar para fazer melhor.',
                    'otimismo': 'Eu aprecio o seu feedback. Seu otimismo é motivador para mim.',
                    'decepção': 'Lamento saber que você teve uma experiência frustrante, agradeço muito por ter '
                                'trazido esse problema à minha atenção.',
                    'orgulho': 'É maravilhoso saber que meu serviço foi util para você. Espero te atender novamente.',
                    'raiva': 'Vou revisar o que aconteciou, e trabalhar para te dar um melhor atendimento no futuro.'}

    # respostas que predeterminadas para polaridade identificada
    resp_polar = {'positivo': 'Muito obrigado. Para mim, é um prazer enorme poder te ajudar.',
                  'negativo': 'Seu feedback ajuda na melhora do meu serviço. Ate a proxima.',
                  # Prometemos que a sua próxima experiência será muito melhor do que esta'
                  'neutro': 'Obrigado. Eu realmente aprecio o seu feedback.'}

    positive_emotion = ("satisfação", "felicidade", "otimismo", "orgulho")
    negative_emotion = ("insatisfação", "tristeza", "decepção", "raiva")

    if text[-1] == ".":
        text = text
    else:
        text = text + "."

    # componentes do prompt:
    instruction2 = "identifique a emoção da seguinte frase: \n\n"  # instruçao principal

    # exemplos de clasificação
    frase_ex = "User: Seu atendimento foi bastante agradável. \nAI: positivo satisfação.\n\n" \
               "User: Você não me ajudou em nada, podia prestar um serviço melhor. \nAI: negativo insatisfação.\n\n" \
               "User: Obrigado, você fez meu dia melhor. \nAI: positivo felicidade.\n\n" \
               "User: Você só piorou o meu dia. \nAI: negativo tristeza.\n\n" \
               "User: Muito obrigado, esta de parabens. \nAI: positivo satisfação.\n\n" \
               "User: Com sua ajuda vou consegui melhorar meu trabalho. \nAI: positivo otimismo.\n\n" \
               "User: Você é decepcionante. \nAI: negativo decepção.\n\n" \
               "User: Estou orgulhoso de você ser uma ferramenta da empresa. \nAI: positivo otimismo.\n\n" \
               "User: seu atendimento é uma bosta. \nAI: negativo raiva.\n\n" \
               "User: O serviço foi bom, mas poderia melhorar. \nAI: neutro opinião.\n\n" \
               "User: Muito obrigado, esta de parabens. \nAI: positivo satisfação.\n\n"
    pr_text2 = instruction2 + frase_ex + "User: " + text + "\n"

    # f_error = False
    # response = None
    try:
        json_data = {'user': GPT3_USER_SENT,
                     'pswd': GPT3_PSWD_SENT,
                     'prompt': pr_text2,
                     'temperature': req_temp_sent,
                     'max_tokens': req_max_sent,
                     'stop': req_stop_sent,
                     'best_of': req_best_of_sent,
                     'top_p': req_top_p_sent,
                     'n': req_n_sent}

        if sent_source == 'fine-tune':
            json_data['model'] = req_model_sent
        else:
            json_data['engine'] = req_engine_sent
        print('start_gpt3req: ', str(datetime.today()), '\n')
        response = post(url=GPT3ENDPOINT,
                        json=json_data)
        print('end_gpt3req: ', str(datetime.today()), '\n')

        # print(response.content)
        sent = response.json()['choices'][0]['text']
        # print('gpt3_ok3')
    except:
        sent = 'AI: neutro não_emoção'
        # f_error = True
        # print('gpt3_nok')

    if len(sent.split(" ")) == 3:
        polarity = sent.split(" ")[-2]
        emotion = sent.split(" ")[-1]
    else:
        polarity = 'neutro'
        emotion = ''

    if emotion in resp_emotion:
        answer = resp_emotion[emotion]
        if emotion in positive_emotion:
            if polarity == "negativo":
                answer = resp_polar[polarity]
                emotion = polarity
        elif emotion in negative_emotion:
            if polarity == "positivo":
                answer = resp_polar[polarity]
                emotion = polarity
    elif polarity in resp_polar:
        answer = resp_polar[polarity]
        emotion = polarity
    else:
        answer = resp_polar['neutro']
        emotion = 'neutro'

    # if not test_uni:
    '''
    if f_error:
        mlm.main_logger(f'Erro na Chamada do Endpoint OpenAI client:{answer}', level="ERROR")
        mlm.main_logger(traceback.format_exc(), level="ERROR")
    else:
        mlm.main_logger('Chamada do Endpoint OpenAI client: ' + str(response.text))
    mlm.main_logger(f"Tempo de execucao do sent2_gpt3: {time() - start}")
    '''
    return answer, emotion


if __name__ == '__main__':
    print(sentimento_gpt3('odeio esse banco'))

from quadro import Quadro
from postIt import PostIt
import json


def salvar_quadro(quadro: Quadro):
    nome_arquivo = quadro.get_nome().lower().replace(" ", "") + '.json'

    data = {
        "nome": quadro.get_nome(),
        "postIts": []
    }

    for post in quadro.get_all_postIt():
        data['postIts'].append(
            json.dumps({"titulo": post.get_titulo(), "notas": post.get_notas(), "posicao": post.get_posicao()}))

    with open('quadros/' + nome_arquivo, 'w') as out:
        json.dump(data, out)


def abrir_arquivo(nome_arquivo: str):
    nome_arquivo = nome_arquivo.lower().replace(" ", "")

    if not nome_arquivo.endswith('.json'):
        nome_arquivo = nome_arquivo + '.json'

    try:
        with open('quadros/' + nome_arquivo) as json_arquivo:
            data = json.load(json_arquivo)

            quadro = Quadro(data['nome'])

            for str_post in data['postIts']:
                data_post = json.loads(str_post)
                post = PostIt(data_post['titulo'], data_post['notas'], data_post['posicao'])
                quadro.add_postIt(post)
    except:
        print("Quadro não pode ser encontrado!\n")
        return None
    return quadro

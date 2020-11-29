import json
import os

from colorama import Fore, Style
from postIt import PostIt
from postItDatado import PostItDatado
from quadro import Quadro


def salvar_quadro(quadro: Quadro):
    nome_arquivo = quadro.get_nome().lower().replace(" ", "") + '.json'

    data = {
        "nome": quadro.get_nome(),
        "postIts": []
    }

    for post in quadro.get_all_postIt():
        data_post = {"titulo": post.get_titulo(), "notas": post.get_notas(), "posicao": post.get_posicao(),
                     "data_limite": None}
        if isinstance(post, PostItDatado):
            data_post['data_limite'] = post.get_data_limite()

        data['postIts'].append(data_post)

    if not os.path.exists('quadros'):
        os.mkdir("quadros")

    with open('quadros/' + nome_arquivo, 'w') as out:
        json.dump(data, out, indent=4)


def abrir_arquivo(nome_arquivo: str):
    nome_arquivo = nome_arquivo.lower().replace(" ", "")

    if not nome_arquivo.endswith('.json'):
        nome_arquivo = nome_arquivo + '.json'

    try:
        with open('quadros/' + nome_arquivo) as json_arquivo:
            data = json.load(json_arquivo)

            quadro = Quadro(data['nome'])

            for str_post in data['postIts']:
                data_post = str_post

                if data_post['data_limite'] is not None:
                    post = PostItDatado(data_post['titulo'], data_post['notas'], data_post['data_limite'],
                                        data_post['posicao'])
                else:
                    post = PostIt(data_post['titulo'], data_post['notas'], data_post['posicao'])
                quadro.add_postIt(post)
                # quadro.get_all_postIt().sort(key=lambda post: post.get_posicao(), reverse=True)
    except Exception as e:
        print(Fore.RED, end="")
        print("\nQuadro não pode ser encontrado!\n")
        print(Style.RESET_ALL, end="")
        return None
    return quadro

from postIt import PostIt
from quadro import Quadro


def validar_entrada_postIt(titulo: str, anotacao: str):
    if len(titulo) > 26:
        print("Nome Inválido: Grande demais o limite é de 26 caracteres!")
        return "", "", True
    elif len(anotacao) > 240:
        print("Anotação Inválida: Grande demais o limite é de 240 caracteres!")
        return "", "", True
    else:
        return titulo, anotacao, False


def encontra_post(quadro: Quadro, posicao_post):
    for post in quadro.get_all_postIt():
        if post.get_posicao() == posicao_post:
            return post, False
    print("O quadro atual não possui uma nota nessa posição!")
    return None, True

from colorama import Fore, Style
from quadro import Quadro


def validar_entrada_postIt(titulo: str, anotacao: str, data_limite: str):
    if len(titulo) > 26:
        print(Fore.RED, end="")
        print("\nNome Inválido: Grande demais o limite é de 26 caracteres!\n")
        print(Style.RESET_ALL, end="")
        return "", "", None, True
    elif len(anotacao) > 240:
        print(Fore.RED, end="")
        print("\nAnotação Inválida: Grande demais o limite é de 240 caracteres!\n")
        print(Style.RESET_ALL, end="")
        return "", "", None, True
    elif len(data_limite) > 13:
        print(Fore.RED, end="")
        print("\nData Limite Inválida: A descrição da data limite é de no máximo 13 caracteres!\n")
        print(Style.RESET_ALL, end="")
        return "", "", None, True
    else:
        if len(data_limite.replace(" ", "")) == 0:
            data_limite = None
        return titulo, anotacao, data_limite, False


def encontra_post(quadro: Quadro, posicao_post):
    for post in quadro.get_all_postIt():
        if post.get_posicao() == posicao_post:
            return post, False
    print(Fore.RED, end="")
    print("\nO quadro atual não possui uma nota nessa posição!\n")
    print(Style.RESET_ALL, end="")
    return None, True

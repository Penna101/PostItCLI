import os
import buffer
import math
from quadro import Quadro
from postIt import PostIt


class Escolhas:
    MENU_INICIAL = 1
    MENU_ESCOLHAS_QUADRO = 2

    CADASTRO_QUADRO = 1
    ACESSAR_QUADRO = 2
    SAIR = 5

    CADASTRO_POSTIT = 1
    EDITAR_POSTIT = 2
    ACESSAR_OUTRO_QUADRO = 3

    EDIT_POSICAO = 1
    EDIT_TITULO = 2
    EDIT_NOTAS = 3


def inicializar():
    nome_app()
    return escolhas_inicial()


def nome_app():
    limpar_tela()
    print(
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" +
        "\n                                     SISTEMA DE LEMBRETES VIRTUAIS CRIADO POR JOÃO PENNA ZANDONAI" +
        "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


def escolhas_inicial():
    print("(1) Cadastrar um novo Quadro")
    print("(2) Acessar um Quadro")
    print("(5) Sair do Programa")
    return int(input("\nQual opção deseja acessar? "))


def escolhas():
    print("(1) Cadastrar um novo PostIt")
    print("(2) Editar um PostIt")
    print("(3) Acessar outro Quadro")
    print("(5) Sair do Programa")
    return int(input("\nQual opção deseja acessar? "))


def cadastrar_quadro():
    limpar_tela()
    print(
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        "\n                                      CADASTRAR NOVO QUADRO"
        "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


def acessar_quadro(quadro: Quadro):
    limpar_tela()
    print(
       "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" +
        "\n{:{align}{width}}".format(quadro.get_nome().upper(), align="^", width=126) +
        "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    linhas_posts = []
    cont = 0
    for linha in range(0, math.ceil(len(quadro.get_all_postIt()) / 3)):
        linhas_posts.append([[], [], []])
        for coluna in range(0, 3):
            if cont < len(quadro.get_all_postIt()):
                linhas_posts[linha][coluna] = quadro.get_postIt(cont)
                cont += 1

    buffer.imprimir_posts_coloridos_matriz(linhas_posts)


def editar_postIt(postIt: PostIt):
    print("Editar o PostIt: {:02d} {}".format(postIt.get_posicao(), postIt.get_titulo()))
    print("(1) Trocar de Posição")
    print("(2) Alterar Título")
    print("(3) Alterar Anotação")
    print("(5) Sair Edição")

    return int(input("\nQual opção deseja acessar? "))


def limpar_tela():
    os.system('clear')

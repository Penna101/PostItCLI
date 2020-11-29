import math
import os

import buffer
from colorama import Fore, Style
from postIt import PostIt
from quadro import Quadro


class Escolhas:
    MENU_INICIAL = 1
    MENU_ESCOLHAS_QUADRO = 2

    CADASTRO_QUADRO = 1
    ACESSAR_QUADRO = 2
    SAIR = 5

    CADASTRO_POSTIT = 1
    EDITAR_POSTIT = 2
    REMOVER_POSTIT = 3
    ACESSAR_OUTRO_QUADRO = 4

    EDIT_POSICAO = 1
    EDIT_TITULO = 2
    EDIT_NOTAS = 3
    EDIT_DATA_LIMITE = 4

    ERRO_ENTRADA = 0


def inicializar():
    nome_app()
    return escolhas_inicial()


def nome_app():
    limpar_tela()
    print(Fore.CYAN)
    print(
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" +
        "\n                                     SISTEMA DE LEMBRETES VIRTUAIS CRIADO POR JOÃO PENNA ZANDONAI" +
        "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print(Style.RESET_ALL)


def tratar_input_menu():
    entrada = input("\nQual opção deseja acessar? ")
    try:
        entrada = int(entrada)
        return entrada
    except:
        print(Fore.RED, end="")
        print("\n{} NÃO É UMA ENTRADA VÁLIDA\n".format(entrada))
        print(Style.RESET_ALL, end="")
        return 0


def erro_escolha_novamente():
    print(Fore.RED, end="")
    print("\nESCOLHA UMA OPÇÃO DO MENU\n")
    print(Style.RESET_ALL, end="")


def escolhas_inicial():
    print(Fore.LIGHTWHITE_EX, end="")
    print("(1) Cadastrar um novo Quadro")
    print("(2) Acessar um Quadro")
    print("(5) Sair do Programa")

    return tratar_input_menu()


def escolhas():
    print(Fore.LIGHTWHITE_EX, end="")
    print("(1) Cadastrar um novo PostIt")
    print("(2) Editar um PostIt")
    print("(3) Remover um PostIt")
    print("(4) Acessar outro Quadro")
    print("(5) Sair do Programa")

    return tratar_input_menu()


def escolhas_editar_postIt(postIt: PostIt):
    print(Fore.LIGHTWHITE_EX, end="")
    print("Editar o PostIt: {:02d} - {}".format(postIt.get_posicao(), postIt.get_titulo()))
    print("(1) Trocar de Posição")
    print("(2) Alterar Título")
    print("(3) Alterar Anotação")
    print("(4) Alterar Data Limite")
    print("(5) Sair Edição")

    return tratar_input_menu()


def cadastrar_quadro():
    limpar_tela()
    print(Fore.CYAN)
    print(
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        "\n                                      CADASTRAR NOVO QUADRO"
        "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print(Style.RESET_ALL)


def acessar_quadro(quadro: Quadro):
    limpar_tela()
    print(Fore.LIGHTGREEN_EX)
    print("\n{:{align}{width}}".format("Você está Visualizando o Quadro:", align="^", width=126))
    print(
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" +
        "\n{:{align}{width}}".format(quadro.get_nome().upper(), align="^", width=126) +
        "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print(Style.RESET_ALL)

    linhas_posts = []
    cont = 0
    for linha in range(0, math.ceil(len(quadro.get_all_postIt()) / 3)):
        linhas_posts.append([[], [], []])
        for coluna in range(0, 3):
            if cont < len(quadro.get_all_postIt()):
                linhas_posts[linha][coluna] = quadro.get_postIt(cont)
                cont += 1

    buffer.imprimir_posts_coloridos_matriz(linhas_posts)


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

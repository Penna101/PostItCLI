from colorama import Fore, Back, Style

largura = 30
alinhamento = '^'


def imprimir_posts_coloridos(linhas_posts):
    linhas_format = divide_lista(linhas_posts)
    for linhas_posts_format in linhas_format:
        for linha in range(0, 11):
            for linha_post in linhas_posts_format:
                print((Fore.RED + "{separador}  " + Fore.YELLOW + "{linha_post}" + Fore.RED + "  {separador}").format(
                    separador="{}", linha_post=linha_post[linha]), end="")
            print()
    print(Style.RESET_ALL)


def imprimir_posts_coloridos_matriz(posts):
    for linha in range(0, len(posts)):
        for indice_print in range(0, 11):
            for coluna in range(0, 3):
                if posts[linha][coluna]:
                    print(
                        (Fore.RED + "{separador}  " + Fore.YELLOW + "{linha_post}" + Fore.RED + "  {separador}").format(
                            separador="{}", linha_post=posts[linha][coluna].linhas_post[indice_print]), end="")
            print()
    print(Style.RESET_ALL)


# Divide uma lista a cada 3 componentes gerando lista de listas
def divide_lista(lst):
    for i in range(0, len(lst), 3):
        yield lst[i:i + 3]

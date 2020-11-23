from postIt import PostIt
from quadro import Quadro
import menu
import arquivoService
import validador

# Mostra o cabeçalho Inicial
escolha = menu.inicializar()

# Inicializa a varíavel que dita qual menu está sendo utilizado
menu_atual = menu.Escolhas.MENU_INICIAL

# Inicializa a variavel do quadro atual
quadro = None

# Enquanto as escolher forem diferente a opção de sair a aplicação continuara funcionando
while escolha != menu.Escolhas.SAIR:

    # Menu quando não há nenhum quadro selecionado
    if menu_atual == menu.Escolhas.MENU_INICIAL:

        # Cadastro de um quadro novo, cria um arquivo .json com o nome do quadro criado e logo o acessa
        if escolha == menu.Escolhas.CADASTRO_QUADRO:
            menu.cadastrar_quadro()
            novo_quadro = Quadro(input("Nome do quadro: "))
            arquivoService.salvar_quadro(novo_quadro)
            menu.acessar_quadro(novo_quadro)
            quadro = novo_quadro
            menu_atual = menu.Escolhas.MENU_ESCOLHAS_QUADRO

        # Necessário digitar o nome do quadro que deseja acessar, o programa irá pesquisar nos arquivos .json
        elif escolha == menu.Escolhas.ACESSAR_QUADRO:
            quadro = arquivoService.abrir_arquivo(input("Nome quadro: "))
            if quadro is not None:
                menu.acessar_quadro(quadro)
                menu_atual = menu.Escolhas.MENU_ESCOLHAS_QUADRO

    # Menu quando tem um quadro selecionado
    elif menu_atual == menu.Escolhas.MENU_ESCOLHAS_QUADRO:

        # Cadastrar um post It com validação de tamanho para o título e anotação
        if escolha == menu.Escolhas.CADASTRO_POSTIT:
            titulo, notas, erro = \
                validador.validar_entrada_postIt(
                    input("(Opcional)Título do Post It (Máx 26 char): "),
                    input("Anotação(Maxímo de 240 caracteres):\n"))
            if erro is False:
                postIt = PostIt(titulo, notas, 1 + len(quadro.get_all_postIt()))
                quadro.add_postIt(postIt)
                menu.acessar_quadro(quadro)
                arquivoService.salvar_quadro(quadro)

        # Encontra um PostIt para edição pela posição dele
        elif escolha == menu.Escolhas.EDITAR_POSTIT:
            posicao_post = int(input("Posição do Post It a Editar(Posição é o número entre () ao lado do título: "))
            postIt, erro = validador.encontra_post(quadro, posicao_post)
            if erro is False:
                escolha_edit = menu.editar_postIt(postIt)

                # Edição de posição, troca de posição com outro Post It
                if escolha_edit == menu.Escolhas.EDIT_POSICAO:
                    posicao_post_troca = int(
                        input("Posição do Post It a trocar de posição com o Post It {}: ".format(postIt.get_posicao())))
                    post_troca, erro_edit = validador.encontra_post(quadro, posicao_post_troca)
                    if erro_edit is False:

                        # Remove os dois Post It a serem editados do quadro
                        quadro.remove_postIt(postIt)
                        quadro.remove_postIt(post_troca)

                        # Salva nos objetos a posição nova deles
                        nova_posicao = post_troca.get_posicao()
                        post_troca.set_posicao(postIt.get_posicao())
                        postIt.set_posicao(nova_posicao)

                        # Adiciona na lista de post its em quadro na posição nova deles
                        quadro.add_postIt_index(postIt, postIt.get_posicao() - 1)
                        quadro.add_postIt_index(post_troca, post_troca.get_posicao() - 1)

                        arquivoService.salvar_quadro(quadro)
                        menu.acessar_quadro(quadro)

                elif escolha_edit == menu.Escolhas.EDIT_TITULO:
                    novo_titulo = input("Digite o novo título: ")
                    novo_titulo, dump, erro_edit = validador.validar_entrada_postIt(novo_titulo, "")
                    if erro_edit is False:
                        postIt.set_titulo(novo_titulo)
                        arquivoService.salvar_quadro(quadro)
                        menu.acessar_quadro(quadro)

                elif escolha_edit == menu.Escolhas.EDIT_NOTAS:
                    nova_anotacao = input("Digite a nova anotação:\n")
                    dump, nova_anotacao, erro_edit = validador.validar_entrada_postIt("", nova_anotacao)
                    if erro_edit is False:
                        postIt.set_notas(nova_anotacao)
                        arquivoService.salvar_quadro(quadro)
                        menu.acessar_quadro(quadro)

                elif escolha_edit == menu.Escolhas.SAIR:
                    menu.acessar_quadro(quadro)

        elif escolha == menu.Escolhas.ACESSAR_OUTRO_QUADRO:
            quadro_novo = arquivoService.abrir_arquivo(input("Nome quadro: "))
            if quadro_novo is not None:
                quadro = quadro_novo
                menu.acessar_quadro(quadro)
                menu_atual = menu.Escolhas.MENU_ESCOLHAS_QUADRO

    # Mostra as escolhas possíveis dependendo de qual o menu atual
    if menu_atual == menu.Escolhas.MENU_INICIAL:
        escolha = menu.escolhas_inicial()
    elif menu_atual == menu.Escolhas.MENU_ESCOLHAS_QUADRO:
        escolha = menu.escolhas()

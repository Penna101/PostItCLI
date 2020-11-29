from postIt import PostIt


class PostItDatado(PostIt):

    def __init__(self, titulo, notas, data_limite, posicao=0):
        super().__init__(titulo, notas, posicao, False)
        self.__data_limite = data_limite
        self.__diagramar_nota()

    def get_data_limite(self):
        return self.__data_limite

    def set_data_limite(self, data_limite):
        self.__data_limite = data_limite

    def set_posicao(self, posicao):
        super().set_posicao(posicao)
        self.__diagramar_nota()

    def adicionar_linha_separacao_bottom(self):
        self.linhas_post.append(
            "==== Data Limite:{:{align}{width}}====".format(self.__data_limite, align="^", width="13"))

    def __diagramar_nota(self):
        if self.get_notas() is not None:
            self.linhas_notas = []
            self.linhas_post = []
            self.adicionar_linhas_notas()

            self.adicionar_linha_separacao_top()
            self.adicionar_linhas_post_conteudo()
            self.adicionar_linha_separacao_bottom()


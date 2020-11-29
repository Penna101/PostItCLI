class PostIt:

    def __init__(self, titulo, notas, posicao=0):
        self.__titulo = str(titulo).upper()
        self.__notas = str(notas)
        self.__linhas_notas = []
        self.linhas_post = []
        self.__posicao = posicao
        self._diagramar_nota()

    def get_posicao(self):
        return self.__posicao

    def set_posicao(self, posicao):
        self.__posicao = posicao
        self._diagramar_nota()

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo
        self._diagramar_nota()

    def get_notas(self):
        return self.__notas

    def set_notas(self, notas):
        self.__notas = notas
        self._diagramar_nota()

    def _adicionar_linhas_notas(self):
        i = 30
        notas = "{:{width}}".format(self.__notas, width=240)
        while True:
            if len(notas) > i:
                self.__linhas_notas.append(notas[:i])
                notas = notas[i:]
            else:
                self.__linhas_notas.append(notas)
                break

    def _adicionar_linhas_post_conteudo(self):
        self.linhas_post.append("||({posicao:02d}){titulo:{align}{width}}||".format(posicao=self.__posicao,
                                                                                    titulo=self.__titulo,
                                                                                    align="^",
                                                                                    width="26"))
        for linha in self.__linhas_notas:
            self.linhas_post.append("||{:{align}{width}}||".format(linha, align="^", width="30"))

    def _adicionar_linha_separacao_top(self):
        self.linhas_post.append("==================================")

    def _adicionar_linha_separacao_bottom(self):
        self.linhas_post.append("==================================")

    def _diagramar_nota(self):
        if self.__notas is not None:
            self.__linhas_notas = []
            self.linhas_post = []
            self._adicionar_linhas_notas()

            self._adicionar_linha_separacao_top()
            self._adicionar_linhas_post_conteudo()
            self._adicionar_linha_separacao_bottom()

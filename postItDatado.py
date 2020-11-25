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

    def __diagramar_nota(self):
        if self.get_notas() is not None:
            self.linhas_notas = []
            self.linhas_post = []
            i = 30
            notas = "{:{width}}".format(self.get_notas(), width=240)
            while True:
                if len(notas) > i:
                    self.linhas_notas.append(notas[:i])
                    notas = notas[i:]
                else:
                    self.linhas_notas.append(notas)
                    break

            self.linhas_post.append("==================================")
            self.linhas_post.append("||({posicao:02d}){titulo:{align}{width}}||".format(posicao=self.get_posicao(),
                                                                                        titulo=self.get_titulo(),
                                                                                        align="^",
                                                                                        width="26"))
            for linha in self.linhas_notas:
                self.linhas_post.append("||{:{align}{width}}||".format(linha, align="^", width="30"))
            self.linhas_post.append(
                "==== Data Limite:{:{align}{width}}====".format(self.__data_limite, align="^", width="13"))

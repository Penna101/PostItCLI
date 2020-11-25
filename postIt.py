class PostIt:

    def __init__(self, titulo, notas, posicao=0, isDiagramarAuto=True):
        self.__titulo = str(titulo).upper()
        self.__notas = str(notas)
        self.linhas_notas = []
        self.linhas_post = []
        self.__posicao = posicao
        if isDiagramarAuto:
            self.__diagramar_nota()

    def imprimir_post(self):
        for linha in self.linhas_post:
            print(linha)

    def imprimir_linha(self, linha):
        print("||{:{align}{width}}||".format(linha, align="^", width="30"))

    def imprimir_titulo(self):
        print("||{:{align}{width}}||".format(self.__titulo, align="^", width="30"))

    def pegar_linha(self, index):
        if len(self.linhas_notas) > index:
            return self.linhas_notas[index]

    def get_posicao(self):
        return self.__posicao

    def set_posicao(self, posicao):
        self.__posicao = posicao
        self.__diagramar_nota()

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo
        self.__diagramar_nota()

    def get_notas(self):
        return self.__notas

    def set_notas(self, notas):
        self.__notas = notas
        self.__diagramar_nota()

    def __diagramar_nota(self):
        if self.__notas is not None:
            self.linhas_notas = []
            self.linhas_post = []
            i = 30
            notas = "{:{width}}".format(self.__notas, width=240)
            while True:
                if len(notas) > i:
                    self.linhas_notas.append(notas[:i])
                    notas = notas[i:]
                else:
                    self.linhas_notas.append(notas)
                    break

            self.linhas_post.append("==================================")
            self.linhas_post.append("||({posicao:02d}){titulo:{align}{width}}||".format(posicao=self.__posicao,
                                                                                        titulo=self.__titulo,
                                                                                        align="^",
                                                                                        width="26"))
            for linha in self.linhas_notas:
                self.linhas_post.append("||{:{align}{width}}||".format(linha, align="^", width="30"))
            self.linhas_post.append("==================================")

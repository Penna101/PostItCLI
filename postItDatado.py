from postIt import PostIt


class PostItDatado(PostIt):

    def __init__(self, titulo, notas, data_limite, posicao=0):
        self.__data_limite = data_limite
        super().__init__(titulo, notas, posicao)

    def get_data_limite(self):
        return self.__data_limite

    def set_data_limite(self, data_limite):
        self.__data_limite = data_limite

    def _adicionar_linha_separacao_bottom(self):
        self.linhas_post.append(
            "==== Data Limite:{:{align}{width}}====".format(self.__data_limite, align="^", width="13"))

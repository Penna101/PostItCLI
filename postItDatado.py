from postIt import PostIt


class PostItDatado(PostIt):

    def __init__(self, titulo, notas, data_limite):
        super().__init__(titulo, notas)
        self.data_limite = data_limite

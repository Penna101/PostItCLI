class Quadro:

    def __init__(self, nome: str):
        self.__postIts = []
        self.__nome = nome

    def add_postIt(self, postIt):
        self.__postIts.append(postIt)
        self.__postIts.sort(key=lambda post: post.get_posicao())

    def set_postIts(self, postIts):
        self.__postIts = []
        self.__postIts = postIts

    def get_postIt(self, index):
        return self.__postIts[index]

    def get_all_postIt(self):
        return self.__postIts

    def remove_postIt(self, post):
        self.__postIts.remove(post)

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def organizar_posicao(self):
        for post in self.__postIts:
            post.set_posicao(self.__postIts.index(post) + 1)

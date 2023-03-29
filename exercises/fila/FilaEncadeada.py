from ObjFila import ObjFila

class FilaEncadeada:
    def __init__(self, max):
        self.__max = max
        self.__num_obj = 0
        self.__primeiro = None
        self.__ultimo = None

    @property
    def primeiro(self):
        return self.__primeiro

    @property
    def ultimo(self):
        return self.__ultimo

    def entrar(self, obj):
        if self.__num_obj == self.__max:
            raise Exception('Estouro de pilha.')

        obj = ObjFila(valor=obj)

        if self.__num_obj == 0:
            self.__primeiro = obj
            self.__ultimo = obj
        else:
            self.__ultimo.proximo = obj
            self.__ultimo = obj

        self.__num_obj += 1

    def sair(self):
        if not self.__primeiro:
            raise Exception('Pilha vazia.')

        p1 = self.__primeiro
        self.__primeiro = p1.proximo

        self.__num_obj -= 1

        return p1.valor

    def percorrer(self):
        if not self.primeiro:
            return 0

        n = 1
        iter = self.primeiro

        while iter and iter.proximo != None:
            iter = iter.proximo
            n += 1

        return n

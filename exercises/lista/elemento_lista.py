class ElementoLista:
    def __init__(self, valor, proximo=None):
        self.__valor = valor
        self.__proximo = proximo

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def proximo(self):
        return self.__proximo

    @proximo.setter
    def proximo(self, prx):
        self.__proximo = prx

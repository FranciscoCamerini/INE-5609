class ObjFila:
    def __init__(self, valor, proximo=None):
        self.__valor = valor
        self.__proximo = proximo

    def __str__(self):
        return '%s' % self.valor or 'Valor'

    @property
    def valor(self):
        return self.__valor

    @property
    def proximo(self):
        return self.__proximo

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @proximo.setter
    def proximo(self, prox):
        self.__proximo = prox


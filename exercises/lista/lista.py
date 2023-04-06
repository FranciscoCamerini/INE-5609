from elemento_lista import ElementoLista

class ListaEncadeada:
    def __init__(self):
        self.__primeiro = None
        self.__ultimo = None

    def __str__(self):
        string = ''
        iter = self.primeiro
        while iter:
            string += str(iter.valor)
            if iter.proximo:
                string += ' -> '
            iter = iter.proximo

        return string

    @property
    def primeiro(self):
        return self.__primeiro

    @property
    def ultimo(self):
        return self.__ultimo

    @primeiro.setter
    def primeiro(self, p):
        self.__primeiro = p

    @ultimo.setter
    def ultimo(self, u):
        self.__ultimo = u

    def insere_frente(self, valor):
        elemento = ElementoLista(valor, self.primeiro)
        self.primeiro = elemento

        if not self.ultimo:
            self.ultimo = elemento

    def insere_atras(self, valor):
        elemento = ElementoLista(valor)

        if self.ultimo:
            self.ultimo.proximo = elemento

        if not self.primeiro:
            self.primeiro = elemento

        self.ultimo = elemento

    def remove_primero(self):
        if self.primeiro and self.primeiro.proximo:
            self.primeiro = self.primeiro.proximo
        else:
            self.primeiro = None

    def remove_ultimo(self):
        if self.primeiro and self.primeiro.proximo:
            iter = self.primeiro
            while iter.proximo and iter.proximo.proximo:
                iter = iter.proximo

            iter.proximo = None
            self.ultimo = iter
        else:
            self.primeiro = None

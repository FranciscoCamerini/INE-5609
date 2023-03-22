from fila_exceptions import FilaCheiaException, FilaVaziaException

class Fila:
    def __init__(self, size=100):
        self._fila = []
        self._inicio = 0
        self._fim = 0
        self._tamanho = size
        self._n_elementos = 0

    def __str__(self):
        return "%s" % self._fila

    @property
    def primeiro(self):
        return self._fila[self._inicio]

    @property
    def vazia(self):
        return self._n_elementos == 0

    @property
    def cheia(self):
        return self._n_elementos == self._tamanho

    def entrar(self, valor):
        if self.cheia:
            raise FilaCheiaException('Fila cheia!')

        self._fila[self._fim] = valor
        self._fim = (self._fim + 1) % self._tamanho
        self._n_elementos += 1

    def sair(self):
        if self.vazia:
            raise FilaVaziaException('Fila vazia!')

        valor = self._fila[self._inicio]
        self._inicio = (self._inicio + 1) % self._tamanho
        self._n_elementos -= 1

        return valor

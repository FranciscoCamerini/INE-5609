class ListaCheiaException(BaseException):
    def __init__(self):
        super().__init__('Tamanho máximo da Lista atingido!')

class IndiceInexistenteException(BaseException):
    def __init__(self, i):
        super().__init__('Índice %s inexiste na ListaGloriosa' % i)

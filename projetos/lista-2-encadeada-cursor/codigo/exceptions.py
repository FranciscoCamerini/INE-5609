class ListaCheiaException(BaseException):
    def __init__(self):
        super().__init__('Tamanho máximo da ListaGloriosa atingido!')

class ListaVaziaException(BaseException):
    def __init__(self):
        super().__init__('A ListaGloriosa está vazia!')

class IndiceInexistenteException(BaseException):
    def __init__(self, i):
        super().__init__('Índice %s inexiste na ListaGloriosa' % i)

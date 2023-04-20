class ListaCheiaException(BaseException):
    def __init__(self):
        super().__init__('Tamanho máximo da Lista atingido!')

from elemento import Elemento
from exceptions import ListaCheiaException

class Lista:
    def __init__(self, max):
        self.__max = max
        self.__n_elementos = 0
        self.__primeiro = Elemento(valor=None)
        self.__ultimo = Elemento(valor=None)
        self.__cursor = self.__primeiro

    def __str__(self):
        # Printa a lista, elemento onde o cursor está é cercado por '()'

        string = '['
        iterador = self.__primeiro
        while iterador.valor is not None:
            string += f'({iterador.valor})' if self.__cursor == iterador else f'{iterador.valor}'
            if iterador.proximo:
                string += ' -> '
                iterador = iterador.proximo
            else:
                break

        return string + ']'

    def __avanca_cursor(self, pos: int = 1) -> None:
        for _ in range(pos):
            if proximo := self.__cursor.proximo:
                self.__cursor = proximo

    def __retrocede_cursor(self, pos: int = 1) -> None:
        for _ in range(pos):
            if anterior := self.__cursor.anterior:
                self.__cursor = anterior

    def __move_cursor_posicao(self, pos) -> None:
        indice_ultimo = self.__n_elementos - 1

        if pos < indice_ultimo / 2 and pos >= 0:
            self.__move_cursor_inicio()
            self.__avanca_cursor(pos)
        else:
            self.__move_cursor_final()
            if pos > 0:
                self.__retrocede_cursor(indice_ultimo - pos)
            else:
                pos *= -1
                self.__retrocede_cursor(pos -  1)

    def __move_cursor_inicio(self) -> None:
        self.__cursor = self.__primeiro

    def __move_cursor_final(self) -> None:
        self.__cursor = self.__ultimo

    def __avisa_se_cheia(self) -> ListaCheiaException:
        if self.cheia():
            raise ListaCheiaException()

    @property
    def comprimento(self) -> int:
        return self.__n_elementos

    def vazia(self) -> bool:
        return self.comprimento == 0

    def cheia(self) -> bool:
        return self.comprimento == self.__max

    def acessa_atual(self) -> any:
        return self.__cursor.valor

    def acessa_posicao(self, pos) -> any:
        self.__move_cursor_posicao(pos)
        return self.acessa_atual()

    def inserir_como_atual(self, valor) -> None:
        if not self.__cursor.valor:
            self.__n_elementos += 1

        self.__cursor.valor = valor

    def inserir_antes_atual(self, valor) -> None:
        self.__avisa_se_cheia()
        elemento = Elemento(valor=valor, proximo=self.__cursor)

        if anterior_do_atual := self.__cursor.anterior:
            anterior_do_atual.proximo = elemento
        else:
            self.__primeiro = elemento

        self.__cursor.anterior = elemento
        self.__cursor = elemento
        self.__n_elementos += 1

    def inserir_apos_atual(self, valor) -> None:
        self.__avisa_se_cheia()
        elemento = Elemento(valor=valor, anterior=self.__cursor)

        if proximo_do_atual := self.__cursor.proximo:
            proximo_do_atual.anterior = elemento
            elemento.proximo = proximo_do_atual
        else:
            self.__ultimo = elemento

        self.__cursor.proximo = elemento
        self.__cursor = elemento
        self.__n_elementos += 1

    def inserir_como_ultimo(self, valor) -> None:
        self.__move_cursor_final()
        self.inserir_apos_atual(valor)

    def inserir_como_primeiro(self, valor) -> None:
        self.__move_cursor_inicio()
        self.inserir_antes_atual(valor)

    def inserir_posicao(self, pos, valor) -> None:
        self.__avisa_se_cheia()

        self.__move_cursor_posicao(pos)
        self.inserir_como_atual(valor)

    def excluir_atual(self) -> None:
        atual = self.__cursor

        if atual.anterior and atual.proximo:
            atual.anterior.proximo = atual.proximo
            atual.proximo.anterior = atual.anterior
            self.__cursor = atual.proximo
        elif proximo := atual.proximo:
            proximo.anterior = None
            self.__cursor = proximo
            self.__primeiro = proximo
        elif anterior := atual.anterior:
            anterior.proximo = None
            self.__cursor = anterior
            self.__ultimo = anterior

        self.__n_elementos -= 1

    def excluir_primeiro(self) -> None:
        self.__move_cursor_inicio()
        self.excluir_atual()

    def excluir_ultimo(self) -> None:
        self.__move_cursor_final()
        self.excluir_atual()

    def excluir_posicao(self, pos) -> None:
        self.__move_cursor_posicao(pos)
        self.excluir_atual()

    def excluir_elemento(self, valor) -> None:
        # Excluir todos os elementos da lista com determinado valor

        self.__move_cursor_inicio()
        n = self.comprimento
        for i in range(n):
            if self.acessa_atual() == valor:
                self.excluir_atual()
            else:
                self.__avanca_cursor(1)

    def busca(self, valor) -> bool:
        self.__move_cursor_inicio()

        for i in range(self.comprimento):
            if self.acessa_atual() == valor:
                return True
            self.__avanca_cursor(1)

        return False

    def posicao_de(self, valor) -> int:
        self.__move_cursor_inicio()

        for i in range(self.comprimento):
            if self.acessa_atual() == valor:
                return i
            self.__avanca_cursor(1)

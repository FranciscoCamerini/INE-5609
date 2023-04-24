from .elemento import Elemento
from .exceptions import ListaCheiaException, IndiceInexistenteException

class ListaGloriosa:
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
            if iterador.proximo and iterador.proximo.valor is not None:
                string += ' -> '
                iterador = iterador.proximo
            else:
                break

        return string + ']'

    def __avisa_se_cheia(self) -> ListaCheiaException:
        if self.cheia():
            raise ListaCheiaException()

    def avanca_cursor(self, pos: int = 1, erro_se_inexistente=False) -> None:
        for _ in range(pos):
            if proximo := self.__cursor.proximo:
                self.__cursor = proximo
            elif erro_se_inexistente:
                raise IndiceInexistenteException(pos + 1)

    def retrocede_cursor(self, pos: int = 1, erro_se_inexistente=False) -> None:
        for _ in range(pos):
            if anterior := self.__cursor.anterior:
                self.__cursor = anterior
            elif erro_se_inexistente:
                raise IndiceInexistenteException(pos - 1)

    def move_cursor_posicao(self, i: int) -> None:
        indice_ultimo = self.__n_elementos - 1

        if i > 0 and i > indice_ultimo:
            raise IndiceInexistenteException(i)
        elif i < 0 and i * -1 - 1 > indice_ultimo:
            raise IndiceInexistenteException(i)

        # Vemos se o índice está mais próximo do inicio ou final da lista, assim, percorremos menos elementos ao deslocar o cursor.
        if i < indice_ultimo / 2 and i >= 0:
            self.move_cursor_inicio()
            self.avanca_cursor(i, erro_se_inexistente=True)
        else:
            self.move_cursor_final()
            if i > 0:
                self.retrocede_cursor(indice_ultimo - i, erro_se_inexistente=True)
            else:
                i *= -1
                self.retrocede_cursor(i -  1, erro_se_inexistente=True)

    def move_cursor_inicio(self) -> None:
        self.__cursor = self.__primeiro

    def move_cursor_final(self) -> None:
        self.__cursor = self.__ultimo

    def __proximo_do_cursor(self) -> any:
        if self.__cursor.proximo and self.__cursor.proximo.valor is not None:
            return self.__cursor.proximo

    def __anterior_ao_cursor(self) -> any:
        if self.__cursor.anterior and self.__cursor.anterior.valor is not None:
            return self.__cursor.anterior

    def proximo_do_cursor(self) -> any:
        if elemento := self.__proximo_do_cursor():
            return elemento.valor

    def anterior_ao_cursor(self) -> any:
        if elemento := self.__anterior_ao_cursor():
            return elemento.valor

    def comprimento(self) -> int:
        return self.__n_elementos

    def vazia(self) -> bool:
        return self.comprimento() == 0

    def cheia(self) -> bool:
        return self.comprimento() == self.__max

    def acessa_atual(self) -> any:
        return self.__cursor.valor

    def acessa_posicao(self, i: int) -> any:
        self.move_cursor_posicao(i)
        return self.acessa_atual()

    def inserir_como_atual(self, valor: any) -> None:
        if self.__cursor.valor is None:
            self.__n_elementos += 1

        self.__cursor.valor = valor

    def inserir_antes_atual(self, valor: any) -> None:
        self.__avisa_se_cheia()
        elemento = Elemento(valor=valor, proximo=self.__cursor)

        if anterior := self.__anterior_ao_cursor():
            elemento.anterior = anterior
            anterior.proximo = elemento
        else:
            self.__primeiro = elemento
            if self.__ultimo.valor is None:
                self.__ultimo = elemento

        self.__cursor.anterior = elemento
        self.__n_elementos += 1

    def inserir_apos_atual(self, valor: any) -> None:
        self.__avisa_se_cheia()
        elemento = Elemento(valor=valor, anterior=self.__cursor)

        if proximo := self.__proximo_do_cursor():
            elemento.proximo = proximo
            proximo.anterior = elemento
        else:
            self.__ultimo = elemento
            if self.__primeiro.valor is None:
                self.__primeiro = elemento

        self.__cursor.proximo = elemento
        self.__n_elementos += 1

    def inserir_como_ultimo(self, valor: any) -> None:
        cursor_inicio = self.__cursor

        self.move_cursor_final()
        self.inserir_apos_atual(valor)

        self.__cursor = cursor_inicio

    def inserir_como_primeiro(self, valor: any) -> None:
        cursor_inicio = self.__cursor

        self.move_cursor_inicio()
        self.inserir_antes_atual(valor)

        self.__cursor = cursor_inicio

    def inserir_posicao(self, i: int, valor: any) -> None:
        self.__avisa_se_cheia()

        cursor_inicio = self.__cursor

        self.move_cursor_posicao(i)
        self.inserir_como_atual(valor)

        self.__cursor = cursor_inicio

    def excluir_atual(self) -> None:
        atual = self.__cursor
        anterior = self.__anterior_ao_cursor()
        proximo = self.__proximo_do_cursor()

        if anterior and proximo:
            anterior.proximo = proximo
            proximo.anterior = anterior
            self.__cursor = atual.proximo
        elif proximo:
            proximo.anterior = None
            self.__cursor = proximo
            self.__primeiro = proximo
        elif anterior:
            anterior.proximo = None
            self.__cursor = anterior
            self.__ultimo = anterior

        self.__n_elementos -= 1

    def excluir_primeiro(self) -> None:
        cursor_inicio = self.__cursor

        self.move_cursor_inicio()
        retornar_cursor = False
        if cursor_inicio != self.__cursor:
            retornar_cursor = True

        self.excluir_atual()
        if retornar_cursor:
            self.__cursor = cursor_inicio

    def excluir_ultimo(self) -> None:
        cursor_inicio = self.__cursor

        self.move_cursor_final()
        retornar_cursor = False
        if cursor_inicio != self.__cursor:
            retornar_cursor = True

        self.excluir_atual()
        if retornar_cursor:
            self.__cursor = cursor_inicio

    def excluir_posicao(self, i: int) -> None:
        cursor_inicio = self.__cursor

        self.move_cursor_posicao(i)
        retornar_cursor = False
        if cursor_inicio != self.__cursor:
            retornar_cursor = True

        self.excluir_atual()
        if retornar_cursor:
            self.__cursor = cursor_inicio


    def excluir_elemento(self, valor: any) -> None:
        # Excluir todos os elementos da lista com determinado valor
        cursor_inicio = self.__cursor
        self.move_cursor_inicio()

        n = self.comprimento()
        for i in range(n):
            if self.acessa_atual() == valor:
                self.excluir_atual()
            else:
                self.avanca_cursor(1)

        if cursor_inicio.valor != valor:
            self.__cursor = cursor_inicio
        elif cursor_inicio.proximo and cursor_inicio.proximo.valor:
            self.__cursor = cursor_inicio.proximo
        elif cursor_inicio.anterior and cursor_inicio.anterior.valor:
            self.__cursor = cursor_inicio.anterior

    def busca(self, valor: any) -> bool:
        self.move_cursor_inicio()

        for i in range(self.comprimento()):
            if self.acessa_atual() == valor:
                return True
            self.avanca_cursor(1)

        return False

    def posicao_de(self, valor: any) -> int:
        self.move_cursor_inicio()

        for i in range(self.comprimento()):
            if self.acessa_atual() == valor:
                return i
            self.avanca_cursor(1)

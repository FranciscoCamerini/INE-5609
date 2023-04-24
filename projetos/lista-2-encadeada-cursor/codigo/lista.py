from .elemento import ElementoLista
from .exceptions import ListaCheiaException, IndiceInexistenteException, ListaVaziaException

class ListaGloriosa:
    def __init__(self, max):
        # Para facilitar algumas operações criamos um elemento fake que será nosso cursor, primeiro e ultimo elemento no início.
        elemento_inicial_fake = ElementoLista(valor=None)

        self.__max = max
        self.__n_elementos = 0
        self.__primeiro = elemento_inicial_fake
        self.__ultimo = elemento_inicial_fake
        self.__cursor = elemento_inicial_fake

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

    def primeiro(self):
        return self.__primeiro.valor if self.__primeiro else None

    def ultimo(self):
        return self.__ultimo.valor if self.__ultimo else None

    def __avisa_se_cheia(self) -> ListaCheiaException:
        if self.cheia():
            raise ListaCheiaException()

    def __avisa_se_vazia(self) -> ListaVaziaException:
        if self.vazia():
            raise ListaVaziaException()

    def __avanca_cursor(self, pos: int = 1, erro_se_inexistente=False) -> None:
        for _ in range(pos):
            if proximo := self.__cursor.proximo:
                self.__cursor = proximo
            elif erro_se_inexistente:
                raise IndiceInexistenteException(pos + 1)

    def __retrocede_cursor(self, pos: int = 1, erro_se_inexistente=False) -> None:
        for _ in range(pos):
            if anterior := self.__cursor.anterior:
                self.__cursor = anterior
            elif erro_se_inexistente:
                raise IndiceInexistenteException(pos - 1)

    def __move_cursor_posicao(self, i: int) -> None:
        indice_ultimo = self.__n_elementos - 1

        if i > 0 and i > indice_ultimo:
            raise IndiceInexistenteException(i)
        elif i < 0 and i * -1 - 1 > indice_ultimo:
            raise IndiceInexistenteException(i)

        # Vemos se o índice está mais próximo do inicio ou final da lista, assim, percorremos menos elementos ao deslocar o cursor.
        if i < indice_ultimo / 2 and i >= 0:
            self.__move_cursor_inicio()
            self.__avanca_cursor(i, erro_se_inexistente=True)
        else:
            self.__move_cursor_final()
            if i > 0:
                self.__retrocede_cursor(indice_ultimo - i, erro_se_inexistente=True)
            else:
                i *= -1
                self.__retrocede_cursor(i -  1, erro_se_inexistente=True)

    def __move_cursor_inicio(self) -> None:
        self.__cursor = self.__primeiro

    def __move_cursor_final(self) -> None:
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
        self.__move_cursor_posicao(i)
        return self.acessa_atual()

    def inserir_como_atual(self, valor: any) -> None:
        if self.__cursor.valor is None:
            self.__avisa_se_cheia()
            self.__n_elementos += 1

        self.__cursor.valor = valor

    def inserir_antes_atual(self, valor: any) -> None:
        self.__avisa_se_cheia()
        elemento = ElementoLista(valor=valor, proximo=self.__cursor)

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
        elemento = ElementoLista(valor=valor, anterior=self.__cursor)

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
        self.__avisa_se_cheia()

        if not self.vazia():
            elemento = ElementoLista(valor=valor, anterior=self.__ultimo)
            self.__ultimo.proximo = elemento
            self.__ultimo = elemento
        else:
            self.__ultimo.valor = valor

        self.__n_elementos += 1

    def inserir_como_primeiro(self, valor: any) -> None:
        self.__avisa_se_cheia()

        if not self.vazia():
            elemento = ElementoLista(valor=valor, proximo=self.__primeiro)
            self.__primeiro.anterior = elemento
            self.__primeiro = elemento
        else:
            self.__primeiro.valor = valor

        self.__n_elementos += 1

    def inserir_posicao(self, i: int, valor: any) -> None:
        self.__avisa_se_cheia()

        cursor_inicio = self.__cursor

        self.__move_cursor_posicao(i)
        self.inserir_como_atual(valor)

        self.__cursor = cursor_inicio

    def excluir_atual(self) -> None:
        self.__avisa_se_vazia()
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
        self.__avisa_se_vazia()

        p = self.__primeiro
        if p.proximo and p.proximo.valor is not None:
            self.__primeiro = p.proximo
            self.__primeiro.anterior = None
            if p == self.__cursor:
                self.__cursor = self.__primeiro

        self.__n_elementos -= 1

    def excluir_ultimo(self) -> None:
        self.__avisa_se_vazia()

        u = self.__ultimo
        if u.anterior and u.anterior.valor is not None:
            self.__ultimo = u.anterior
            self.__ultimo.proximo = None
            if u == self.__cursor:
                self.__cursor = self.__ultimo

        self.__n_elementos -= 1

    def excluir_posicao(self, i: int) -> None:
        self.__avisa_se_vazia()
        cursor_inicio = self.__cursor

        self.__move_cursor_posicao(i)
        retornar_cursor = False
        if cursor_inicio != self.__cursor:
            retornar_cursor = True

        self.excluir_atual()
        if retornar_cursor:
            self.__cursor = cursor_inicio


    def excluir_elemento(self, valor: any) -> None:
        # Excluir todos os elementos da lista com determinado valor
        iter = self.__primeiro
        while iter and iter.valor is not None:
            if iter.valor == valor:
                if iter == self.__primeiro:
                    self.__primeiro = iter.proximo

                if iter == self.__ultimo:
                    self.__ultimo = iter.anterior

                if iter == self.__cursor:
                    if iter.proximo and iter.proximo.valor:
                        self.__cursor = iter.proximo
                    elif iter.anterior and iter.anterior.valor:
                        self.__cursor = iter.anterior

                if iter.proximo:
                    iter.proximo.anterior = None

            iter = iter.proximo

    def busca(self, valor: any) -> bool:
        cursor_inicio = self.__cursor
        self.__move_cursor_inicio()

        for _ in range(self.comprimento()):
            if self.acessa_atual() == valor:
                return True
            self.__avanca_cursor(1)

        self.__cursor = cursor_inicio
        return False

    def posicao_de(self, valor: any) -> int:
        cursor_inicio = self.__cursor
        self.__move_cursor_inicio()

        for i in range(self.comprimento()):
            if self.acessa_atual() == valor:
                return i
            self.__avanca_cursor(1)

        self.__cursor = cursor_inicio

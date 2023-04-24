import time

from codigo.lista import ListaGloriosa

def tempo_pra_ler(t: int) -> None:
    time.sleep(t)

def mostra_lista(lista: ListaGloriosa) -> None:
    print('Aqui está a lista: ', lista)

if __name__ == '__main__':
    print('Olá, bem vindo a demonstração da ListaGloriosa.\n')
    tempo_pra_ler(1)

    print('Vamos começar instanciando uma lista:\n')
    tempo_pra_ler(1)
    print('lista = ListaGloriosa(max=10)')
    tempo_pra_ler(1)
    lista = ListaGloriosa(max=10)
    mostra_lista(lista)
    tempo_pra_ler(1.5)

    print('\nAgora, vamos user os métodos `inserir_como_primeiro` e `inserir_como_ultimo` para adicionar alguns números à lista\n')
    tempo_pra_ler(1)

    try:
        n1 = float(input('Primeiro número: '))
        n2 = float(input('Segundo número: '))
        n3 = float(input('Terceiro número: '))
    except:
        ...

    print('\nlista.inserir_como_primeiro(%s)' % n1)
    tempo_pra_ler(0.5)
    print('lista.inserir_como_primeiro(%s)' % n2)
    tempo_pra_ler(0.5)
    print('lista.inserir_como_ultimo(%s)\n' % n3)
    tempo_pra_ler(0.5)
    lista.inserir_como_primeiro(n1)
    lista.inserir_como_primeiro(n2)
    lista.inserir_como_ultimo(n3)
    tempo_pra_ler(1)
    mostra_lista(lista)
    print('Como podemos ver, a ordem dos elementos está como esperada.')
    tempo_pra_ler(2)
    print('Note que o último elemento está cercado por parênteses, estes parênteses simbolizam a posição do cursor da nossa lista')
    tempo_pra_ler(1.5)
    print('Podemos usar o método `retrocede_cursor` para centralizar o cursor no meio de nossa lista. E depois o método `insere_apos_atual` para inserir um novo elemento')
    tempo_pra_ler(2.5)
    print('\nlista.retrocede_cursor(pos=1)\n')
    lista.retrocede_cursor()
    mostra_lista(lista)
    tempo_pra_ler(1.5)
    n = float(input('\nDigite um número: '))
    print('\nlista.inserir_apos_atual(%s)\n' % n)
    tempo_pra_ler(1)
    lista.inserir_apos_atual(n)
    mostra_lista(lista)
    tempo_pra_ler(1.5)

    print('Para agilizar as coisas, vou adicionar mais uns números na lista, para em seguida, testarmos os métodos de exclusão de elementos.')
    tempo_pra_ler(1.5)
    lista.inserir_como_ultimo(42)
    lista.inserir_como_ultimo(-7)
    lista.inserir_como_ultimo(31)
    lista.inserir_como_ultimo(2)
    lista.inserir_como_ultimo(99)
    mostra_lista(lista)

    tempo_pra_ler(1)
    n = float(input('\nEscolha um número para ser excluido: '))
    tempo_pra_ler(1)
    print('lista.excluir_elemento(valor=%s)' % n)
    lista.excluir_elemento(n)
    tempo_pra_ler(1)
    mostra_lista(lista)
    tempo_pra_ler(1.5)

    i = int(input('\nEscolha um índice da lista (0..n) para ser exclúido: '))
    lista.excluir_posicao(pos=i)
    print('\nlista.excluir_posicao(pos=%s)' % i)
    tempo_pra_ler(1)
    mostra_lista(lista)
    tempo_pra_ler(1.5)

    print('\nAgora, vamos excluir o primeiro e o ultimo elemento.\n')
    tempo_pra_ler(1)
    lista.excluir_primeiro()
    lista.excluir_ultimo()
    print('lista.excluir_primeiro()')
    tempo_pra_ler(0.5)
    print('lista.excluir_ultimo()\n')
    mostra_lista(lista)
    tempo_pra_ler(1.5)

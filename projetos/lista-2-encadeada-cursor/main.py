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

    n1, n2, n3 = None, None, None
    while n1 is None or n2 is None or n3 is None:
        if n1 is None:
            try:
                n1 = float(input('Digite um número: '))
            except:
                print('O valor deve ser numérico.')
                continue
        if n2 is None:
            try:
                n2 = float(input('Outro número: '))
            except:
                print('O valor deve ser numérico.')
                continue

        if n3 is None:
            try:
                n3 = float(input('Outro número: '))
            except:
                print('O valor deve ser numérico.')
                continue

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
    print('Note que o primeiro elemento a ser inserido está cercado por parênteses, estes parênteses simbolizam a posição do cursor da nossa lista')
    tempo_pra_ler(1.5)
    print('Podemos usar o método `insere_apos_atual` para inserir um novo elemento após o cursor')
    tempo_pra_ler(2.5)
    tempo_pra_ler(1.5)
    n = None
    while n is None:
        try:
            n = float(input('\nDigite um número: '))
        except:
            print('O valor deve ser numérico.')
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
    n = None
    while n is None:
        try:
            n = float(input('\nEscolha um número para ser excluido: '))
        except:
            print('O valor deve ser numérico.')
    tempo_pra_ler(1)
    print('lista.excluir_elemento(valor=%s)' % n)
    lista.excluir_elemento(n)
    tempo_pra_ler(1)
    mostra_lista(lista)
    tempo_pra_ler(1.5)

    i = None
    while i is None:
        try:
            i = int(input('\nEscolha um índice da lista (0..n) para ser exclúido: '))
        except:
            print('O valor deve ser numérico.')

    lista.excluir_posicao(i=i)
    print('\nlista.excluir_posicao(i=%s)' % i)
    tempo_pra_ler(1)
    mostra_lista(lista)
    tempo_pra_ler(1.5)

    print('\nAgora, vamos excluir o primeiro e ultimo elemento.\n')
    tempo_pra_ler(1)
    lista.excluir_primeiro()
    lista.excluir_ultimo()
    print('lista.excluir_primeiro()')
    tempo_pra_ler(0.5)
    print('lista.excluir_ultimo()')
    tempo_pra_ler(0.5)
    mostra_lista(lista)
    tempo_pra_ler(2)

    print('\nAgora, vamos buscar por algum valor específico na lista')
    tempo_pra_ler(1)
    n = None
    while n is None:
        try:
            n = float(input('\nValor a ser buscado: '))
        except:
            print('O valor deve ser numérico.')
    tempo_pra_ler(0.5)
    print('\nboolean = lista.busca(%s)' % n)
    boolean = lista.busca(n)
    print('Valor está na lista? %s' % boolean)
    tempo_pra_ler(0.5)
    mostra_lista(lista)
    print('Perceba que o cursor foi deslocado para o elemento buscado. Caso o elemento buscado não exista, o cursor continua em sua posição original.')
    tempo_pra_ler(2)

    print('\nAgora digite um valor para acharmos seu índice na lista. Se o valor não estiver na lista, o método retornará None\n')
    tempo_pra_ler(1)
    n = None
    while n is None:
        try:
            n = float(input('\nValor: '))
        except:
            print('O valor deve ser numérico.')
    print('\ni = lista.posicao_de(valor=%s)' % n)
    tempo_pra_ler(1)
    i = lista.posicao_de(n)
    print('Índice: %s' % i)

    print('\nPor último, vamos inserir o valor 42, em um índice específico da lista. Este método suporta indexação negativa. (-1 = ultimo)')
    tempo_pra_ler(1)
    i = None
    while i is None:
        try:
            i = int(input('\nÍndice: '))
        except:
            print('O valor deve ser numérico.')
    lista.inserir_posicao(i, 42)
    print('\nlista.inserir_posicao(%s, 42)\n' % i)
    tempo_pra_ler(1)
    mostra_lista(lista)

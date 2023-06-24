from lista_invertida import ListaInvertida, COLUNAS_VALOR_CONTINUO


def exibir_resultado_busca(resultado):
    print("Resultado da busca:")
    if resultado:
        for chave_objeto in resultado:
            cadastro = lista_invertida.pega_cadastro(chave_objeto)
            print("Chave: {}".format(chave_objeto))
            for coluna, valor in cadastro.items():
                print("{}: {}".format(coluna, valor))
            print()
    else:
        print("Nenhum resultado encontrado.")
    print()


def buscar():
    coluna = input("Digite o nome da coluna para a busca: ").lower().strip()

    if coluna in COLUNAS_VALOR_CONTINUO:
        valor_1 = input("Digite o inicio do intervalo: ")
        valor_2 = input("Digite o final do intervalo: ")
        try:
            valor = [float(valor_1), float(valor_2)]
        except Exception:
            print("Valor inválidon\n")
            return buscar()
    else:
        valor = input("Digite o valor a ser buscado: ")

    resultado = lista_invertida.busca(coluna, valor)
    exibir_resultado_busca(resultado)


def buscar_composta():
    busca = input("Digite a busca composta (coluna1, valor1, coluna2, valor2): ").split(",")
    if len(busca) % 2 != 0:
        print("Busca inválida.")
        return

    resultado = lista_invertida.busca_and(*[b.strip().lower() for b in busca])
    exibir_resultado_busca(resultado)


def buscar_or():
    busca = input("Digite a busca composta com OR (coluna1, valor1, coluna2, valor2): ").split(",")
    if len(busca) % 2 != 0:
        print("Busca inválida.")
        return

    resultado = lista_invertida.busca_or(*[b.strip().lower() for b in busca])
    exibir_resultado_busca(resultado)


def incluir_elemento():
    lista_invertida.cadastro()
    print("Cadastro incluído com sucesso.")


def remover_elemento():
    chave = input("Digite a chave do cadastro a ser removido: ")
    lista_invertida.remove_cadastro(chave)
    print("Cadastro removido com sucesso.")


def exibir_todos_dados():
    dados = lista_invertida.pega_dados()
    if dados:
        print("Dados cadastrados:")
        for chave, cadastro in dados.items():
            print("Chave: {}".format(chave))
            for coluna, valor in cadastro.items():
                print("{}: {}".format(coluna, valor))
            print()
    else:
        print("Nenhum dado cadastrado.")
    print()


if __name__ == "__main__":
    lista_invertida = ListaInvertida()

    while True:
        print("---------- MENU ----------")
        print("1 - Busca Simples")
        print("2 - Busca Composta (AND)")
        print("3 - Busca Composta (OR)")
        print("4 - Incluir Elemento")
        print("5 - Remover Elemento")
        print("6 - Exibir Todos os Dados")
        print("0 - Sair")
        opcao = input("Digite a opção desejada: ")

        try:
            if opcao == "1":
                buscar()
            elif opcao == "2":
                buscar_composta()
            elif opcao == "3":
                buscar_or()
            elif opcao == "4":
                incluir_elemento()
            elif opcao == "5":
                remover_elemento()
            elif opcao == "6":
                exibir_todos_dados()
            elif opcao == "0":
                break
        except Exception as e:
            print("Ops, excessão executando operação: ", e)

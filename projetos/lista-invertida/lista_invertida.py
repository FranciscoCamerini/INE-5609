import json
import random
from pathlib import Path

from utils import chave_nome, chave_salario, chave_cidade, chave_cep, chave_coluna

CAMINHO_DADOS = Path(__file__).parent / "cadastros.json"

COLUNAS_VALOR_CONTINUO = { "salario" }
COLUNAS_VALOR_DISCRETO = { "nome", "cidade", "cep" }


class ListaInvertida:
    def __init__(self):
        self.__diretorios: dict = {
            "nome": {},
            "salario": {},
            "cidade": {},
            "cep": {},
        }

        if CAMINHO_DADOS.exists():
            with open(CAMINHO_DADOS, "r") as arquivo:
                self.__dados: dict = json.loads(arquivo.read())
        else:
            self.__dados = {}

        for chave_objeto, objeto in self.__dados.items():
            self.__insere_objeto_diretorios(chave_objeto, objeto)

    def __salva_dados(self):
        with open(CAMINHO_DADOS, "w") as arquivo:
            arquivo.write(json.dumps(self.__dados, indent=4))

    def __insere_objeto_diretorios(self, chave_objeto, objeto):
        self.__insere_diretorio("nome", chave_nome(objeto["nome"]), chave_objeto)
        self.__insere_diretorio("salario", chave_salario(objeto["salario"]), chave_objeto)
        self.__insere_diretorio("cidade", chave_cidade(objeto["cidade"]), chave_objeto)
        self.__insere_diretorio("cep", chave_cep(objeto["cep"]), chave_objeto)

    def __insere_diretorio(self, diretorio, chave, valor):
        if isinstance(valor, str):
            valor = valor.strip().lower()

        diretorio = self.__pega_diretorio(diretorio)
        if chave in diretorio:
            diretorio[str(chave)].append(valor)
        else:
            diretorio[str(chave)] = [valor]

    def __pega_diretorio(self, coluna):
        diretorio = self.__diretorios.get(coluna)
        if not isinstance(diretorio, dict):
            raise ValueError('Objeto não possui coluna "%s"' % coluna)

        return diretorio

    def __busca_discreta(self, coluna, valor):
        diretorio = self.__pega_diretorio(coluna)
        lista_diretorio = diretorio.get(chave_coluna(coluna, valor), [])

        objetos = set()

        if isinstance(valor, str):
            valor = valor.strip().lower()

        for chave_obj in lista_diretorio:
            if cadastro := self.pega_cadastro(chave_obj):
                try:
                    if cadastro[coluna].lower() == valor:
                        objetos.add(chave_obj)
                except AttributeError:
                    if cadastro[coluna] == valor:
                        objetos.add(chave_obj)

        return objetos

    def __busca_continua(self, coluna, intervalo):
        try:
            inicio, fim = intervalo[0], intervalo[1]
        except Exception:
            raise ValueError(
                'Valor de busca para coluna continua "%s" deve ser um iteravel contendo inicio e fim do intervalo'
                % coluna
            )

        chave_inicio = chave_coluna(coluna, inicio)
        chave_fim = chave_coluna(coluna, fim)
        diretorio = self.__pega_diretorio(coluna)

        alvos = set()
        for i in range(int(chave_inicio), int(chave_fim) + 1):
            lista = diretorio.get(str(i), [])
            for chave in lista:
                if inicio <= self.pega_cadastro(chave)[coluna] <= fim:
                    alvos.add(chave)

        return alvos

    def __busca_composta(self, *args):
        if len(args) % 2 != 0:
            raise ValueError("Argumentos inválidos para busca composta")

        resultados = []
        for i in range(0, len(args), 2):
            coluna, valor = args[i], args[i + 1]
            resultados.append(self.busca(coluna, valor))

        return resultados

    def busca(self, coluna, valor):
        coluna = coluna.strip().lower()

        def busca_multiplos_valores(coluna, valores):
            parametros = []
            for v in valores:
                parametros.extend([coluna, v])

            return self.busca_or(*parametros)

        if coluna in COLUNAS_VALOR_CONTINUO:
            if not isinstance(valor, (list, tuple, set)):
                raise ValueError("Valor para busca continua deve ser um iteravel representando um intervalo: %s" % valor)

            if any([isinstance(v, (list, tuple, set)) for v in valor]):
                return busca_multiplos_valores(coluna, valor)

            return self.__busca_continua(coluna, valor)
        elif coluna in COLUNAS_VALOR_DISCRETO:
            if isinstance(valor, (list, tuple, set)):
                return busca_multiplos_valores(coluna, valor)

            return self.__busca_discreta(coluna, valor)

    def busca_or(self, *args):
        resultados = self.__busca_composta(*args)
        return set().union(*resultados)

    def busca_and(self, *args):
        if resultados := self.__busca_composta(*args):
            return resultados[0].intersection(*resultados[1:])

        return set()

    def cadastro(self):
        while True:
            try:
                nome = input("Nome: ").strip().lower()
                salario = float(input("Salario: "))
                cidade = input("Cidade: ").strip().lower()
                cep = input("CEP: ").replace("-", "").replace(".", "")
                break
            except Exception:
                print("Valor inválido, tente novamente")
                self.cadastro()

        while True:
            chave_unica = str(random.randint(1, 9999))
            if not self.pega_cadastro(chave_unica):
                self.__dados[chave_unica] = {
                    "nome": nome,
                    "salario": salario,
                    "cidade": cidade,
                    "cep": cep,
                }
                break

        self.__insere_objeto_diretorios(chave_unica, self.pega_cadastro(chave_unica))
        self.__salva_dados()

    def pega_cadastro(self, chave):
        if isinstance(chave, (list, tuple, set)):
            return [self.pega_cadastro(c) for c in chave]

        return self.__dados.get(str(chave))

    def remove_cadastro(self, chave):
        self.__dados.pop(chave, None)

    def pega_dados(self):
        return self.__dados

    @property
    def diretorios(self):
        return self.__diretorios

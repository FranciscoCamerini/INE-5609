import json
import random
from pathlib import Path

from utils import chave_nome, chave_salario, chave_cidade, chave_cep, chave_coluna

CAMINHO_DADOS = Path(__file__).parent / "dados.json"
CAMINHO_DIRETORIOS = Path(__file__).parent / "diretorios.json"

COLUNAS_VALOR_CONTINUO = { "salario" }
COLUNAS_VALOR_DISCRETO = { "nome", "cidade", "cep" }


class ListaInvertida:
    def __init__(self):
        self.diretorios: dict = {
            "nome": {},
            "salario": {},
            "cidade": {},
            "cep": {},
        }

        with open(CAMINHO_DADOS, "r") as arquivo:
            self.dados: dict = json.loads(arquivo.read())

        if CAMINHO_DIRETORIOS.exists():
            with open(CAMINHO_DIRETORIOS, "r") as arquivo:
                self.diretorios = json.loads(arquivo.read())
        else:
            # Monta diretórios
            for chave_objeto, objeto in self.dados.items():
                self._insere_objeto_diretorios(chave_objeto, objeto)

            self._salva_diretorios()

    def _salva_dados(self):
        with open(CAMINHO_DADOS, "w") as arquivo:
            arquivo.write(json.dumps(self.dados, indent=4))

    def _insere_objeto_diretorios(self, chave_objeto, objeto):
        self._insere_diretorio("nome", chave_nome(objeto["nome"]), chave_objeto)
        self._insere_diretorio("salario", chave_salario(objeto["salario"]), chave_objeto)
        self._insere_diretorio("cidade", chave_cidade(objeto["cidade"]), chave_objeto)
        self._insere_diretorio("cep", chave_cep(objeto["cep"]), chave_objeto)

    def _salva_diretorios(self):
        CAMINHO_DIRETORIOS.touch(exist_ok=True)
        with open(CAMINHO_DIRETORIOS, "w") as arquivo:
            arquivo.write(json.dumps(self.diretorios, indent=4))

    def _insere_diretorio(self, diretorio, chave, valor):
        if isinstance(valor, str):
            valor = valor.strip().lower()

        diretorio = self.diretorios[diretorio]
        if chave in diretorio:
            diretorio[chave].append(valor)
        else:
            diretorio[chave] = [valor]

    def _pega_diretorio(self, coluna):
        if diretorio := self.diretorios.get(coluna):
            return diretorio

        raise ValueError('Objeto não possui coluna "%s"' % coluna)

    def _busca_discreta(self, coluna, valor):
        diretorio = self._pega_diretorio(coluna)
        lista_diretorio = diretorio.get(chave_coluna(coluna, valor))

        objetos = set()

        if isinstance(valor, str):
            valor = valor.strip().lower()

        for chave_obj in lista_diretorio:
            try:
                if self.dados.get(chave_obj, {}).get(coluna).lower() == valor:
                    objetos.add(chave_obj)
            except AttributeError:
                if self.dados.get(chave_obj, {}).get(coluna).lower() == valor:
                    objetos.add(chave_obj)

        return objetos

    def _busca_continua(self, coluna, intervalo: tuple):
        try:
            inicio, fim = intervalo[0], intervalo[1]
        except Exception:
            return ValueError(
                'Valor de busca para coluna quantitativa "%s" deve ser um iteravel contendo inicio e fim do intervalo'
                % coluna
            )

        chave_inicio = chave_coluna(coluna, inicio)
        chave_fim = chave_coluna(coluna, fim)
        diretorio = self._pega_diretorio(coluna)

        alvos = set()
        for i in range(int(chave_inicio), int(chave_fim) + 1):
            lista = diretorio.get(str(i) + '.0', [])
            for chave in lista:
                if inicio <= self.dados[chave][coluna] <= fim:
                    alvos.add(chave)

        return alvos

    def _busca_composta(self, *args):
        if len(args) % 2 != 0:
            raise ValueError("Argumentos inválidos para busca composta")

        resultados = []
        for i in range(0, len(args), 2):
            coluna, valor = args[i], args[i + 1]
            resultados.append(self.busca(coluna, valor))

        return resultados

    def busca(self, coluna, valor):
        coluna = coluna.strip().lower()

        if coluna in COLUNAS_VALOR_CONTINUO:
            return self._busca_continua(coluna, valor)
        elif coluna in COLUNAS_VALOR_DISCRETO:
            return self._busca_discreta(coluna, valor)

    def busca_or(self, *args):
        resultados = self._busca_composta(*args)

        return set().union(*resultados)

    def busca_and(self, *args):
        if resultados := self._busca_composta(*args):
            return resultados[1].intersection(*resultados[1:])

        return set()

    def _cadastro(self):
        nome = input("Nome: ").strip().lower()
        salario = float(input("Salario: "))
        cidade = input("Cidade: ").strip().lower()
        cep = input("CEP: ").replace("-", "").replace(".", "")

        while True:
            chave_unica = str(random.randint(1, 9999))
            if not self.dados.get(chave_unica):
                self.dados[chave_unica] = {
                    "nome": nome,
                    "salario": salario,
                    "cidade": cidade,
                    "cep": cep,
                }
                break

        return chave_unica

    def cadastro(self):
        chave_unica = None
        while not chave_unica:
            try:
                chave_unica = self._cadastro()
            except Exception:
                print("Valor inválido, tente novamente")
                self._cadastro()

        self._insere_objeto_diretorios(chave_unica, self.dados[chave_unica])
        self._salva_diretorios()
        self._salva_dados()

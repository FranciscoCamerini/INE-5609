# Documentação da Estrutura de Dados - ListaInvertida

A estrutura de dados `ListaInvertida` é responsável por armazenar e organizar um conjunto de dados de forma a facilitar a busca por diferentes critérios. Ela possui os seguintes métodos públicos:

## Construtor
```python
def __init__(self)
```
O construtor inicializa a estrutura de dados, carregando os dados do arquivo `cadastros.json` e construindo os diretórios para otimizar as buscas.

## Busca por Valor
```python
def busca(self, coluna, valor)
```
Realiza uma busca na estrutura de dados com base em **uma** coluna específica e um valor. A coluna indica o critério de busca desejado, enquanto o valor é o parâmetro a ser buscado. O método retorna um conjunto de chaves de objetos que correspondem ao critério de busca.


### Busca por colunas contínuas
Para as colunas de valor contínuo `salario`, o parâmetro `"valor"` deverá ser um iterável de dois valores representando um intervalo a ser buscado, por exemplo:
```python
    # Achar todos as chaves de objetos com "salario" entre 2500 e 5000
    lista = ListaInvertida()
    objetos = lista.busca("salario", [2500, 5000])
```

### Busca por colunas discretas
Para as demais colunas, de valores discretos, a busca se derá por valores exatos ao parâmetro `"valor"` de forma case-insensitive.
```python
    # Achar todos as chaves de objetos com "nome" = "Francisco"
    objetos = lista.busca("nome", "francisco")
```

**Importante**: Há também como se passar multiplos valores para a mesma coluna, passando uma lista de valores:
```python
    # Buscar todos os objeto com "nome" = "Thiago" OU "Gabriel"
    objetos = lista.busca("nome", ["thiago", "gabriel"])

    # Buscar todos os objeto com "salario" no intervalo de 1000 a 1500 OU 3000 a 4000
    objetos = lista.busca("nome", [
        [1000, 1500], [3000, 4000]
    ])
```



## Busca Lógica OR
```python
def busca_or(self, *args)
```
Realiza uma busca lógica OR na estrutura de dados por **mais de uma** coluna. Permite buscar objetos que correspondam a diferentes critérios de busca. Os argumentos são passados como pares de coluna e valor, indicando o critério de busca desejado para cada par. O método retorna um conjunto de chaves de objetos que correspondem a pelo menos um dos critérios de busca.

Exemplo:
```python
    # Achar todos as chaves de objetos com "nome" = "Francisco" OU "nome" = "Luiz" OU "nome" = "Pedro"
    objetos = lista.busca_or("nome", "francisco", "nome", "luiz", "nome", "pedro")

    # Achar todos as chaves de objetos com "cidade" = "Florianopolis" OU "salario" entre 4000 e 10000
    objetos = lista.busca_or("cidade", "florianopolis", "salario", [4000, 10000])
```

## Busca Lógica AND
```python
def busca_and(self, *args)
```
Realiza uma busca lógica AND na estrutura de dados. Permite buscar objetos que correspondam a todos os critérios de busca especificados. Os argumentos são passados como pares de coluna e valor, indicando o critério de busca desejado para cada par. O método retorna um conjunto de chaves de objetos que correspondem a todos os critérios de busca.

Exemplo:
```python
    # Achar todos as chaves de objetos com "nome" = ("Francisco" OU "Gabriel") AND "cidade" = "Joinville" AND "salario" entre 1200 e 3500
    objetos = lista.busca_and("nome", ["francisco", "gabriel"], "cidade", "joinville", "salario", [1200, 3500])
```

## Acesso a Cadastro
```python
def acessa_cadastro(self, chave_unica)
```
Acessa o objeto correspondente a `"chave_unica"` no arquivo de dados. Retorna `None` caso o objeto não exista.


## Remoção de Cadastro
```python
def remove_cadastro(self, chave_unica)
```
Remove o cadastro dos dados correspondente a `"chave_unica"`.

## Realizar Cadastro
```python
def cadastro(self)
```
Realiza o cadastro de um novo objeto na estrutura de dados. Solicita ao usuário as informações necessárias, como nome, salário, cidade e CEP. O objeto é adicionado à estrutura de dados e aos diretórios correspondentes, e os dados são salvos no arquivo `cadastros.json`.

## Acesso aos Dados
```python
def pega_dados(self)
```
Retorna os dados do arquivo `cadastros.json` como um dicionário.

## Observações
- Existem dois tipos de colunas: colunas de valor contínuo e colunas de valor discreto. As colunas de valor contínuo são: "salario". As colunas de valor discreto são: "nome", "cidade" e "cep".
- A estrutura de dados utiliza uma técnica conhecida como "lista invertida", na qual são construídos diretórios para cada coluna, permitindo uma busca mais eficiente.
- Os métodos de busca permitem buscar por um valor exato em uma coluna discreta ou por um intervalo de valores em uma coluna contínua.
- Os métodos de busca lógica OR e AND permitem buscar por objetos que correspondam a múltiplos critérios de busca, combinando colunas e valores diferentes.
- A estrutura de dados é persistente, ou seja, os dados são salvos em arquivos e podem ser carregados novamente em uma execução subsequente
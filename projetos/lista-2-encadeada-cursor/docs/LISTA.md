# Trabalho 1 - INE5609 - Estruturas de Dados

<strong>Alunos</strong>: Francisco Camerini (22100898), Luiz Felipe Scheidt (22100914).

Lista duplamente encadeada com cursor desenvolvida em Python.

## Métodos

A classe <strong>ListaGloriosa</strong>, encontrada dentro do arquivo <b>lista.py</b> dispõe dos seguintes métodos para armazenamento e consulta de dados.

### Construtor
O construtor da classe recebe um parametro `"max"`, que deve ser um número inteiro. Este valor será o número máximo de elementos que a <b>ListaGloriosa</b> armazenará.
```python
minha_lista = ListaGloriosa(max=99) # instancia uma lista que armazenará no máximo 99 elementos.
```


### Sobre o cursor

#### `avanca_cursor(pos: int = 1, erro_se_inexistente: bool = False) -> None`
Avança o cursor da lista o número de posições indicados em `"pos"`.

Este método recebe um parâmetro booleano `"erro_se_inexistente"`, se `True`, o método levantará uma excessão `IndiceInexistenteException` caso a posição desejada esteja fora dos limites da lista. Caso contrário, o cursor irá até onde for possível, sem levantar erros. Por padrão o valor deste parametro é `False`.

#### `retrocede_cursor(pos: int = 1, erro_se_inexistente: bool = False) -> None`
Retrocede o cursor da lista o número de posições indicados em `"pos"`.

Este método recebe um parâmetro booleano `"erro_se_inexistente"`, se `True`, o método levantará uma excessão `IndiceInexistenteException` caso a posição desejada esteja fora dos limites da lista. Caso contrário, o cursor irá até onde for possível, sem levantar erros. Por padrão o valor deste parametro é `False`.

#### `move_cursor_posicao(i: int) -> None`
Move o cursor da lista para o índice indicado em `"i"`. (Lembrando que o primeiro índice da lista é 0)

Este método suporta indexação negativa, `-1` representa o último índice da lista, `-2` o penúltimo, e assim por diante.

#### `move_cursor_inicio() -> None`
Move o cursor para o primeiro elemento da lista.

#### `move_cursor_final() -> None`
Move o cursor para o último elemento da lista.

### Sobre a Estrutura

#### `acessa_atual() -> any`
Retorna o valor do elemento armazenado na posição apontada pelo cursor.

#### `acessa_posicao(i: int) -> any`
Retorna o valor do elemento armazenado no índice `"i"`. (Lembrando que o primeiro índice da lista é 0)

Caso o  indice `"i"` esteja fora dos limites da lista, será levantada uma `IndiceInexistenteException`.

#### `inserir_como_atual(valor: any) -> None`
Insere `"valor"` no elemento apontado pelo cursor.

Se a lista estiver cheia, levanta `ListaCheiaException`.

#### `inserir_antes_atual(valor: any) -> None`
Insere `"valor"` como antecessor do elemento apontado pelo cursor.

Se a lista estiver cheia, levanta `ListaCheiaException`.

#### `inserir_apos_atual(valor: any) -> None`
Insere `"valor"` como sucessor do elemento apontado pelo cursor.

Se a lista estiver cheia, levanta `ListaCheiaException`.

#### `inserir_como_ultimo(valor: any) -> None`
Insere `"valor"` no final da lista.

Se a lista estiver cheia, levanta `ListaCheiaException`.

#### `inserir_como_primeiro(valor: any) -> None`
Insere `"valor"` no inicio da lista.

Se a lista estiver cheia, levanta `ListaCheiaException`.

#### `inserir_posicao(i: int, valor: any) -> None`
Insere `"valor"` na posição apontada pelo índice `"i"`.

Caso o  indice `"i"` esteja fora dos limites da lista, será levantada uma `IndiceInexistenteException`.

#### `excluir_atual() -> None`
Exclui o elemento apontado pelo cursor atualmente.

Se a lista estiver vazia, levanta `ListaVaziaException`.

#### `excluir_primeiro() -> None`
Exclui o primeiro elemento da lista.

Se a lista estiver vazia, levanta `ListaVaziaException`.

#### `excluir_ultimo() -> None`
Exclui o último elemento da lista.

Se a lista estiver vazia, levanta `ListaVaziaException`.

#### `excluir_posicao(i: int) -> None`
Exclui o elemento no índice `"i"`.

Se a lista estiver vazia, levanta `ListaVaziaException`.

Caso o  indice `"i"` esteja fora dos limites da lista, será levantada uma `IndiceInexistenteException`.

#### `excluir_elemento(valor: any) -> None`
Exclui todos os elementos da lista cujo valor seja igual a `"valor"`.

Caso o elemento não esteja presente, nada acontece.

### Consultas

#### `vazia() -> bool`
Retorna `True` caso a lista esteja vazia, caso contrário, `False`.

#### `cheia() -> bool`
Retorna `True` caso o número de elementos na lista seja igual ao valor máximo permitido, caso contrário, `False`.

#### `comprimento() -> int`
Retorna um número inteiro que representa a quantidade de elementos armazenados na lista.

#### `busca(valor: any) -> bool`
Retorna True caso a lista contenha um elemento igual a `"valor"`, caso contrário, `False`.

#### `primeiro() -> any`
Retorna o valor do primeiro elemento.

#### `ultimo() -> any`
Retorna o valor do ultimo elemento.

#### `posicao_de(valor: any) -> int | None`
Retorna o índice do elemento igual a `"valor"`. Caso `"valor"` não esteja na lista, retorna `None`.

## Demonstração

Para ver uma demonstração do funcionamento da `ListaGloriosa` em toda sua glória, rode o arquivo `main.py` com um interpretador de Python 3.8 ou versões superiores.

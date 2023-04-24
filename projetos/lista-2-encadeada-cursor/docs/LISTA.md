# Trabalho 1 - INE5609 - Estruturas de Dados

<strong>Alunos</strong>: Francisco Camerini (22100898), Luiz Felipe Scheidt (22100914).

## Implementação

Lista duplamente encadeada com cursor desenvolvida em Python.

Para cada valor inserido na `ListaGloriosa` existe um objeto `ElementoLista` correspondente, este objeto possui os atributos, `valor`, `proximo` e `anterior` (ponteiros para outros objetos `ElementoLista`).

O <b>cursor</b> da  `ListaGloriosa` foi implementado como um atributo privado `"__cursor"`, este, é apenas um ponteiro para um `ElementoLista` específico. O valor deste atributo é manipulado pelos [métodos privados do cursor](#sobrecursor).

Para facilitar o controle da quantidade de elementos e o acesso a elementos específicos a classe possui os seguinte atributos privados:

Atributo        | Tipo            |Significado
----------------|-----------------|---------------------
`__max`         |  `int`          |Quantidade máxima permitida de elementos
`__n_elementos` |  `int`          |Quantidade atual de elementos
`__primeiro`    | `ElementoLista` |Ponteiro para o primeiro `ElementoLista`
`__ultimo`      | `ElementoLista` |Ponteiro para o ultimo `ElementoLista`
`__cursor`      | `ElementoLista` |Ponteiro para o `ElementoLista` atual (cursor)

Ao se instanciar um objeto `ListaGloriosa`, os atributos, `__primeiro`, `__ultimo` e `__cursor`, são todos iniciados apontando para um mesmo objeto `ElementoLista` "fake" de valor `None`, a fim de facilitar as operações de inserção de valores na lista.

## Documentação dos Métodos

A classe <strong>ListaGloriosa</strong>, encontrada dentro do arquivo <b>lista.py</b> dispõe dos seguintes métodos para armazenamento e consulta de dados.

### Construtor
O construtor da classe recebe um parametro `"max"`, que deve ser um número inteiro. Este valor será o número máximo de elementos que a <b>ListaGloriosa</b> armazenará.
```python
minha_lista = ListaGloriosa(max=99) # instancia uma lista que armazenará no máximo 99 elementos.
```


### <a name="sobrecursor"> Sobre o cursor (privados)

#### `__avanca_cursor(pos: int = 1, erro_se_inexistente: bool = False) -> None`
Avança o cursor da lista o número de posições indicados em `"pos"`.

Este método recebe um parâmetro booleano `"erro_se_inexistente"`, se `True`, o método levantará uma excessão `IndiceInexistenteException` caso a posição desejada esteja fora dos limites da lista. Caso contrário, o cursor irá até onde for possível, sem levantar erros. Por padrão o valor deste parametro é `False`.

#### `__retrocede_cursor(pos: int = 1, erro_se_inexistente: bool = False) -> None`
Retrocede o cursor da lista o número de posições indicados em `"pos"`.

Este método recebe um parâmetro booleano `"erro_se_inexistente"`, se `True`, o método levantará uma excessão `IndiceInexistenteException` caso a posição desejada esteja fora dos limites da lista. Caso contrário, o cursor irá até onde for possível, sem levantar erros. Por padrão o valor deste parametro é `False`.

#### `__move_cursor_posicao(i: int) -> None`
Move o cursor da lista para o índice indicado em `"i"`. (Lembrando que o primeiro índice da lista é 0)

Este método suporta indexação negativa, `-1` representa o último índice da lista, `-2` o penúltimo, e assim por diante.

Se `"i"` estiver fora dos limites da lista, levanta `IndiceInexistenteException`.

Algo interessante sobre a implementação deste método é que o deslocamento do cursor varia de acordo com o índice desejado, como sempre saberemos o número de elementos que a lista possui (`__n_elementos`), saberemos também, qual índice representa o meio da lista, dessa forma podemos calcular se é mais vantajoso começar o deslocamento do cursor pelo início ou fim da lista. Assim, no pior caso, o deslocamento para o índice desejado ocorrerá em aproximadamente `n/2` operações.

#### `__move_cursor_inicio() -> None`
Move o cursor para o primeiro elemento da lista.

#### `__move_cursor_final() -> None`
Move o cursor para o último elemento da lista.

#### `__proximo_do_cursor() -> ElementoLista | None`
Retorna o `ElementoLista` localizado após o cursor ou `None` se inexistente.

#### `__anterior_ao_cursor() -> ElementoLista | None`
Retorna o `ElementoLista` localizado antes do cursor ou `None` se inexistente.

### Sobre a Estrutura

#### `acessa_atual() -> any`
Retorna o valor do elemento armazenado na posição apontada pelo cursor.

#### `acessa_posicao(i: int) -> any`
Retorna o valor do elemento armazenado no índice `"i"`. (Lembrando que o primeiro índice da lista é 0)

Utiliza os métodos, `__move_cursor_posicao` e `__acessa_atual`. Retornando o cursor a posição original ao final do método.

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

Para ver uma demonstração do funcionamento da `ListaGloriosa` em toda sua glória, rode o arquivo `main.py` com um interpretador Python de versão 3.8 ou superior.

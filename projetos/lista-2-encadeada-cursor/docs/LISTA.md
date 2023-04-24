# Trabalho 1 - INE5609 - Estruturas de Dados

<strong>Alunos</strong>: Francisco Camerini, Luiz Felipe Scheidt

Lista duplamente encadeada com cursor desenvolvida em Python

## Métodos

A classe <strong>ListaGloriosa</strong>, encontrada dentro do arquivo <b>lista.py</b> dispõe dos seguintes métodos para armazenamento e consulta de dados.

### Construtor
...

### Sobre o cursor

#### `avanca_cursor(pos: int = 1) -> None`
...

#### `retrocede_cursor(pos: int = 1) -> None`
...

#### `move_cursor_posicao(pos: int) -> None`
...

#### `move_cursor_inicio() -> None`
...

#### `move_cursor_final() -> None`
...

### Sobre a Estrutura

#### `comprimento() -> int`
...

#### `acessa_atual() -> any`
...

#### `acessa_posicao(pos: int) -> any`
...

#### `inserir_como_atual(valor: any) -> None`
...

#### `inserir_antes_atual(valor: any) -> None`
...

#### `inserir_apos_atual(valor: any) -> None`
...

#### `inserir_como_ultimo(valor: any) -> None`
...

#### `inserir_como_primeiro(valor: any) -> None`
...

#### `inserir_posicao(pos: int, valor: any) -> None`
...

#### `excluir_atual() -> None`
...

#### `excluir_primeiro() -> None`
...

#### `excluir_ultimo() -> None`
...

#### `excluir_posicao(pos: int) -> None`
...

#### `excluir_elemento(valor: any) -> None`
...

### Consultas

#### `vazia() -> bool`
...

#### `cheia() -> bool`
...

#### `busca(valor: any) -> bool`
...

#### `posicao_de(valor: any) -> int | None`
...

# Arvore de Decisão - INE5609
**Alunos**: Francisco Camerini, Luiz Felipe Scheidt

Programa que manipula uma árvore binária de decisão implementada em Python utilizando alocação dinâmica.

O objetivo do programa é tentar advinhar o animal que o usuário está pensando, e quando não advinhar, receber uma pergunta para aprender a diferença entre os dois animais, inserindo a pergunta e o novo animal na árvore.

## Implementação:

A classe `ArvoreDecisao` possui apenas um atributo chamado `raiz`, que aponta para um objeto da classe `No`, e um método, `insere_pergunta`.

A classe `No` possui os seguintes atributos:

Atributo  | Tipo| Significado
----------|----- |------
`tipo`    | `string` |Tipos possíveis: `animal` e `pergunta`
`conteudo`| `string` |Nome do animal ou uma pergunta
`esquerda`| `No` ou `None` |Ponteiro para seu filho da esquerda
`direita` |  `No` ou `None` |Ponteiro para seu filho da direita

Ao instanciar a árvore pela primeira vez, o programa define automaticamente a raiz da árvore como o animal Alce.

## Percorrimento e Inserção na árvore

Na árvore, as folhas serão sempre animais e as perguntas nunca serão folhas. Ao chegar em uma pergunta e colher a resposta do usuário, o programa avança para o filho da direita caso a resposta seja positiva, caso contrário, avança para o filho da esquerda.

A partir do momento que chegamos em uma folha da árvore, que será sempre um animal, o programa recebe dois inputs do usuário, o animal que ele pensou e uma pergunta que o diferencie do animal presente na folha da árvore.

Ao instanciar a árvore pela primeira vez, o programa define automaticamente a raiz da árvore como o animal Alce. Digamos que o usuário já jogou uma rodada e a árvore se encontra assim:

```

          (É Terrestre?)
          /           \
         /             \
      (Baleia)       (Alce) <-- Estamos aqui

```

Para o caso acima, o programa perguntará: você pensou em um Alce?

Se sim, o usuário tem a opcão de jogar novamente ou terminar o programa.

Caso contrário, o programa recebe o input do novo animal e da pergunta e chama o método da árvore `insere_pergunta`.

A pergunta deverá ser positiva para o animal atual (Alce), e negativa para o novo animal, de forma que o animal atual, será o filho da direita do nó da pergunta, e o novo animal, o filho da esquerda.

O programa pega o nó atual (do Alce), e seta ele mesmo como seu filho direito, e o novo animal como seu filho esquerdo, depois altera o tipo do nó original Alce para `pergunta` e seu conteúdo para a pergunta do usuário:

```

          (É Terrestre?)
          /           \
         /             \
      (Baleia)      (Tem chifres?)
                    /            \
                 (Coelho)       (Alce)

```

## Persistência

O programa utiliza a biblioteca `pickle` para persistir a árvore instanciada, de forma que ao final de toda execução sem nenhum erro, a árvore é salva em disco.
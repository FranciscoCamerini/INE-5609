import os
import pickle
import logging
from pathlib import Path

from arvore_decisao import ArvoreDecisao, No

PATH_ARVORE = Path(os.path.join(Path(__file__).parent.resolve(), 'persistencia', 'arvore'))

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger('arvore-decisao')


def pega_resposta_valida():
    while True:
        try:
            n = int(input('Resposta (1 = Sim, 0 = Não): '))
            break
        except ValueError:
            pass

    return n


def roda_arvore(arvore: ArvoreDecisao):
    print('\nPense em um animal...')

    no_atual = arvore.raiz
    while no_atual:
        if no_atual.is_animal:
            print('Você pensou em um(a) %s?' % no_atual.conteudo)

            if pega_resposta_valida():
                print('\nEu sabia!!')
                break
            else:
                animal = input('Qual animal você pensou: ')
                pergunta = input(
                    'Escreva uma frase que possa ser respondida de forma positiva considerando um(a) %s e negativa para um(a) %s: \n'
                    % (no_atual.conteudo, animal)
                )
                arvore.insere_pergunta(no_atual, pergunta, animal)

                break
        elif no_atual.is_pergunta:
            print(no_atual.conteudo)
            no_atual = no_atual.direita if pega_resposta_valida() else no_atual.esquerda

    print('Você quer jogar novamente?')
    if pega_resposta_valida():
        roda_arvore(arvore)


if __name__ == '__main__':
    if PATH_ARVORE.exists():
        logger.info(' Carregando árvore de decisão do disco')
        with open(PATH_ARVORE, 'rb') as file:
            arvore = pickle.loads(file.read())
    else:
        PATH_ARVORE.touch(exist_ok=True)
        logger.info(' Criando nova árvore de decisão')
        arvore = ArvoreDecisao(raiz=No('Alce'))

    try:
        roda_arvore(arvore)
    except Exception as e:
        logger.error(' Erro inesperado rodando árvore: %s' % e)
    else:
        logger.info(' Salvando árvore no disco, até a próxima')
        with open(PATH_ARVORE, 'wb') as file:
            pickle.dump(arvore, file)

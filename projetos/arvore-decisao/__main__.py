import os
import pickle
import logging

from arvore_decisao import ArvoreDecisao, No

PATH_ARVORE = os.path.join(os.getcwd(), 'arvore-decisao', 'persistencia', 'arvore')

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
                pergunta = input('Escreva uma frase que possa ser respondida de forma positiva considerando um(a) %s e negativa para um(a) %s: \n' % (no_atual.conteudo, animal))
                arvore.insere_pergunta(no_atual, pergunta, animal)

                break
        elif no_atual.is_pergunta:
            print(no_atual.conteudo)
            resposta = pega_resposta_valida()
            no_atual = no_atual.direita if resposta else no_atual.esquerda

    print('Você quer jogar novamente?')
    if pega_resposta_valida():
        roda_arvore(arvore)


if __name__ == '__main__':
    if os.access(PATH_ARVORE, os.R_OK):
        logger.info(' Carregando árvore de decisão do disco')
        with open(PATH_ARVORE, 'rb') as file:
            arvore = pickle.loads(file.read())
    else:
        logger.info(' Criando nova árvore de decisão')
        arvore = ArvoreDecisao(raiz=No('Alce'))

    try:
        roda_arvore(arvore)
    except (BaseException, Exception) as e:
        logger.error(' Erro inesperado rodando árvore: %s' % e)
    else:
        logger.info(' Salvando árvore no disco, até a próxima')
        with open(PATH_ARVORE, 'wb') as file:
            pickle.dump(arvore, file)

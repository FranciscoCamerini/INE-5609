class No:
    PERGUNTA = 'pergunta'
    ANIMAL = 'animal'

    def __init__(self, conteudo: str, tipo=None) -> None:
        self.conteudo = conteudo
        self.tipo = tipo or No.ANIMAL
        self.esquerda = None
        self.direita = None

    @property
    def is_animal(self) -> bool:
        return self.tipo == No.ANIMAL

    @property
    def is_pergunta(self) -> bool:
        return self.tipo == No.PERGUNTA


class ArvoreDecisao:
    def __init__(self, raiz=None) -> None:
        self.raiz = raiz

    def insere_pergunta(self, no_atual: No, pergunta: str, resposta_negativa: str) -> None:
        no_atual.direita = No(no_atual.conteudo)
        no_atual.conteudo = pergunta
        no_atual.tipo = No.PERGUNTA

        no_atual.esquerda = No(resposta_negativa)

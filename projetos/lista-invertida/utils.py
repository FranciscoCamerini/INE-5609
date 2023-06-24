def chave_nome(valor):
    return valor.strip().lower()[:2]


def chave_salario(valor):
    return int(valor // 1200)


def chave_cidade(valor):
    return valor.strip().lower()[:2]


def chave_cep(valor):
    return valor[:4]


def chave_coluna(coluna, valor):
    if coluna == "nome":
        return chave_nome(valor)
    elif coluna == "salario":
        return chave_salario(valor)
    elif coluna == "cidade":
        return chave_cidade(valor)
    elif coluna == "cep":
        return chave_cep(valor)
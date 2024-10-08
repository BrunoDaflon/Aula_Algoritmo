# lista = [10,11,12,13]
# lista.sort



def buscaBinária(lista, chave):
    pos_ini = 0
    pos_fim = len(lista) - 1
    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2
        if lista[pos_meio] == chave:
            return pos_meio
        if lista[pos_meio] > chave:
            pos_fim = pos_meio - 1
        if lista[pos_meio] < chave:
            pos_ini = pos_meio + 1
    return -1
def insertion_sort(lista):
    n = len(lista)
    for i in range(1,n):
        chave = lista[i]
        j = i -1
        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = chave

minha_lista = [3, 5, 6, 1, 8, 7, 2, 4]

insertion_sort(minha_lista)

print(minha_lista)
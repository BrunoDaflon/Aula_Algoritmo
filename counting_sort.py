def counting_sort(l):
    size = len(l)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        count[l[i]] += 1

    for j in range(1, 10):
        count[j] += count[j-1]

    a = size-1
    while a >= 0:
        output[count[l[a]-1]] = l[a]
        count[l[a] - 1] -= 1
        a -= 1

    for k in range(0, size):
        l[k] = output[k]

lista = [3, 5, 6, 1, 8, 7, 2, 4]

counting_sort(lista)
print(lista)
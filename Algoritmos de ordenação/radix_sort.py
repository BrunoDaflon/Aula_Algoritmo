def counting_sort(l, place):
    size = len(l)
    output = [0] * size
    count = [0] * 10

    for i in range(size):
        index = l[i] // place
        count[index % 10] += 1

    for j in range(1, 10):
        count[j] += count[j - 1]

    k = size - 1
    while k >= 0:
        index = l[k] // place
        output[count[index % 10] - 1] = l[k]
        count[index % 10] -= 1
        k -= 1

    for a in range(size):
        l[a] = output[a]

def radix_sort(l):
    m = max(l)
    place = 1
    while m // place > 0:
        counting_sort(l, place) 
        place *= 10

lista = [3, 5, 6, 1, 8, 7, 2, 4]

radix_sort(lista)

print(lista)
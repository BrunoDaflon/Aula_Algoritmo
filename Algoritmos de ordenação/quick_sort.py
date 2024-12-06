def quicksort(v, p, r):
    if p < r:
        q = particionar(v, p, r)
        quicksort(v, p, q-1)
        quicksort(v, q+1, r)

def particionar(v, p, r):
    x = v[p]
    i = p
    j = p + 1

    while j <= r:
        if v[j] < x:
            i += 1
            trocar(v, i, j)
        j += 1
    trocar(v, p, i)

    return i

def trocar(v, n, m): 
    temp = v[n]
    v[n] = v[m]
    v[m] = temp

vetor = [3, 5, 6, 1, 8, 7, 2, 4]

quicksort(vetor, 0, len(vetor)-1)

print(vetor)
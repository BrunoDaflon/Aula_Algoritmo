def mergesort(v, p, r):
    if p < r:
        q = (p+r) // 2
        mergesort(v, p, q)
        mergesort(v, q+1, r)
        intercalar(v, p, q, r)

def intercalar(v, p, q, r):
    temp = v.copy()
    i = p
    j = q + 1
    k = p

    while k <= r:
        if i > q:
            v[k] = temp[j]
            j += 1
        elif j > r:
            v[k] = temp[i]
            i += 1
        elif temp [i] <= temp[j]:
            v[k] = temp[i]
            i += 1
        else:
            v[k] = temp[j]
            j += 1

        k += 1

vetor = [3, 5, 6, 1, 8, 7, 2, 4]

mergesort(vetor, 0, len(vetor)-1)

print(vetor)
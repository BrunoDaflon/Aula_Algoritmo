def bucket_sort(l):
    bucket_count = 10
    bucket = [[] for _ in range(bucket_count)]

    for j in l:
        index = int(bucket_count * j)
        bucket[index].append(j)

    for k in range(bucket_count):
        bucket[k] = sorted(bucket[k])

    a = 0
    for b in range(bucket_count):
        for c in range(len(bucket[b])):
            l[a] = bucket[b][c]
            a += 1

    return l

lista = [0.3, 0.5, 0.6, 0.1, 0.8, 0.7, 0.2, 0.4]

res = bucket_sort(lista)

print(res)
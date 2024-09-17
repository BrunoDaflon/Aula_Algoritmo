#Crie uma lista com 1000 elementos
#Calcule a media da lista, utilizando apenas funções
'''def listas(lista):
    soma = 0
    lista = list(range(1,1000))
    for i in lista:
        soma += i
resultado = listas
print(resultado)'''


#lista = []
n = 10
#for i in range(n):
#    lista.append(i)
lista = list(range(1,1001))
for i in lista:
    print(i)
media = sum(lista)/len(lista)
print(media)

#somatorio
import math
'''n = 3
soma = 0
for i in range(1, n+1):
    soma += math.pow((i+1),2)
print(soma)'''

#Somatorio em def
def sigma(n):
    soma = 0
    for i in range(1,n+1):
        soma+= math.pow((i+1),2)
    return soma

resultado = sigma(3)
print(resultado)





#float
x = 10 / 3

#arredonda
y = math.ceil(x)

#casting
z = int(x)

print(x)
print(y)
print(z)


carro = [
    "Bmw", "Mercedez"
]
lista = [1,2,3]
lista = [1.0, 2.0]
lista = []
'''def logica(a,b):
    return a or b

a = bool(input("Insira um valor de a: "))
b = bool(input("Insira um valor de b: "))
resultado = logica(a,b)

print(resultado)

estudar no w3schools (recomendação)
'''
import math

#1 Crie uma função para calcular a area de um triangulo.
def area_triangulo(base, altura):
    return (base * altura)/2

triangulo = area_triangulo(5,4)
print(triangulo)

#2 Crie um programa para calcular a area de um quadrado.
def area_quadrado(lado):
    #return lado ** 2
    return math.pow(lado,2)

quadrado = area_quadrado(5)
print(quadrado)

#3 Crie um programa para calcular a area de um circulo

def area_circulo(raio):
    #return 3.14 * raio * raio
    #return 3.14 * (raio ** 2)
    #return math.pi * (raio ** 2)
    return math.pi * math.pow(raio,2)
 
circulo = area_circulo(10)
print(circulo)

#4 Crie um programa para calcular a area de um trapézio

def area_trapezio(base_menor, base_maior, altura):
    return ((base_menor+base_maior)*altura)/2

trapezio = area_trapezio(10,5,4)
print(trapezio)

# Depois refaça utilizando biblioteca
#import math



#5 --> x^2 - 4x + 4 = 0, encontre as raízes
def encontra_raizes(a,b,c):
    delta = math.pow(b,2) - 4*a*c
    if delta >= 0:
        raiz1 = (-b + math.sqrt(delta))/2*a
        raiz2 = (-b - math.sqrt(delta))/2*a
        return raiz1, raiz2
    else:
        return None

resultado = encontra_raizes(1,-4,4)
print(resultado)

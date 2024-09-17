#1
def calcular_potencia(base, expoente):
    if expoente == 0:
        return 1
    return base * calcular_potencia(base, expoente - 1)
resultado = calcular_potencia(2,3)
print(resultado)


#2
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Insira um número para calcular o Nésimo termo da sequência Fibonacci: "))
if n:
    print(f"O {n}-ésimo termo da sequência Fibonacci é {fibonacci(n)}")

#3
def contar_digitos(cd):
    if cd < 10:
        return 1
    return 1 + contar_digitos(cd // 10)
numero = 9
print(f"O número {numero} tem {contar_digitos(numero)} dígitos!!!")


    
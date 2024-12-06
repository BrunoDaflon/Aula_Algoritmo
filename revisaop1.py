#1

import random
lista = random.sample(range(1,101),10)
maior = max(lista)
menor = min(lista)
print(f"Na lista com os números: {lista}\no maior número é o: {maior}\ne o menor número é o: {menor}.")

#2 
lista_frutas = []
for i in range(5):
    fruta = input("Insira uma fruta: ")
    lista_frutas.append(fruta)
    print("Fruta adcionada com sucesso!")
print()
procurar_fruta = input("Insira uma fruta para procurar na lista: ")
if procurar_fruta in lista_frutas:
    print("Essa fruta está na lista.")
else:
    print("Essa fruta não está na lista.")

#3
def calcular_media_lista(numeros):
    soma = sum(numeros)
    media = soma / len(numeros)
    return media
numeros = [40,20,50,30,76,32,89,25,83,27]
resultado = calcular_media_lista(numeros)
print(resultado)

#4
listas = [
    ['Bruno', 30, 'Saquarema'],
    ['Lorena', 26, 'Saquarema'],
    ['Hygor', 27, 'Saquarema'],
    ['Leonardo', 36, 'Brasília'],
    ['Kevin', 26, 'Portsmouth']
]
for lista in listas:
    nome, idade, cidade = lista
    print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

#5
lista = []
for i in range(10):
    numero = int(input("Insira um número: "))
    if numero not in lista:
        lista.append(numero)
    else:
        print("Número removido, pois ja se encontra na lista!")
print(lista)


#6
horas_semana = {}
semana = ['Segunda', 'Terça', 'Quarta','Quinta','Sexta']
for dia in semana:
    horas = float(input(f"Quantas horas você trabalhou na {dia}: "))
    horas_semana[dia] = horas
total_de_horas = sum(horas_semana.values())
print(f"O total de horas na semana trabalhada foi de {total_de_horas}")

#7
alunos_notas = {
    'Joao': 9,
    'Pedro': 6,
    'Gabriela': 10,
    'Bruno': 8,
    'Lorena': 10,
    'Alice': 7,
    'Andre': 6.5,
    'Marlon': 7.9,
    'Mateus': 5,
}

def consultar_alunos_e_atualizar():
    aluno = input('Insira o nome do aluno: ')
    if aluno in alunos_notas:
        print(f"O aluno {aluno}, tem uma nota {alunos_notas[aluno]}")
        atualizar = input("Gostaria de atualizar a nota do aluno? (s/n) ")
        if atualizar == "s":
            nota = float(input("Insira a nova nota: "))
            alunos_notas[aluno] = nota
            print(f"Nota do {aluno} atualizada para {alunos_notas[aluno]}")
        else:
            print("Ok")
    else:
        print("Aluno não encontrado")
consultar_alunos_e_atualizar()


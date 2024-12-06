import os
try:
    os.chdir(r"D:\Faculdade\Segundo Periodo\3- Algoritimo\aula 9\parte 2\6")
    with open('texto.txt','w')as arquivo:
        arquivo.write("Esse é um texto de programação em python. com ele eu treino as tecnicas de algoritimo em python!")
    with open("texto.txt","r") as arquivo:
except:...
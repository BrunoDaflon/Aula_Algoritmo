import os
try:
    os.chdir(r"D:\Faculdade\Segundo Periodo\3- Algoritimo\aula 9\parte 2\2")
    frase = input("Insira uma frase: ")
    with open('frase_usuario.txt','w') as arquivo:
        arquivo.write(frase)
    with open('frase_usuario.txt','r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
    print(os.getcwd())

except FileNotFoundError:
    print("Arquivo não encontrado")
except PermissionError:
    print("Você não possui permissão")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Até mais!")
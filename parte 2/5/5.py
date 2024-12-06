import os
try:
    os.chdir(r"D:\Faculdade\Segundo Periodo\3- Algoritimo\aula 9\parte 2\5")
    frase = input("Insira a frase: ")
    with open("anotacoes.txt","a") as arquivo:
        arquivo.write(frase + '\n')
        print(frase)
    print("Frase adicionada com sucesso ao arquivo 'anotacoes.txt'")
        

except FileNotFoundError:
    print("Arquivo não encontrado")
except PermissionError:
    print("Você não possui permissão")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Até mais!")
import os
try:
    os.chdir(r"D:\Faculdade\Segundo Periodo\3- Algoritimo\aula 9\parte 2\4")
    with open("origem.txt", "w") as arquivo:
        arquivo.write("Vamos copiar essa frase!!!")
    with open("origem.txt","r")as arquivo:
        conteudo = arquivo.read()
    with open("copia.txt","w") as arquivo:
        arquivo.write(conteudo)
        print(conteudo)
        print("arquivo copiado para 'copia.txt'")

    print(os.getcwd())
        
except FileNotFoundError:
        print("Arquivo não encontrado")
except Exception as e:
     print(f"Erro: {e}")
finally:
     print("Fechando programa")
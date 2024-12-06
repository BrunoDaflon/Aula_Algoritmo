def ler_arquivo_txt(arquivo):
    import os
    try:
        os.chdir(r'D:\Faculdade\Segundo Periodo\3- Algoritimo\aula 9\parte 2\1')
        with open("mensagem.txt", "w") as arquivo:
            arquivo.write("Algumas mensagens de texto para o exercicio 1 da aula 9 de algoritimos...")

        with open('mensagem.txt', "r") as arquivo:
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

ler_arquivo_txt("mensagem.txt")
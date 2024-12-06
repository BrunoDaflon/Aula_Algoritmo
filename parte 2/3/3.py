def contar_linhas_e_palavras(arquivo):
    import os
    try:
        os.chdir(r"D:\Faculdade\Segundo Periodo\3- Algoritimo\aula 9\parte 2\3")
        with open("texto.txt",'w') as arquivo:
            arquivo.write("Aqui é a primeira linha, primeira frase\n")
            arquivo.write("Aqui é a segunda linha, segunda frase\n")
            arquivo.write("Aqui é a terceira linha, terceira frase\n")
            arquivo.write("Aqui é a quarta linha, quarta frase\n")
            arquivo.write("Aqui é a quinta linha, quinta frase\n")
        
        with open("texto.txt",'r') as arquivo:
            conteudo = arquivo.readlines()
            numero_linhas = len(conteudo)
            numero_palavras = sum(len(linha.split()) for linha in conteudo)
            print(f"Linhas: {numero_linhas}")
            print(f"Palavras: {numero_palavras}")
                                
        print(os.getcwd())

    except FileNotFoundError:
        print("Arquivo não encontrado")
    except PermissionError:
        print("Você não possui permissão")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Até mais!")

contar_linhas_e_palavras("texto.txt")
    
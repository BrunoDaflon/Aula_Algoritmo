import os
biblioteca = []

def adicionar_livro(titulo,autor,ano,paginas):
    livro = {
        "titulo":titulo,
        "autor": autor,
        "ano": ano,
        "paginas": paginas,
    }
    biblioteca.append(livro)


def listar_livros(biblioteca):
    if not biblioteca:
        print("Sem livros cadastrado na biblioteca!")
    else:
        print("Livros:\n")
        for livros in biblioteca:
            print(f'- Livro: {livros["titulo"]} - Autor: {livros["autor"]} - Ano: {livros["ano"]} - Páginas: {livros["paginas"]}.')
    

def ordenar_livros():
    if not biblioteca:
        print("Sem livros cadastrado na biblioteca!")
        return
  
    
    ano_ou_pag = input("Deseja ordenar por 'ano' ou 'paginas'? ").strip().lower()
    if ano_ou_pag in ["ano","paginas"]:
        print("Deseja ordenar de forma 'crescente' ou 'decrescente'?\n")
        ordem = input("Escolha entre 'crescente' ou 'decrescente'.\nDigite(crescente/decrescente): ")
        if ordem == "crescente":
            reverso = False
        elif ordem == "decrescente":
            reverso = True
        else:
            print("Ordem inválida! Escolha entre 'crescente' ou 'decrescente'")
            return
    else:
        print("Inválido! Escolha entre 'ano' ou 'paginas'.")
    
    biblioteca.sort(key=lambda livro: livro[ano_ou_pag], reverse=reverso)
    print(f"Livros ordenados por {ano_ou_pag} em ordem {'decrescente' if reverso else 'crescente'}.\n")

def salvar_livros():
    try:
        os.chdir(r'C:\Users\Bruno\Desktop\exercicio\Biblioteca')
        with open("biblioteca.txt","w") as arquivo:
            for livro in biblioteca:
                arquivo.write(f"{livro['titulo']},{livro['autor']},{livro['ano']},{livro['paginas']}\n")
        print("Salvo")
    except IOError as e:
        print(f"Erro:{e}")

def carregar_livros():
    if not os.path.exists("biblioteca.txt"):
        print("Arquivo não existe.")
        return
    try:
        with open("biblioteca.txt", "r") as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        print("Dados carregados.")

    except IOError as e:
        print("Erro ao carregar o arquivo:", e)
    except ValueError:
        print("Erro no formato dos dados. Verifique o conteúdo do arquivo.")


def menu():
    while True:
        print("\nBiblioteca Digital")
        print("1. Adicionar livro")
        print("2. Listar livros")
        print("3. Ordenar livros")
        print("4. Salvar dados em arquivo")
        print("5. Carregar dados do arquivo")
        print("6. Sair")

        escolha = input("\nEscolha uma opção: ")
        if escolha == "1":
            titulo = input("\nInsira o titulo do livro: ")
            autor = input("Insira o autor do livro: ")
            ano = int(input("Insira o ano do livro: "))
            paginas = int(input("insira qts páginas tem no livro: "))
            adicionar_livro(titulo,autor,ano,paginas)
        elif escolha == "2":
            listar_livros(biblioteca)
        elif escolha == "3":           
            ordenar_livros()
        elif escolha == "4":
            salvar_livros()
        elif escolha == "5":
            carregar_livros()
        elif escolha == "6":
            salvar = input("Deseja salvar os dados antes de sair? (S/N): ").strip().lower()
            if salvar == "s":
                salvar_livros()
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()
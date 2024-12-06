import os

produtos = []

def adicionar_produto():
    
    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    try:
        preco = float(input("Preço: "))
        if preco <= 0:
            raise ValueError("O preço deve ser um número positivo!")
        quantidade = int(input("Quantidade: "))
        if quantidade < 0:
            raise ValueError("A quantidade deve ser positiva!")
    except ValueError as e:
        print(f"Erro: {e}")
        return
    
    produto = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade}
    produtos.append(produto)
    print("Produto adicionado com sucesso!")

def alterar_quantidade():
    nome = input("Nome do produto: ")
    produto = next((p for p in produtos if p["nome"].lower() == nome.lower()), None)
    
    if produto:
        escolha = input("Escolha adicionar(+) ou subtrair(-) a quantidade? (+/-): ").strip().upper()
        
        if escolha not in ["+", "-"]:
            print("Opção inválida.\n Digite '+' para adicionar ou '-' para Subtrair.")
            return
        
        try:
            quantidade_alterada = int(input("Informe a quantidade: "))
            if quantidade_alterada < 0:
                print("A quantidade deve ser um número positivo.")
                return
            
            if escolha == "+":
                produto["quantidade"] += quantidade_alterada
                print(f"Quantidade atualizada!!! Nova quantidade: {produto['quantidade']}")
            elif escolha == "-":
                if produto["quantidade"] >= quantidade_alterada:
                    produto["quantidade"] -= quantidade_alterada
                    print(f"Quantidade atualizada!!! Nova quantidade: {produto['quantidade']}")
                else:
                    print("Erro: quantidade a diminuir é maior do que a quantidade em estoque.")
        
        except ValueError:
            print("Erro: a quantidade deve ser um número inteiro.")
    else:
        print("Produto não encontrado.")


def exibir_produtos():
    if not produtos:
        print("Estoque zerado!.")
    else:
        print("Produtos em estoque:")
        for produto in produtos:
            print(f"Nome: {produto['nome']}, Categoria: {produto['categoria']}, Preço: R${produto['preco']:.2f}, Quantidade: {produto['quantidade']}")


def ordenar_produtos():
    if not produtos:
        print("Estoque zerado!")
        return

    preco_ou_qtd = input("Deseja orderar por (preço/quantidade)? \nResponda: ").lower()
    ordem = input("Ordem (crescente/decrescente)? \nReponda: ").lower()

    if preco_ou_qtd not in ["preço", "quantidade"] or ordem not in ["crescente", "decrescente"]:
        print("Dados inseridos inválidos!\nResponda corretamente...")
        return

    escolha = "preco" if preco_ou_qtd == "preço" else "quantidade"
    produtos.sort(key=lambda p: p[escolha], reverse=(ordem == "decrescente"))
    print(f"Produtos ordenados por {preco_ou_qtd} em ordem {ordem}.")
    exibir_produtos()


def salvar_em_arquivo():
    try:
        os.chdir(r'C:\Users\Bruno\Desktop\exercicio\Estoque')
        with open("estoque_loja.txt","w") as arquivo:
            for produto in produtos:              
                arquivo.write(f"{produto['nome']},{produto['categoria']},{produto['preco']},{produto['quantidade']}\n")
        print("Dados salvos!")
    except IOError as e:
        print(f"Erro: {e}")

def carregar_do_arquivo():
    if not os.path.exists("estoque_loja.txt"):
        print("Arquivo de estoque não encontrado.")
        return
    try:
        with open("estoque_loja.txt", "r") as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        print("Dados carregados.")

    except IOError as e:
        print("Erro ao carregar o arquivo:", e)
    except ValueError:
        print("Erro no formato dos dados. Verifique o conteúdo do arquivo.")

def menu():
    while True:
        print("\nSistema de Gestão de Estoque")
        print("1 - Adicionar produto")
        print("2 - Alterar quantidade")
        print("3 - Listar produtos")
        print("4 - Ordenar produtos")
        print("5 - Salvar dados em arquivo")
        print("6 - Carregar dados do arquivo")
        print("7 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            alterar_quantidade()
        elif opcao == "3":
            exibir_produtos()
        elif opcao == "4":
            ordenar_produtos()
        elif opcao == "5":
            salvar_em_arquivo()
        elif opcao == "6":
            carregar_do_arquivo()
        elif opcao == "7":
            salvar = input("Deseja salvar o estoque antes de sair? (S/N): ").lower()
            if salvar == "s":
                salvar_em_arquivo()
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida, tente novamente.")
menu()
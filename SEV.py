"""
Aqui no inicio está sendo a cabeça do código onde tem as importações da biblioteca para manipulação de arquivos e textos. 
Definições para constantes específicas para onde os dados serão armazenados. Verificação e criação da pasta dados de produtos. 
Criação de na lista estoque e o dicionário de funcionários.

"""

import os
import re

PASTA_DADOS = "dados_produtos"
ARQUIVO_PRODUTOS = os.path.join(PASTA_DADOS, "produtos.txt")
ARQUIVO_FUNCIONARIOS = os.path.join(PASTA_DADOS, "funcionarios.txt")

if not os.path.exists(PASTA_DADOS):
    os.makedirs(PASTA_DADOS)

estoque = []
funcionarios = {}

"""
Antes de ter o acesso diretamente ao sistema de estoque e vendas é necessário um login inicial antes de tudo, para justamente o sistema determinar qual função cada funcionário terá a partir daquele acesso.

"""

def login_cadastro():
    while True:
        print("\n[1] Login\n[2] Cadastrar novo funcionário\n[3] Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cpf = input("CPF: ").strip()
            senha = input("Senha: ")
            if cpf in funcionarios and funcionarios[cpf]["senha"] == senha:
                print(f"Bem-vindo(a), {funcionarios[cpf]['nome']} {funcionarios[cpf]['sobrenome']}!")
                return funcionarios[cpf]["tipo"]
            else:
                print("CPF ou senha inválidos.")
        elif opcao == "2":
            while True:
                cpf = input("CPF (somente números): ").strip()
                if not cpf.isdigit() or len(cpf) != 11:
                    print("Erro: O CPF deve conter exatamente 11 números.")
                elif cpf in funcionarios:
                    print("Erro: CPF já cadastrado.")
                else:
                    break 
            nome = input("Primeiro Nome: ").strip()
            sobrenome = input("Sobrenome: ").strip()
            while True:
                email = input("Email: ").strip()
                if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    print("Erro: Email inválido.")
                else:
                    break
            celular = input("Celular (somente números): ").strip()
            while True:
                senha = input("Senha (mínimo 8 caracteres, 1 letra maiúscula e 1 caractere especial): ")
                if len(senha) < 8:
                    print("Erro: A senha deve ter no mínimo 8 caracteres.")
                elif not any(c.isupper() for c in senha):
                    print("Erro: A senha deve conter pelo menos 1 letra maiúscula.")
                elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
                    print("Erro: A senha deve conter pelo menos 1 caractere especial.")
                else:
                    break
            tipo = input("Tipo (administrador/vendedor): ").strip().lower()
            if tipo in ["administrador", "vendedor"]:
                funcionarios[cpf] = {
                    "nome": nome,
                    "sobrenome": sobrenome,
                    "email": email,
                    "celular": celular,
                    "senha": senha,
                    "tipo": tipo
                }
                salvar_funcionarios()
                print("Funcionário cadastrado com sucesso!")
            else:
                print("Tipo inválido.")
        elif opcao == "3":
            exit()
        else:
            print("Opção inválida.")

"""
Aqui foi realizado uma função para salvar os dados dos funcionários e o administrador ter o maior controle deles.

"""

def salvar_funcionarios():
    with open(ARQUIVO_FUNCIONARIOS, "w") as f:
        for cpf, info in funcionarios.items():
            f.write(f"{cpf};{info['nome']};{info['sobrenome']};{info['email']};{info['celular']};{info['senha']};{info['tipo']}\n")

"""
    Aqui foi feito uma função para carregar os dados necessários do estoque,seus produtos e cadastro de funcionários. Foi feito dois breves dicionários com os dados necessários de cadastro dos produtos e cadastro de funcionários.

"""
def carregar_dados():
    global estoque, funcionarios
    estoque = []
    if os.path.exists(ARQUIVO_PRODUTOS):
        with open(ARQUIVO_PRODUTOS, "r") as f:
            for linha in f:
                dados = linha.strip().split(";")
                estoque.append({
                    "id": int(dados[0]),
                    "nome": dados[1],
                    "categoria": dados[2],
                    "preco": float(dados[3]),
                    "estoque": int(dados[4])
                })

    funcionarios = {}
    if os.path.exists(ARQUIVO_FUNCIONARIOS):
        with open(ARQUIVO_FUNCIONARIOS, "r") as f:
            for linha in f:
                dados = linha.strip().split(";")
                funcionarios[dados[0]] = {
                    "nome": dados[1],
                    "sobrenome": dados[2],
                    "email": dados[3],
                    "celular": dados[4],
                    "senha": dados[5],
                    "tipo": dados[6]
                }

"""
    Essa função salva os dados de produtos no arquivo especificado.Ela percorre a lista de estoque e escreve cada produto em uma nova linha no arquivo.
"""

def salvar_dados():
    with open(ARQUIVO_PRODUTOS, "w") as f:
        for produto in estoque:
            linha = f"{produto['id']};\n{produto['nome']};\n{produto['categoria']};\n{produto['preco']};\n{produto['estoque']}\n"
            f.write(linha)


"""
    Aqui é feita a função para cadastrar um novo produto.O produto é adicionado à lista de estoque e os dados são salvos no arquivo.
"""


def cadastrar_produto():
    try:
        global estoque
        nome = input("Nome do produto: ")
        categoria = input("Categoria: ")
        preco = float(input("Preço: "))
        estoque_inicial = int(input("Quantidade inicial em estoque: "))
        
        novo_produto = {
            "id": len(estoque) + 1,
            "nome": nome,
            "categoria": categoria,
            "preco": preco,
            "estoque": estoque_inicial
        }
        estoque.append(novo_produto)
        salvar_dados()
        print(f"O Produto '{nome}' foi cadastrado com sucesso!")
    except ValueError:
        print("Erro: Insira valores numéricos válidos para preço e estoque.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


"""
    Essa função exibe todos os produtos cadastrados.Ela percorre a lista de estoque e apresenta as informações de cada produto.
"""


def exibir_produtos():
    try:
        global estoque
        if not estoque:
            print("Nenhum produto foi cadastrado até então.")
        else:
            print("\nProdutos cadastrados:")
            for produto in estoque:
                print(f"ID: {produto['id']}\n | Nome: {produto['nome']}\n | Categoria: {produto['categoria']} | "
                      f"Preço: R$ {produto['preco']:.2f} | Estoque: {produto['estoque']}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


"""
    Essa função permite filtrar produtos pelo nome ou categoria.Ela retorna os produtos correspondentes aos critérios de busca.
"""


def filtrar_produtos():
    try:
        nome = input("Digite aqui o nome do produto (ou pressione Enter para ignorar): ")
        categoria = input("Digite aqui a categoria do produto em que deseja filtrar (ou pressione Enter para ignorar): ")
        resultados = [
            produto for produto in estoque
            if (nome and nome.lower() in produto["nome"].lower()) or
               (categoria and categoria.lower() in produto["categoria"].lower())
        ]
        if resultados:
            print("Produtos encontrados:")
            for produto in resultados:
                print(f"ID: {produto['id']}\n | Nome: {produto['nome']}\n | Categoria: {produto['categoria']}\n | Preço: R$ {produto['preco']:.2f}\n | Estoque: {produto['estoque']}")
        else:
            print("Nenhum produto encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

"""
    Essa função edita as informações de um produto. O usuário pode alterar nome, categoria e preço do produto.
"""

def editar_produto():
    try:
        produto_id = int(input("Digite o ID do produto que deseja editar: "))
        for produto in estoque:
            if produto["id"] == produto_id:
                nome = input("Escreva aqui um novo nome para o produto (ou pressione Enter para manter o atual): ")
                categoria = input("Escreva aqui uma nova categoria (ou pressione Enter para manter a atual): ")
                preco = input("Escreva aqui um novo preço (ou pressione Enter para manter o atual): ")
                
                if nome:
                    produto["nome"] = nome
                if categoria:
                    produto["categoria"] = categoria
                if preco:
                    produto["preco"] = float(preco)
                salvar_dados()
                print(f"Produto do ID: {produto_id} atualizado com sucesso!")
                return
        print(f"Produto ID {produto_id} não encontrado.")
    except ValueError:
        print("Erro: Insira um número válido para o ID ou preço.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


"""
    Essa função exclui um produto do estoque. Após a exclusão, os dados atualizados são salvos no arquivo.
"""


def excluir_produto():
    try:
        produto_id = int(input("ID do produto que deseja excluir: "))
        if any(produto["id"] == produto_id for produto in estoque):
            estoque[:] = [produto for produto in estoque if produto["id"] != produto_id]
            salvar_dados()
            print(f"Produto do ID: {produto_id} excluído com sucesso!")
        else:
            print(f"Produto do ID: {produto_id} não encontrado.")
    except ValueError:
        print("Erro: Insira um número válido para o ID.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


"""
    Essa função atualiza o estoque de um produto específico.É possível adicionar ou remover quantidades do estoque.
"""


def atualizar_estoque():
    try:
        global estoque
        produto_id = int(input("ID do produto que deseja atualizar o estoque: "))
        quantidade = int(input("Quantidade a ser adicionada (use número negativo para retirar): "))
        for produto in estoque:
            if produto["id"] == produto_id:
                produto["estoque"] += quantidade
                salvar_dados()
                print(f"Estoque do produto ID {produto_id} atualizado com sucesso!")
                return
        print(f"Produto ID {produto_id} não encontrado.")
    except ValueError:
        print("Erro: Insira números válidos para ID e quantidade.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


"""
    Essa função realiza a venda de um produto.Ela reduz o estoque e exibe os detalhes da venda, incluindo o método de pagamento.
"""


def venda_produto():
    try:
        produto_id = int(input("Digite o ID do produto que deseja vender: "))
        quantidade_vendida = int(input("Digite a quantidade a ser vendida: "))
        for produto in estoque:
            if produto["id"] == produto_id:
                if produto["estoque"] >= quantidade_vendida:
                    print("Selecione o método de pagamento:")
                    print("[1]Dinheiro")
                    print("[2]Pix")
                    print("[3]Débito")
                    print("[4]Crédito")
                    metodo_pagamento = input("Escolha uma para sua forma de pagamento: ")
                    if metodo_pagamento == "1":
                        metodo_pagamento = "Dinheiro"
                    elif metodo_pagamento == "2":
                        metodo_pagamento = "Pix"
                    elif metodo_pagamento == "3":
                        metodo_pagamento = "Débito"
                    elif metodo_pagamento == "4":
                        metodo_pagamento = "Crédito"
                    else:
                        print("Opção inválida. Venda cancelada.")
                        return
                    produto["estoque"] -= quantidade_vendida
                    salvar_dados()
                    print(f"\nVenda realizada com sucesso!")
                    print(f"Produto: {produto['nome']}")
                    print(f"Quantidade: {quantidade_vendida}")
                    print(f"Total: R$ {produto['preco'] * quantidade_vendida:.2f}")
                    print(f"Método de pagamento: {metodo_pagamento}")
                    return
                else:
                    print("Estoque insuficiente para realizar a venda.")
                    return
        print(f"Produto ID {produto_id} não encontrado.")
    except ValueError:
        print("Erro: Insira números válidos para ID e quantidade.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


def menu():
    tipo_acesso = login_cadastro()
    while True:
        print("Sistema de Estoque e Vendas")
        if tipo_acesso == "administrador":
            print("[1] Cadastrar produto")
            print("[2] Exibir produtos")
            print("[3] Filtrar produtos")
            print("[4] Editar produto")
            print("[5] Excluir produto")
            print("[6] Atualizar estoque")
            print("[7] Realizar venda")
            print("[8] Sair")
        elif tipo_acesso == "vendedor":
            print("[1] Exibir produtos")
            print("[2] Filtrar produtos")
            print("[3] Realizar venda")
            print("[4] Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
            if tipo_acesso == "administrador":
                if opcao == 1:
                    cadastrar_produto()
                elif opcao == 2:
                    exibir_produtos()
                elif opcao == 3:
                    filtrar_produtos()
                elif opcao == 4:
                    editar_produto()
                elif opcao == 5:
                    excluir_produto()
                elif opcao == 6:
                    atualizar_estoque()
                elif opcao == 7:
                    venda_produto()
                elif opcao == 8:
                    print("Saindo do sistema...")
                    break
                else:
                    print("Opção inválida.")
            elif tipo_acesso == "vendedor":
                if opcao == 1:
                    exibir_produtos()
                elif opcao == 2:
                    filtrar_produtos()
                elif opcao == 3:
                    venda_produto()
                elif opcao == 4:
                    print("Saindo do sistema...")
                    break
                else:
                    print("Opção inválida.")
        except ValueError:
            print("Erro: Insira um número válido para a opção.")
        except Exception as e:
            print(f"Erro inesperado: {e}")

carregar_dados()
menu()

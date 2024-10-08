projetos = []

def cadastrar_projeto(cliente, gerente, data, status):
    codigo = f"P{str(len(projetos)+1).zfill(3)}"
    novo_projeto = {
        "codigo" : codigo,
        "cliente" : cliente,
        "gerente" : gerente,
        "data" : data,
        "status" : status,
    }
    projetos.append(novo_projeto)
    print(f"Projeto {codigo} Adcionado")

def atualizar_status_projeto(codigo,novo_status):
    for projeto in projetos:
        if projeto["codigo"] == codigo:
            projeto["status"] = novo_status
            print(f"Status do código {codigo} atualizado para {novo_status}.")
            return
    print("Projeto não localizado!")

def buscar_projeto(codigo):
    for projeto in projetos:
        if projeto["codigo"] == codigo:
            print(f'Código: {projeto["codigo"]} - Cliente: {projeto["cliente"]} - Gerente: {projeto["gerente"]} -  data do inicio {projeto["data"]} - Status: {projeto["status"]} ')
            return
    print("Projeto não localizado!")

def listar_projetos(projetos):
    if not projetos:
        print("Sem projetos cadastrados!")
    else:
        print("Projetos: ")
        for projeto in projetos:
            print(f'Código: {projeto["codigo"]} - Cliente: {projeto["cliente"]} - Gerente: {projeto["gerente"]} - data do inicio {projeto["data"]} - Status: {projeto["status"]} ')

def contar_projetos_por_gerente(gerente):
    contagem= sum(1 for projeto in projetos if projeto["gerente"] == gerente)
    print(f"O(a) gerente: {gerente} tem {contagem} projeto(s) cadastrados!")

def menu():
    while True:
        print("SISTEMA DE GERENCIAMENTO DE PROJETOS\n")
        print("1 - Cadastrar um projeto")
        print("2 - Atualizar o status de um projeto")
        print("3 - Buscar projeto pelo código")
        print("4 - Listar projetos cadastrados")
        print("5 - Contar projetos por gerente")
        print("6 - Sair do sistema\n")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cliente = input("\nInsira o nome do cliente: ")
            gerente = input("Insira o nome do gerente do projeto: ")
            data = input("Insira a data do início do projeto ex:(00/00/0000): ")
            status = input("Insira o status do projeto: (Planejamento, Em andamento, Concluído): ")
            cadastrar_projeto(cliente,gerente,data,status)

        elif opcao == "2":
            codigo = input("Insira o código do projeto: ").upper()
            novo_status = input("Insira o novo status do projeto: (Planejamento, Em andamento, Concluído): ")
            atualizar_status_projeto(codigo, novo_status)

        elif opcao == "3":
            codigo = input("Insira o código do projeto: ").upper()
            buscar_projeto(codigo)

        elif opcao == "4":
            listar_projetos(projetos)

        elif opcao == "5":
            gerente = input("Insira o nome do gerente do projeto: ")
            contar_projetos_por_gerente(gerente)

        elif opcao == "6":
            print("Saindo do sistema......")
            break
        else:
            print("Opção inválida!")

menu()
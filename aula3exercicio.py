clientes = []

def adcionar_cliente(nome, email, telefone, endereco):
    cliente = [nome, email, telefone, endereco]
    clientes.append(cliente)
    print(f"Cliente {nome}")


def exibir_clientes():
    for cliente in clientes:
        print(f"Nome: {cliente[0]}, Email: {cliente[1]}, telefone: {cliente[2]}, endereço: {cliente[3]}")

def remover_cliente(email):
    for cliente in clientes:
        if cliente[1] == email:
            clientes.remove(cliente)
            print(f"Cliente com email: {email} removido")
            return
    print(f"Cliente com o email {email} não encontrado")

def buscar_cliente(email):
    for cliente in clientes:
        if cliente[1] == email:
            print(f"Cliente encontrado: Nome: {cliente[0]}, E-mail: {cliente[1]}, Telefone: {cliente[2]}, Endereço: {cliente[3]}")
            return
    print("Cliente não localizado!")

def menu():
    while True:
        print("MENU")
        print("1 - Adicionar cliente")
        print("2 - Exibir clientes")
        print("3 - Remover cliente")
        print("4 - Buscar cliente")
        print("5 - Sair do sistema")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            endereco = input("Endereço: ")
            adcionar_cliente(nome, email, telefone, endereco)
        elif opcao == "2":
            exibir_clientes()
        elif opcao == "3":
            email = input("Digite o e-mail para o cliente ser removido: ")
            remover_cliente(email)
        elif opcao == "4":
            email = input("Digite o e-mail do cliente: ")
            buscar_cliente(email)
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida")

menu()
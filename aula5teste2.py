lista_tarefas = []

def adicionar_tarefa(lista_tarefas, descricao, status, prioridade):
    if lista_tarefas:
        novo_id = max(tarefa["id"] for tarefa in lista_tarefas) + 1
    else:
        novo_id = 1
    nova_tarefa = {
        "id": novo_id,
        "descricao": descricao,
        "status": status,
        "prioridade": prioridade
    }
    lista_tarefas.append(nova_tarefa)
    print(f"Tarefa {descricao} adicionada!")

def visualizar_tarefas(lista_tarefas):
    if not lista_tarefas:
        print("Sem tarefas cadastradas!")
    else:
        print("Tarefas: ")
        for tarefa in lista_tarefas:
            print(f'ID:{tarefa["id"]} - Descrição: {tarefa["descricao"]}, Status: {tarefa["status"]}, Prioridade: {tarefa["prioridade"]} ')

def filtrar_tarefas(lista_tarefas, status=None, prioridade=None):
    tarefas_filtradas = [tarefa for tarefa in lista_tarefas if (status is None or tarefa['status'] == status) and (prioridade is None or tarefa['prioridade'] == prioridade)]
    return tarefas_filtradas

def menu():
    while True:
        print("\nGerenciamento de Tarefas\n")
        print("1 - Adicionar nova tarefa")
        print("2 - Visualizar tarefas")
        print("3 - Filtrar tarefas por status e/ou prioridade")
        print("4 - Sair do programa")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            descricao = input("Insira a descrição da tarefa: ")
            status = input("Insira o status da tarefa(pendente, em andamento, concluida): ")
            prioridade = input("Insira a prioridade(alta, média, baixa): ")
            adicionar_tarefa(lista_tarefas, descricao, status, prioridade)

        elif opcao == "2":
            visualizar_tarefas(lista_tarefas)

        elif opcao == "3":
            status = input("Insira o status (pendente, em andamento, concluida) para filtrar (ou ENTER para ignorar): ")
            prioridade = input("Insira a prioridade (alta, média, baixa) para filtrar (ou ENTER para ignorar): ")

            status = status if status else None
            prioridade = prioridade if prioridade else None

            tarefas_filtradas = filtrar_tarefas(lista_tarefas, status=status, prioridade=prioridade)

            if tarefas_filtradas:
                print("\n--- Tarefas Filtradas ---")
                visualizar_tarefas(tarefas_filtradas)
            else:
                print("Nenhuma tarefa encontrada com esse filtro.")
        
        
        elif opcao == '4':
            print("Saindo do programa")
            break
        
        else:
            print("Opção inválida!")

        
menu()

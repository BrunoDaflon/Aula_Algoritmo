import os
alunos = []

def adicionar_aluno():
    nome = input("Insira o nome do Aluno: ")
    notas = []
    

    while True:
        try:
            num_notas= int(input("Insira a quantidade de notas (2/5): "))
            if num_notas < 2 or num_notas > 5:
                raise ValueError("Número inválido. Insira entre 2 e 5.")
            break
        except ValueError as e:
                print(f"Error: {e}")
            
    for i in range(num_notas):
        while True:
            try:
                nota = float(input(f"Nota {i+1}: "))
                if nota < 0 and nota > 10:
                    raise ValueError("A nota deve ser entre 0 e 10.")
                notas.append(nota)
                break
            except ValueError as e:
                print(f"Erro: {e}")
                
        
    media = sum(notas) / len(notas)
    aluno = {
        "nome":nome,
        "nota": nota,
        "media": media,
    }
    alunos.append(aluno)
    print(f"Aluno(a) {nome} adicionado(a)!")




def ordenar_alunos():
    alunos.sort(key=lambda x: x["media"], reverse=True)
    print("Alunos ordenados pela média.\n")




def salvar_em_arquivo():
    ordenar_alunos()
    try:
        os.chdir(r'C:\Users\Bruno\Desktop\Alunos')
        with open("alunos.txt","w") as arquivo:
            for aluno in alunos:
                arquivo.write(f"{aluno['nome']}, {aluno['media']:.2f}\n")
        print("Salvo!")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        print("Fechando programa")

def exibir_alunos():
    for aluno in alunos:
        print(f"{aluno['nome']} - Média: {aluno['media']:.2f}")

def menu():
    while True:
        print("\n- Sistema de gestão de notas de alunos -\n")
        print("\nEscolha o número da opção(1/4)\n")
        print("1 - Adicionar Aluno: ")
        print("2 - Exibir Alunos: ")
        print("3 - Salvar em arquivo: ")
        print("4 - SAIR: \n")
        
        opcao = input("Escolha uma opção: ")
        print()
        
        if opcao == "1":
            adicionar_aluno()
        elif opcao == "2":
            ordenar_alunos()
            exibir_alunos()
        elif opcao == "3":
            salvar_em_arquivo()
        elif opcao == "4":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()


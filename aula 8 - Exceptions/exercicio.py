#EXERCICIO 1
try:
    x = int(input("Insira o primeiro número: "))
    y = int(input(f"{x}, dividido por: "))
    resultado = x / y
    print(resultado)

except ZeroDivisionError:
    print("Deu errado, não pode ser dividido por 0")
except ValueError:
    print("Insira apenas números!")
except Exception as e:
    print(f"Escreva o except:{e}")

#EXERCICIO 2
cores = {
    "vermelho" : (255,0,0),
    "verde": (0,255,0),
    "azul": (0,0,255),
    "amarelo": (255,255,0),
    "branco": (255,255,255),
    "preto": (0,0,0)
}
try:
    cor = input("Cor: ").lower()
    print(f"A cor {cor} em RGB é:{cores[cor]}")

except ValueError:
    print("Cor não encontrada!")
except Exception as e:
    print(f"Cor:{e} não encontrada nesta biblioteca")


#EXERCICIO 3
try:
    num = int(input("Insira um número inteiro: "))
    if num > 10:
        print(f"Numero {num} é válido!")
except ValueError:
    print("Número inválido! Deve ser inserido um número inteiro.")
else:
    print("Programa foi executado com sucesso!")
finally:
    print("Programa encerrado.")

#EXERCICIO 4 (terminar)
# class InvalidPasswordError():
#     pass
# def verificar_senha(senha):
#     if len(senha) < 8 or not any(caractere.isdigit() for caractere in senha):
#         raise InvalidPasswordError("Senha deve ter pelo menos 8 characteres, sendo 1 numeral.")
#     return True

# try:
#     senha = input("Insira uma senha: ")
#     verificar_senha(senha)
# except InvalidPasswordError as e:
#     print("Erro: {e}")
# finally:
#     print("Programa finalizado.")

#EXERCICIO 5
try:
    saldo_conta = float(input("Insira o saldo da conta: R$"))
    valor_transf = float(input("Insira o valor da transferência: R$"))
    
    if valor_transf > saldo_conta:
        raise ValueError("Saldo insuficiente!")
    
    saldo_conta -= valor_transf
    print(f"Transferência realizada!\nSaldo: R${saldo_conta:.2f}")
except ValueError as e:
    print(f"Erro: {e}")
finally:
    print("Finalizando...")
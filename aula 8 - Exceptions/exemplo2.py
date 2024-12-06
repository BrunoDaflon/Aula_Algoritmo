#Divisão
try:
    num = int(input("Valor: "))   
    resultado = 100 / num
    print(resultado)

# except ZeroDivisionError:
#     print("Não pode dividir por zero, caramba")

except ValueError:
    print("Tipo errado, caramba!")
    
# except Exception as e:
#     print(f"Escreva o except:{e}")

finally:
    print("Programa finalizado!")
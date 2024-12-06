#aplicação onde o acesso é permitido por idade
def verificaIdade(idade):
    if idade < 18:
        raise ValueError("Idade não é suficiente!")
        # print("Acesso não autorizado ao sistema!")
    else:
        print('Acesso autorizado no sistema')
        #print("Acesso autorizado ao sistema!")

try:
    verificaIdade(20)
except ValueError as e:
    print(e)
finally:
    print("Acabou")
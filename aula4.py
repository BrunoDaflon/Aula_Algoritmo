#dicionario
cliente = {
    "nome" : "Bruno",
    "email" : "brunodaflon1@gmail.com",
    "telefone" : "22997858915",
    "endereço" : "Rua Francisco Antonio dos Santos, 11."
}

print(cliente)

print(cliente["nome"])
resultado = cliente.get("email")
print(resultado)

resultado1 = cliente.values()
print(resultado1)

cliente["endereço"] = "Rua Nova"
print(cliente)


cliente.update({"endereço":"rua NOVA NOVA"})
print(cliente)


cliente.pop("endereço")
print(cliente)

cliente.clear()
print(cliente)

cliente.keys()
print(cliente)

for i,j in cliente.items():
    print(i,j)
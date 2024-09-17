#List Comprehension
veiculos = ["carros", "bicicleta"]
# novo = []
# for x in veiculos:
#     if "i" in x:
#         novo.append(x)
# print(novo)
novo1 = []
novo1 = [x for x in veiculos if "i" in x]
print(novo1)
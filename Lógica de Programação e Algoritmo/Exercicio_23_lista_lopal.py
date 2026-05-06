matriz = []
soma = 0
for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input(f"Digite o valor: "))
        linha.append(valor)
    matriz.append(linha)
for i in range(2):
    for j in range(2):
        soma += matriz[i][j]

print(soma)

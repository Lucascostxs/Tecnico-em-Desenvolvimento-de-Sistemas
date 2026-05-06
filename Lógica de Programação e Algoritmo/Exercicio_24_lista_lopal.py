matriz = []

for i in range(3):
    linha = []
    for j in range(2):
        valor = int(input(f"Digite o valor: "))
        linha.append(valor)
    matriz.append(linha)

print("numeros maiores que 10:")
for i in range(3):
    for j in range(2):
        if matriz[i][j] > 10:
            print(matriz)
numeros = []

for i in range(4):
    valor = int(input(f"Digite o {i+1}º número: "))
    numeros.append(valor)

numeros.sort()

print(numeros)
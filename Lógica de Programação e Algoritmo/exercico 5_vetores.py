numeros = 0
vetor = []

for i in range(8):
    num = int(input("Digite o numero: "))
    vetor.append(num)

numeros = int(input("Digite um numero para achar: "))

for i in range(8):
    if(vetor[i] == numeros):
        print("encontrou")

        
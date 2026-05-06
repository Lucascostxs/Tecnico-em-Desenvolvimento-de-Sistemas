maior = -9999999999999999999999
for i in range(5):
    numero = float(input("Digite um número: "))
    if numero > maior:
        maior = numero
print("O maior número é:", maior)
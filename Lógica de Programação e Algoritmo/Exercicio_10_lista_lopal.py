numeros = []

for i in range(6):
    num = int(input(f"Digite um numero: "))
    numeros.append(num)

print("numeros pares :")
for num in numeros:
    if num % 2 == 0:
        print(num)
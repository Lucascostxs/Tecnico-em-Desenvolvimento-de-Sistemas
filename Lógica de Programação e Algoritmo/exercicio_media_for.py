numeros =[]

for i in range (4):
    numeros.append(float(input(f"Digite o {i+1}ª numero: ")))

media = sum(numeros)/len(numeros)

print("A média é ", media)
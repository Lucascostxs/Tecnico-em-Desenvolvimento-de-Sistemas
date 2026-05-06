maiores = 0

for i in range(6):
    idade = int(input("Digite a idade: "))  
    if idade >= 18:
        maiores += 1
print(maiores)
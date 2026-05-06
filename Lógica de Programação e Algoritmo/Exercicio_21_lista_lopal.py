soma = 0

for i in range(8):
    num = int(input("Digite um numero: "))
    if (num %2==0):
        soma = num+soma
    
print(soma)
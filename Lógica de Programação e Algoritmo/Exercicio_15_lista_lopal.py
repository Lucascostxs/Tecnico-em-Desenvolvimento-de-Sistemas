numeros =[]
soma = 0
media = 0

for i in range(8):
    num = int(input("numeros: "))
    soma = soma + num

media = soma /8
for numero in numeros:
    if(numeros > media):
        print(numero, ">",media)
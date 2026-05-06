soma = 0
qtd = 0
numero = 0
while numero != -1:
    numero = float(input("Digite um número: "))
    if numero != -1 :
        soma = soma +numero
        qtd += 1

    media = soma / qtd
print(media)
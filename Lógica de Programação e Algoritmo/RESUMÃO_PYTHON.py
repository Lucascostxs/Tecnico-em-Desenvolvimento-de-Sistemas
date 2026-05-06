Python

#Criando uma variavel numerica 

numero = 10

#Criando uma variavel textual 

nome = "Gabriel"

#Usuario inserir um texto

nome_completo = int("Digite seu nome: ")

#Usuario inserir um numero inteiro

idade = int(input("Digite sua idade: "))

#Usuario inserir um numero decimal 

salario = float(input("Digite seu salario: "))

#Estruturas condicionasi - IF, ELIF, ELSE

if(salario > 1500 and idade >18):
    print("Você pode tirar carta!")

if(salario <1500 or idade <18):
    print("Você não pode tirar carta!")

else:
    print("Você não pode tirar carta!")

#Estrutura condicionais exemplo 2

turno = input("Digite seu turno (M/V/N): ")

if(turno =="M"):
    print("Bom dia!")

elif(turno =="V"):
    print("boa tarde!")

elif(turno =="N"):
    print("Boa noite!")

else:
    print("Invalido")

#Estrutura de repetição

# 0 -> 10

for i in range (11): #Sempre coloque um a mais 
    print(i)

# 1 -> 15

for i in range (1,16): #vai do 1 até o 15
    print(i)

# 5 -> 65 (aumentando de 5 em 5)

for i in range(5,66,+5):
    print(i)

# 122 -> 0 (tirando 2 em 2)

for i in range (122, -1, -2):
    print(i)

# Usuario escolhe o inicio e fim
# inicio -> fim

inicio = int(input("inicio: "))
fim = int(input("fim: "))

for  i in range (inicio, fim+1):
    print(i)

#Vetores

nomes = []

#Sempre utilizar para preencher o vetor

for i in range(5):
    nomes.append(input("Digite um nome: "))

#Sempre utilizar para exibir o vetor

for nome in nomes:
    print(nome)

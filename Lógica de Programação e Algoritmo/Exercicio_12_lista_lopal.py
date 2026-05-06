nomes = []

for i in range(5):
    nome = input(f"Digite o nome: ")
    nomes.append(nome)
for nome in reversed(nomes):
    print(nome)
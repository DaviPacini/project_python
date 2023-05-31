import random
nomes = ["Pedro", "Luiza", "Lucas", "Davi", 'Mateus', 'Henrique', 'Julia', 'Maria', 'Janete']
sobrenome = ['Santos', 'Fernandes', 'Souza', 'Grochevski', 'Duarte', 'Pacini', 'Lins']
rg = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
dia = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
ano = []
for i in range(1980, 2024):
    ano.append(i)

print("\n\t"+"*"*40)
print("\t*"+"Nome:", random.choice(nomes), random.choice(sobrenome))
print("\t*"+f"RG: {random.choice(rg)}.{random.choice(rg)}{random.choice(rg)}{random.choice(rg)}.{random.choice(rg)}{random.choice(rg)}{random.choice(rg)} ")
print("\t*"+f"Nascimento: {random.choice(dia)}/{random.choice(mes)}/{random.choice(ano)} ")
print("\t"+"*"*40)


import random

uf = input("Informe a UF: \n")

nomes = ["Pedro", "Luiza", "Lucas", "Davi", 'Mateus', 'Henrique', 'Julia', 'Maria', 'Janete', 'Mariana', 'Leonardo']
sobrenome = ['Santos', 'Fernandes', 'Souza', 'Grochevski', 'Duarte', 'Lins']
last_name = ['Carvalho', 'Vergutz', 'Meireles', 'Pacini', 'Gusmão', 'Dias']
rg = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
dia = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
ano = []
cpf = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(1980, 2024):
    ano.append(i)
c9 = 0
#============= Gerador de CPF ============
c1 = random.choice(cpf)
c2 = random.choice(cpf)
c3 = random.choice(cpf)
c4 = random.choice(cpf)
c5 = random.choice(cpf)
c6 = random.choice(cpf)
c7 = random.choice(cpf)
c8 = random.choice(cpf)
if uf == ('DF', 'GO', 'MS', 'MT', 'TO'):
    c9 = 1


#===================geração do digito de verificação====================
d7 = random.choice(rg)
d6 = random.choice(rg)
d5 = random.choice(rg)
d4 = random.choice(rg)
d3 = random.choice(rg)
d2 = random.choice(rg)

verificador = (d7*9 + d6*8 + d5*7 + d4*6 + d3*5 + d2*4) % 11
ver = 11 - verificador
d1 = ver
#========================================================================

print("\n\t"+"*"*40)
print("\t*"+"Nome:", random.choice(nomes), random.choice(sobrenome), random.choice(last_name))
print("\t*"+f"RG: {d1}.{d2}{d3}{d4}.{d5}{d6}{d7} ")
print("\t*"+f"Nascimento: {random.choice(dia)}/{random.choice(mes)}/{random.choice(ano)} ")
print("\t*"+f"CPF: {c1}{c2}{c3}.{c4}{c5}{c6}.{c7}{c8}{c9}")
print("\t"+"*"*40)


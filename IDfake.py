import random

uf = str(input("Informe a UF (Use letras maiúsculas): \n"))

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

#============= Gerador de CPF ============
c1 = random.choice(cpf)
c2 = random.choice(cpf)
c3 = random.choice(cpf)
c4 = random.choice(cpf)
c5 = random.choice(cpf)
c6 = random.choice(cpf)
c7 = random.choice(cpf)
c8 = random.choice(cpf)
if uf in ['DF', 'GO', 'MS', 'MT', 'TO']:
    c9 = 1
elif uf in ['AC', 'AM', 'AP', 'PA', 'RO', 'RR']:
    c9 = 2
elif uf in ['CE', 'MA', 'PI']:
    c9 = 3
elif uf in ['AL', 'PB', 'PE', 'RN']:
    c9 = 4
elif uf in ['BA', 'SE']:
    c9 = 5
elif uf in ['MG']:
    c9 = 6
elif uf in ['ES', 'RJ']:
    c9 = 7
elif uf in ['SP']:
    c9 = 8
elif uf in ['PR', 'SC']:
    c9 = 9
else:
    c9 = 0

verificadorcpf = (c1*10 + c2*9 + c3*8 + c4*7 + c5*6 + c6*5 + c7*4 + c8*3 + c9*2) % 11
if verificadorcpf == 0 or verificadorcpf == 1:
    Cd1 = 0
else:
    Cd1 = 11 - verificadorcpf

verificadorcpf_2 = (c2*10 + c3*9 + c4*8 + c5*7 + c6*6 + c7*5 + c8*4 + c9*3 + Cd1*2) % 11

if verificadorcpf_2 == 0 or verificadorcpf_2 == 1:
    Cd2 = 0
else:
    Cd2 = 11 - verificadorcpf_2

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
print("\t*"+f"CPF: {c1}{c2}{c3}.{c4}{c5}{c6}.{c7}{c8}{c9}-{Cd1}{Cd2}")
print("\t"+"*"*40)


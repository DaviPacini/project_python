'''DAVI SANTOS PACINI'''

from time import sleep
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mERRO na criação do arquivo\033[m')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mERRO ao ler arquivo\033[m')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            dado[2] = dado[2].replace('\n', '')
            dado[3] = dado[3].replace('\n', '')
            print(f'{dado[0]:<10};{dado[1]:<10};{dado[2]:>5} reais;{dado[3]:>5} horas')
    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', cargo = 'desconhecido', salario = 0, horas = 0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mERRO ao abrir o arquivo!')
    else:
        try:
            a.write(f'{nome}; {cargo}; {salario}; {horas}\n')
        except:
            print('\033[31mERRO na hora de escrever dados!')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, insira um valor válido. \033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mERRO: o usuário cancelou a digitação\033[m')
            return 0
        else:
            return n

def linha(tam = 42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc

arq = 'folha_pag.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
salarios_liquido = []
salarios_bruto = []
descontos = []
while True:
    resposta = menu(['Ver Dados', 'Cadastrar Nova', 'Sair do Sistema'])
    if resposta == 1:
        #opção de listar o conteudo de um arquivo
        lerArquivo(arq)
        print(f'Descontos: {descontos}\n')
        print(f'Descontos totais: {sum(descontos)}')
        print(f'Total salario bruto: {sum(salarios_bruto)}')
        print(f'Total salario líquido: {sum(salarios_liquido)}')


    elif resposta == 2:
        #opção para cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        cargo = str(input('Cargo: '))
        salario = float(input('Salario: '))
        horas = leiaInt('Horas Trabalhadas: ')
        cadastrar(arq, nome, cargo, salario, horas)
        if salario <= 1500:
            salarios_bruto.append(salario)
            salarios_liquido.append(salario)
        elif salario > 1500 and salario <= 3000:
            desconto = salario * 0.15
            descontos.append(desconto)
            salarios_bruto.append(salario)
            salario_liquido = salario - desconto
            salarios_liquido.append(salario_liquido)
        elif salario > 3000 and salario <= 5000:
            desconto = salario * 0.20
            descontos.append(desconto)
            salarios_bruto.append(salario)
            salario_liquido = salario - desconto
            salarios_liquido.append(salario_liquido)
        elif salario > 5000:
            desconto = salario * 0.27
            descontos.append(desconto)
            salarios_bruto.append(salario)
            salario_liquido = salario - desconto
            salarios_liquido.append(salario_liquido)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO: informe uma opção válida!\033[m')
    sleep(3)
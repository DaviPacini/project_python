from ex115.arquivo import *
from ex115.interfaace import *
from time import sleep

arq = 'nomescadastro.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #opção de listar o conteudo de um arquivo
        lerArquivo(arq)

    elif resposta == 2:
        #opção para cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO: informe uma opção válida!\033[m')
    sleep(3)
class Cliente:
    def __init__(self, nome, sobrenome, idade, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cpf = cpf

    def __str__(self):
        return f"Nome: {self.nome} {self.sobrenome}\nIdade: {self.idade}\nCPF: {self.cpf}"


class Conta:
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def __str__(self):
        return f"Agência: {self.agencia}\nConta: {self.conta}\nSaldo: {self.saldo}"

    def saque(self, valor):
        self.saldo -= valor

    def deposito(self, valor):
        self.saldo += valor

    def movimentacao(self, valor, conta_destino):
        self.saque(valor)
        conta_destino.deposito(valor)

    def mostrar_saldo(self):
        return f"Saldo atual: {self.saldo}"


class HistoricoConta:
    def __init__(self):
        self.movimentacoes = []

    def adicionar_movimentacao(self, descricao, valor):
        self.movimentacoes.append((descricao, valor))

    def __str__(self):
        movimentacoes_str = '\n'.join(f"{descricao}: R${valor}" for descricao, valor in self.movimentacoes)
        return f"Histórico de Conta:\n{movimentacoes_str}"


cliente1 = Cliente("João", "Silva", 25, "123.456.789-00")
conta1 = Conta("1234", "56789-1", 5000)
historico1 = HistoricoConta()

print(cliente1)
print(conta1)

conta1.saque(500)
historico1.adicionar_movimentacao("Saque", 500)

conta1.deposito(10000)
historico1.adicionar_movimentacao("Depósito", 10000)

conta1.deposito(1000)
historico1.adicionar_movimentacao("Depósito", 1000)

conta2 = Conta("1234", "56789-2", 2000)
historico2 = HistoricoConta()

print(conta2)

conta1.movimentacao(2000, conta2)
historico1.adicionar_movimentacao(f"Movimentação para conta {conta2.conta}", 2000)
historico2.adicionar_movimentacao(f"Movimentação de conta {conta1.conta}", 2000)

print(historico1)
print(historico2)

print("\nSaldo final de conta1:", conta1.mostrar_saldo())
print("Saldo final de conta2:", conta2.mostrar_saldo())
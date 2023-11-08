from clientes import Cliente
from contas0 import Conta

joao=Cliente('Joao da Silva', '666-1234')
maria=Cliente('Maria da silva', '555-1234')
print(joao.__dict__)
print(maria.__dict__)

conta = Conta(joao, 123, 1000)
conta.resumo()
conta.saque(500)
conta.resumo()
conta.saque(50)
conta.deposito(200)
conta.resumo()

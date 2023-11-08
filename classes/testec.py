from clientes import Cliente
from contas import Conta

joao=Cliente("Joao da Silva", "666-1234")
maria=Cliente("Maria da silva", "555-1234")
print(joao.__dict__)
print(maria.__dict__)

conta1 = Conta([joao], 1, 1000)
conta2 = Conta([maria,joao], 2, 500)
conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(250)
conta1.extrato()
conta2.extrato()

print(conta1.clientes.nome)


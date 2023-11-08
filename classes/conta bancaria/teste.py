from conta import Cliente, Conta
from bancos import Banco

joao = Cliente('João Donato', '3241-2222')
maria = Cliente('Maria da Luz', '1111-11111')
jose = Cliente('José Lima', '4444-1234')

contaJM = Conta([joao,maria],1,1000)
contaJ = Conta([jose], 2,500)

tatu = Banco("Tatu")
tatu.abre_conta(contaJM)
tatu.abre_conta(contaJ)
tatu.lista_contas()

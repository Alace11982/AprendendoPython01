class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.operacoes = []
        #self.deposito(saldo)

    def resumo(self):
        print("CC Número: %s Saldo: %s" % (self.numero, self.saldo))
        num = 0
        for i in self.clientes:
            print(f"{num + 1}º Titular: {i.nome}  \tTelefone: {i.telefone}")
            num += 1
        print()

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
        else:
            print(f"Saldo insuficiente,\n\tImpossível de fazer a operação"
                  f"\nImpossivel debitar R${valor} de R${self.saldo}")

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPOSITO", valor])

    def extrato(self):
        print("Extrato CC Nº \t\t%s\n" % self.numero)
        for o in self.operacoes:
            print("%10s %10.2f" % (o[0], o[1]))
        print('\n   Saldo: %10.2f\n' % self.saldo)


'''class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        Conta.__init__(self, clientes, numero, saldo)

    # ou super().__init__(clientes, numero, saldo)

    def saque(self, valor):
        self.saldo -= valor
        self.operacoes.append(["SAQUE", valor])'''


if __name__ == "__main__":
    joao = Cliente('João da Silva', '777-1234')
    # maria = Cliente('Maria Silva', '555-1234')

    '''conjunta = [joao, maria]

    #conjunta = [Cliente("João da Silva", "777-1234"), Cliente("Maria Silva", "555-1233")]

    conta1 = Conta([joao], 1, 1000)
    conta2 = Conta(conjunta, 2, 500)


    conta3 = Conta([Cliente("João da Silva", "777-1234"), Cliente("José Silva", "555-1233")], 3, 500)
    #print(conta1.__dict__)
    print(conta1.clientes[0].nome)

    print(len(conta2.clientes))
    print(conta2.clientes[0].nome)
    print(conta2.clientes[1].nome)

    conta1.resumo()
    conta2.resumo()
    conta3.resumo()
    #print(conta3.__dict__)

    conta3.saque(500)

    conta3.saque(600)
    conta3.resumo()'''


    conta5 = Conta([joao], 1, 10)
    conta5.resumo()

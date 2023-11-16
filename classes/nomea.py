from functools import total_ordering
@total_ordering

class Nome:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        #return self.nome
        return "<Classe {3} em 0x{0:x} Nome: {1} Chave: {2}>".format(id(self), self.__nome, self.__chave, type(self).__name__)
        '''
    def __repr__(self):
        return "<Classe {3} em 0x{0:x} Nome: {1} Chave: {2}>".format(id(self), self.nome, self.chave, type(self).__name__)
    '''
    def __eq__(self, outro):
        print("__eq__ Chamado")
        return self.nome == outro.nome

    def __lt__(self, outro):
        print("__lt__ Chamado")
        return self.nome < outro.nome
    
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, valor):
        if valor == None or not valor.strip():
            raise ValueError("Nome não pode ser nulo nem em branco")
        self.__nome = valor
        self.__chave = Nome.CriaChave(valor)

    @staticmethod
    def CriaChave(nome):
        return nome.strip().lower()

    #Comentario Explicativo
    '''
Observe que no programa da listagem 10.15, utilizamos um outro decorador
@staticmethod antes da definição do método CriaChave. Veja também que o método
CriaChave não possui o parâmetro self. Esse decorador cria um método estático,
isto é, um método que pode ser chamado apenas com o nome da classe, não necessitando
de um objeto para ser chamado.

O primeiro decorador @total_ordering é definido no módulo functools, por isso
tivemos que importá-lo no início de nosso programa. Ele é responsável por implementar,
ou seja, gerar o código responsável pela implementação de todos os
métodos de comparação especiais, a partir de _ _eq_ _ e de _ _lt_ _. Dessa forma,
_ _neq_ _ será a negação de _ _eq_ _; _ _gt_ _, a negação de _ _lt_ _; _ _le_ _, a combinação
de _ _lt_ _ com _ _eq_ _; e _ _ge_ _, a combinação de _ _gt_ _ com _ _eq_ _,
implementado, assim, todos os operadores de comparação (==, !=, >, <, >=, <=).
    '''    
    
if __name__ == "__main__":
    '''
    mudar o nome do arquivo, por que foi criado um copia do arquivo nome.py, implementando novos recursos'''
    from nomea import *
    A=Nome("Nilo")
    print(A)
    # B=Nome(" ") levanta o erro
    # C=Nome(None)
    
    print(A == Nome('Nilo'))
    print(A != Nome('Nilo'))
    
    print(A < Nome('Nilo'))
    
    #A >= Nome... ou A <= Nome... dará erro por nao ter definido os metodos especiais
    A.nome = "Nilo Menezes"
    print(Nome.CriaChave("x"))
    A.CriaChave('x')
    print(A)
    
    


 




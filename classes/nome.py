class Nome:
    def __init__(self, nome):
        if nome == None or not nome.strip():
            raise ValueError("Nome não pode ser nulo nem em branco")
        self.nome = nome
        self.chave = nome.strip().lower()

    def __str__(self):
        return self.nome
    
    def __repr__(self):
        return "<Classe {3} em 0x{0:x} Nome: {1} Chave: {2}>".format(id(self), self.nome, self.chave, type(self).__name__)
    
    def __eq__(self, outro):
        print("__eq__ Chamado")
        return self.nome == outro.nome

    def __lt__(self, outro):
        print("__lt__ Chamado")
        return self.nome < outro.nome
    
if __name__ == "__main__":
    from nome import *
    A=Nome("Nilo")
    print(A)
    # B=Nome(" ") levanta o erro
    # C=Nome(None)
    message = A.__repr__
    print(message)

    A == Nome('Nilo')
    A != Nome('Nilo')
    A < Nome('Nilo')
    A > Nome('Nilo')

    #A >= Nome... ou A <= Nome... dará erro por nao ter definido os metodos especiais






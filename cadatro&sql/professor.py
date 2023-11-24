from pessoa import Pessoa
class Professor(Pessoa):
    def __init__(self, nome, ano_de_nascimento, cpf, endereco, telefone, disciplinas):
        super().__init__(nome, ano_de_nascimento, cpf, endereco, telefone)
        self._disciplinas = disciplinas
    

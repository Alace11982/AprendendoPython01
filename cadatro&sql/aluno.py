from pessoa import Pessoa
class Aluno(Pessoa):
    def __init__(self,nome, ano_de_nascimento, cpf, endereco, telefone, ra, curso, periodo):
        super().__init__(nome, ano_de_nascimento, cpf, endereco, telefone)
        self._ra = ra 
        self._curso = curso
        self._periodo = periodo
    
        
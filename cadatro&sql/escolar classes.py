class Pessoa:
    def __init__(self, nome, idade, endereco, sexo, email, telefone, foto):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.sexo = sexo
        self.email = email
        self.telefone = telefone
        self.foto = foto 

class Aluno(Pessoa):
    def __init__(self, nome, idade, endereco, matricula, curso):
        super().__init__(nome, idade, endereco)
        self.matricula = matricula
        self.curso = curso

class Funcionario(Pessoa):
    def __init__(self, nome, idade, endereco, sexo, email, telefone, foto, cargo, salario):
        super().__init__(nome, idade, endereco, sexo, email, telefone, foto)
        self.cargo = cargo
        self.salario = salario
    
class Professor(Funcionario):
    def __init__(self, nome, idade, endereco, sexo, email, telefone, foto, cargo, salario, titulacao, disciplina, especialidade, horario_trabalho):
        super().__init__(nome, idade, endereco, sexo, email, telefone, foto, cargo, salario)
        self.titulacao = titulacao
        self.especialidade = especialidade
        self.horario_trabalho = horario_trabalho 
        self.disciplina = disciplina

class Turma:
    def __init__(self, id, nome, ano, turno, matricula_professores):
        self.id = id
        self.nome = nome
        self.ano = ano
        self.turno = turno
        self.matricula_professores = matricula_professores

class Disciplina:
    def __init__(self, id, nome, carga_horaria, bimestre, conteudo_programatico):
        self.id = id 
        self.nome = nome
        self.bimestre = bimestre
        self.conteudo_programatico = conteudo_programatico
        self.carga_horaria = carga_horaria

class Nota:
    def __init__(self, id, matricula_aluno, id_disciplina, nota,bimestre):
        self.id = id
        self.matricula_aluno = matricula_aluno
        self.id_disciplina = id_disciplina
        self.nota = nota
        self.bimestre = bimestre

class Falta:
    def __init__(self, id, matricula_aluno, data, justificada):
        self.id = id
        self.matricula_aluno = matricula_aluno
        self.data = data
        self.justificada = justificada

class Boleto:
    def __init__(self, id, numero_boleto, valor, data_vencimento, data_pagamento, forma_pagamento, status):
        self.id = id
        self.numero_boleto = numero_boleto
        self.valor = valor
        self.data_vencimento = data_vencimento
        self.data_pagamento = data_pagamento
        self.forma_pagamento = forma_pagamento
        self.status = status



alace = Professor('Alace Pereira', 18, 'Rua Olinda, 150', 'M', 'alace@gmail.com', '9999-9999', 'a', 'professor', 'R$2400,00', 'doutor', 'Algoritmos e logica de Programação', 'NDA', 'Noturno')
print(alace.cargo)
print(alace.__dict__)
print(alace.nome)





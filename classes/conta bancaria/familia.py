class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade 

class Familia:
    def __init__(self, pais, filhos):
        self.pais = pais 
        self.filhos = filhos



if __name__ == "__main__":
    pais = Pessoa("João", 40)
    filhos = [Pessoa("Maria", 10), Pessoa("Joãoziho", 5)]

    familia = Familia(pais, filhos)
    print(familia.pais.nome)
    print(familia.filhos[0].nome)


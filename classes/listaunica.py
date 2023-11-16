class listaUnica:
    def __init__(self, elem_class):
        self.lista = []
        self.elem_class = elem_class

    def __len__(self):
        return len(self.lista)
    
    def __iter__(self):
        return iter(self.lista)
    
    def __getitem__(self, p):
        return self.lista[p]

    def indiceValido(self, i):
        return i>=0 and i <len(self.lista)
    
    def adiciona(self, elem):
        if self.pesquisa(elem) == -1:
            self.lista.append(elem)

    def remove(self, elem):
        self.lista.remove(elem)

    def pesquisa(self, elem):
        self.verifica_tipo(elem)
        try:
            return self.lista.index(elem)
        except ValueError:
            return -1
        
    def verifica_tipo(self, elem):
        if type(elem) != self.elem_class:
            raise TypeError("Tipo inválido")
        
    def ordena(self, chave= None):
        self.lista.sort(key=chave)

if __name__ == '__main__':
    from listaunica import *
    lu = listaUnica(int)
    lu.adiciona(5)
    lu.adiciona(3)
    # lu.adiciona(2.5) -> gerara erro

    for e in lu:
        print(e)
    print()
    lu.adiciona(5)
    print(len(lu))
    print()
    print(lu[0])
    print(lu[1])
    print()
    print(len(lu))


class Televisao():
    def __init__(self, canal):
        self.ligada = False
        self.canal = 2
        self.tamanho = ''
        self.marca = ''

    def muda_canal_para_baixo(self):
        self.canal -=1
    
    def muda_canal_para_cima(self):
        self.canal +=1



tv = Televisao(2)
print(tv.ligada)
print(tv.canal)

tv_sala=Televisao(6)
tv_sala.ligada=True
tv_sala.canal=4
tv_sala.tamanho=29
tv_sala.marca='Positivo'
tv_sala.muda_canal_para_baixo()
tv_sala.muda_canal_para_baixo()

print()
print(tv_sala.ligada,tv_sala.canal, tv_sala.tamanho, tv_sala.marca)
print(dir(tv_sala))

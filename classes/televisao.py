class Televisao():
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = ''
        self.marca = ''

tv = Televisao()
print(tv.ligada)
print(tv.canal)

tv_sala=Televisao()
tv_sala.ligada=True
tv_sala.canal=4
tv_sala.tamanho=29
tv_sala.marca='Positivo'

print()
print(tv_sala.ligada,tv_sala.canal, tv_sala.tamanho, tv_sala.marca)
print(dir(tv_sala))

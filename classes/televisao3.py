class Televisao():
    def __init__(self, min, max):
        self.ligada = False
        self.canal = 2
        self.tamanho = ''
        self.marca = ''
        self.cmin = min #Verificaçao de faixa de canais de tv, como valor maximo e minino da faixa
        self.cmax = max

    def muda_canal_para_baixo(self):
        if(self.canal-1>=self.cmin):
            self.canal -=1
            
    def muda_canal_para_cima(self):
        if(self.canal+1<=self.cmax):
            self.canal +=1

tv_quarto = Televisao(2, 10)
tv_quarto.canal = 6

print("Mudando o canal para cima") 
#não passando do valor, pois o mesmo foi setado no começo do codigo...
for x in range(0, 15):
    tv_quarto.muda_canal_para_cima()
    print(tv_quarto.canal, end=' ')

print("\nMudando o canal para baixo") 
#não passando do valor de 2...
for x in range(0, 15):
    tv_quarto.muda_canal_para_baixo()
    print(tv_quarto.canal, end=' ')



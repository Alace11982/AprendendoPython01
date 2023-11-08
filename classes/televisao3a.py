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
        else:
            self.canal =self.cmax
            
    def muda_canal_para_cima(self):
        if(self.canal+1<=self.cmax):
            self.canal +=1
        else:
            self.canal =self.cmin

tv_quarto = Televisao(2, 10)
tv_quarto.canal = 6

print("Mudando o canal para cima") 
#Diferente do código anterior, quando simulamos o apertar do controle remoto com laço for pra mudar de canal, 
#quando chegarmos no valor minimo da faixa de canais, se houver mais um iteração do laço for, voltaremos 
#ao canal máximo, fazer alternar somente entre a faixa de canais configurada no inicio do código

for x in range(0, 15):
    tv_quarto.muda_canal_para_cima()
    print(tv_quarto.canal, end=' ')

print("\nMudando o canal para baixo") 
for x in range(0, 15):
    tv_quarto.muda_canal_para_baixo()
    print(tv_quarto.canal, end=' ')



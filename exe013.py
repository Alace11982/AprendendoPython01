#Solicita ao usuário para digitar a força aplicada e a distância percorrida
forca = float(input("Digite a força aplicada (F): "))
distancia = float(input("Digite a distância percorrida (d): "))

#Calcula o trabalho usando a fórmula T = F * d
trabalho = forca * distancia 

#Exibe o resultado do trabalho 
#print("O trabalho realizado pela força é: ", trabalho )
#Exibe o resultado do trabalho com formatação
print("O trabalho realizado pela força é de {:.2f} joules.".format(trabalho ))


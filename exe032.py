altura = float(input("Digite sua altura em metros: "))
peso = float(input('Digite seu peso em quilogramas: '))

imc = peso / altura ** 2

if imc < 18.5:
    categoria = "abaixo do peso"
elif imc < 25:
    categoria = 'peso normal'
elif imc < 30:
    categoria = 'sobrepeso'
elif imc < 35:
    categoria = 'obesidade'
else:
    categoria = 'obesidade grave'

print(f"Seu IMC é: {imc:.2f}")
print(f"Categoria: {categoria}")


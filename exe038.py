numero =1 
while numero <= 100:
    if numero % 2 == 0:
        print(numero, end=" ")
    numero += 1
print('\n\n')

#Solução 2
numero =0 
while numero <= 100:
    print(numero, end=" ")
    numero += 2

print('\n\n')
#Soluçao 3
for numero in range(2, 101, 2):
    print(numero, end=" ")

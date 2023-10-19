#implemente um função recursiva para encontrar o máximo divisor comum(MDC) de dois números
def gcd(a, b):
    #Caso base:se o segundo número é zero,
    #o MDC é o primeiro número
    if b == 0:
        return a
    
    #Caso recursivo: calcular o MDC entre b 
    #e o resto da divisão de a por b
    return gcd(b, a% b)

#crie um função recursiva para inverter uma string
def reverse_string(s):
    #Caso base: se a string for vazia ou contiver apenas um caractere,
    #retorn a própria string 
    if len(s) <= 1:
        return s
    
    #caso recursivo:
    #retorne a última letra concatenada com a string invertida dos cararcteres restantes
    return s[-1] + reverse_string(s[:-1])

print(reverse_string('alace'))
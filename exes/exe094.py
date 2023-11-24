#Desenvolva uma função recursiva para calcular a soma dos digitos de um número inteiro
def sum_digits(number):
    #caso base: se o número tem apenas um dígito, a soma é o proprio número
    if number < 10:
        return number

    #caso recursivo: separar o último dígito 
    #e somar com a recursão do restante dos dígitos
    last_digit = number % 10
    remaining_digits = number // 10
    return last_digit + sum_digits(remaining_digits)

print(sum_digits(156))

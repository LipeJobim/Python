# Exercício 15


def soma(v1, v2):
    return v1 + v2


def subt(v1, v2):
    return v1 - v2


def mult(v1, v2):
    return v1 * v2


def divid(v1, v2):
    return v1 / v2


operacao = int(input("Qual é a operações? 1-Adição, 2-Subtração, 3-Divisão ou 4-Multiplicação : "))
valor1 = float(input("Qual é o valor 1?"))
valor2 = float(input("Qual é o valor 2?"))

if operacao == 1:
    resultado = soma(valor1, valor2)
elif operacao == 2:
    resultado = subt(valor1, valor2)
elif operacao == 3:
    resultado = divid(valor1, valor2)
elif operacao == 4:
    resultado = mult(valor1, valor2)

print("Resultado:", resultado)

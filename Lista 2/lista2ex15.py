# 15. Escreva um algoritmo para ler 2 valores e uma das seguintes operações a serem executadas (codificada da
# seguinte forma: 1.Adição, 2.Subtração, 3.Divisão, 4.Multiplicação). Calcular e Escreva o resultado dessa operação
# sobre os dois valores lidos.

operacao = int(input("Qual é a operações? 1-Adição, 2-Subtração, 3-Divisão ou 4-Multiplicação"))
valor1 = float(input("Qual é o valor 1?"))
valor2 = float(input("Qual é o valor 2?"))

if operacao == 1:
    print("Resultado:", valor1 + valor2)
elif operacao == 2:
    print("Resultado:", valor1 - valor2)
elif operacao == 3:
    print("Resultado:", valor1 / valor2)
elif operacao == 4:
    print("Resultado:", valor1 * valor2)

# 7. Escreva um algoritmo para ler 2 valores (considere que não serão lidos valores iguais) e escrevê-los
# em ordem crescente.

valor1 = int(input("Qual é o valor 1?"))
valor2 = int(input("Qual é o valor 2?"))
if valor1 > valor2:
    print(valor2, valor1)
else:
    print(valor1, valor2)

# 18. Escreva um algoritmo para ler 3 valores e escrevê-los em ordem crescente. Considere que o usuário não
# informará valores iguais.

valor1 = float(input("Qual é o valor 1?"))
valor2 = float(input("Qual é o valor 2?"))
valor3 = float(input("Qual é o valor 3?"))

if valor1 < valor2 < valor3:
    print("1", valor1, valor2, valor3)

elif valor1 < valor3 < valor2:
    print("2", valor1, valor3, valor2)

elif valor2 < valor1 < valor3:
    print("3", valor2, valor1, valor3)

elif valor2 < valor3 < valor1:
    print("4", valor2, valor3, valor1)

elif valor3 < valor1 < valor2:
    print("5", valor3, valor1, valor2)

elif valor3 < valor2 < valor1:
    print("6", valor3, valor2, valor1)

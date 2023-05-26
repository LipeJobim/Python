# 16. Escreva um algoritmo para ler 3 valores e escreva o maior deles. Considere que o usuário não informará
# valores iguais.

valor1 = float(input("Qual é o valor 1?"))
valor2 = float(input("Qual é o valor 2?"))
valor3 = float(input("Qual é o valor 3?"))

if valor2 < valor1 > valor3:
    print(valor1)
elif valor1 < valor2 > valor3:
    print(valor2)
else:
    print(valor3)

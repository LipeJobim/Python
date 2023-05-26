# Exercício 5

soma = 0
cont = 0
valor = 0

while valor >= 0:
    valor = int(input("Qual é o valor?"))
    if valor < 0:
        break
    soma += valor
    cont += 1

media = soma/cont
print("Média dos valores lidos: ", media)

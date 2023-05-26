# Exercício 8

soma = 0
cont = 0
valor = -1

while valor != 0:
    valor = int(input("Qual é o valor?"))
    if valor == 0:
        break
    if valor % 2 == 0:
        soma += valor
        cont += 1

media = soma / cont
print("Média dos valores pares lidos: ", media)
print(f"Média dos valores pares lidos: {media:.1f}")

# Exercicio 20

soma = 0
valor = -1

while valor != 0:
    valor = int(input("Valor?"))
    if valor == 0:
        break
    if valor < 0:
        soma += valor

print(f"Soma dos números negativos: {soma}")
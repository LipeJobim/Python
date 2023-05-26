# Exercício 26

# import random

maior = 0
menor = 99999
soma = 0

for cont in range(500):
    # valor = random.randint(0, 99999)
    valor = int(input("Valor?"))
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
    soma += valor

media = soma / 500

print(f"Maior valor informado: {maior}")
print(f"Menor valor informado: {menor}")
print(f"Média dos valores informados: {media}")

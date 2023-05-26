# Exercício 9

import random

maior = -99999999999999
menor = 99999999999999

for cont in range(50):
    num = random.randint(-999, 999)
    print(f"Qual é o valor? {num}")

    #num = int(input("Qual é o valor?"))
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f"O maior número lido é {maior}")
print(f"O menor número lido é {menor}")


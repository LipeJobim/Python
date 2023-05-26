# Exercício 28

soma = 0
cont2 = 0

for cont in range(13, 73+1):
    soma += cont
    cont2 += 1

media = soma / cont2

print(f"Média: {media:.2f}")

# Exercício 11

n = int(input("Quantos elementos?"))
a1 = int(input("Primeiro elemento?"))
r = int(input("Razão da progressão?"))

for cont in range(n):
    prog = a1 + cont * r
    print(f"{cont+1}: {prog}")

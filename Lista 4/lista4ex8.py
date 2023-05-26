# Exercício 8

from random import randint

matriz1 = []
for i in range(3):
    matriz1.append([])
    for j in range(3):
        # matriz1[i].append(randint(0, 40))
        num = int(input("Matriz 1 - Valor?"))
        matriz1[i].append(num)
print(f"Matriz 1: {matriz1}")

matriz2 = []
for i in range(3):
    matriz2.append([])
    for j in range(3):
        # matriz2[i].append(randint(0, 40))
        num = int(input("Matriz 2 - Valor?"))
        matriz2[i].append(num)
print(f"Matriz 2: {matriz2}")

produto = []
for i in range(3):
    produto.append([])
    for j in range(3):
        produto[i].append(matriz1[i][j] * matriz2[i][j])
print(f"Produtos da Matriz: {produto}")

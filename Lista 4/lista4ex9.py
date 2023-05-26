# Exercício 9

from random import randint

matriz = []
for i in range(5):
    matriz.append([])
    for j in range(10):
        # num = int(input("Matriz 1 - Valor?"))
        matriz[i].append(randint(0, 20))
        # matriz[i].append(num)
    matriz[i].sort()

print("Matriz:")
for i in range(5):
    print(f"{matriz[i]}")

elemento = []
contador = []

for i in range(5):
    for j in range(10):
        achou = False

        k = 0
        while k <= (len(elemento) - 1):
            if elemento[k] == matriz[i][j]:
                achou = True
            k += 1

        if achou:
            contador[elemento.index(matriz[i][j])] += 1
        else:
            elemento.append(matriz[i][j])
            contador.append(1)

i = 0
while i <= (len(elemento) - 1):
    print(f"O elemento {elemento[i]} apareceu {contador[i]} vezes;")
    i += 1

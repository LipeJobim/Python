# Exercício 9

from random import randint

elemento = []
contador = []
matriz = []


def incluir(num):
    elemento.append(num)
    contador.append(1)


def contar(num):
    contador[elemento.index(num)] += 1


def processar(num):
    achou = False
    k = 0
    while k <= (len(elemento) - 1):
        if elemento[k] == num:
            achou = True
        k += 1
    if achou:
        contar(matriz[i][j])
    else:
        incluir(matriz[i][j])


# Bloco Principal
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

for i in range(5):
    for j in range(10):
        processar(matriz[i][j])

i = 0
while i <= (len(elemento) - 1):
    print(f"O elemento {elemento[i]} apareceu {contador[i]} vezes;")
    i += 1

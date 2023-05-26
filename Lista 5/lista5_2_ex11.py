# Exercício 11


def progressao(primeiro, elemento, razao):
    return primeiro + elemento * razao


n = int(input("Quantos elementos?"))
a1 = int(input("Primeiro elemento?"))
r = int(input("Razão da progressão?"))

for cont in range(n):
    print(f"{cont+1}: {progressao(a1, cont, r)}")

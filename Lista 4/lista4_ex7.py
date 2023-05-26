# Exercício 7

from random import randint

vetor1 = []
for i in range(10):
    num = int(input("Vetor 1 - Número?"))  # randint(0, 40)
    vetor1.append(num)
vetor1.sort()
print(vetor1)

vetor2 = []
for i in range(10):
    num = int(input("Vetor 2 - Número?"))  # randint(0, 40)
    vetor2.append(num)
vetor2.sort()
print(vetor2)

uniao = []
for i in range(10):
    uniao.append(vetor1[i])
    uniao.append(vetor2[i])
uniao.sort()
print(f"União: {uniao}")
# ou
# uniao = vetor1 + vetor2

intersec = []
for i in range(10):
    for j in range(10):
        if vetor1[i] == vetor2[j]:
            intersec.append(vetor1[i])
intersec.sort()
print(f"Intersecção: {intersec}")

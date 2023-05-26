# Exercício 2

vetor = []
for i in range(10):
    num = int(input("Número?"))
    vetor.append(num)

print(vetor)

contpos = 0
contneg = 0
for i in range(10):
    if vetor[i] > 0:
        contpos += 1
    if vetor[i] < 0:
        contneg += 1

print(f"Positivos: {contpos}")
print(f"Negativos: {contneg}")

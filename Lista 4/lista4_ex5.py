# Exercício 5

vetor = []
for i in range(20):
    num = int(input("Número?"))
    vetor.append(num)
print(vetor)

tam = int(len(vetor) / 2) - 1
for i in range(tam):
    aux = vetor[i]
    vetor[i] = vetor[10 + tam - i]
    vetor[10 + tam - i] = aux
print(vetor)

# Exercício 10

vetor = []
num = 1


def houveTroca():
    if vetor[i] > vetor[i + 1]:
        aux = vetor[i + 1]
        vetor[i + 1] = vetor[i]
        vetor[i] = aux
        return True
    return False


while num > 0:
    num = int(input("Vetor 1 - Número?"))  # randint(0, 40)
    if num <= 0:
        break
    vetor.append(num)
print(f"Original: {vetor}")

trocou = True
while trocou:
    trocou = False;
    for i in range(len(vetor) - 1):
        trocou = houveTroca()
print(f"Ordenado: {vetor}")

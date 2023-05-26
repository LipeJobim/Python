# Exercício 3

vetor = []


def localizar(num):
    achou = False
    for i in range(10):
        if num == vetor[i]:
            return i
    return -1


# Bloco Principal
for i in range(10):
    num = int(input("Número?"))
    vetor.append(num)

procura = int(input("Localizar Número?"))
i = localizar(procura)
if achou >= 0:
    print(f"Achei o número na posição {i}.")
else:
    print("O número informado não foi localizado.")

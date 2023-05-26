# Exercício 4

vetor1 = []
vetor2 = []


def lerVetor(vetor, id):
    vetor = []
    for i in range(5):
        num = int(input(f"Vetor {id} - Número?"))
        vetor.append(num)
    return vetor


# Bloco Principal
vetor1 = lerVetor(vetor1, 1)
vetor2 = lerVetor(vetor2, 2)

vetor3 = []
for i in range(5):
    vetor3.append(vetor1[i] + vetor2[i])

print(f"Vetor 1:{vetor1}")
print(f"Vetor 2:{vetor2}")
print(f"Soma   :{vetor3}")

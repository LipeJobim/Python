# Exercício 6

vetor1 = []
for i in range(10):
    num = int(input("Vetor 1 - Número?"))
    vetor1.append(num)
print(vetor1)

vetor2 = []
for i in range(10):
    num = int(input("Vetor 2 - Número?"))
    vetor2.append(num)
print(vetor2)

produto = 0
for i in range(10):
    produto += vetor1[i] * vetor2[i]
print(f"Produto Escalar: {produto}")

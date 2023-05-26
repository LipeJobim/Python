#Exercício 4

vetor1 = []
for i in range(5):
    num = int(input("Vetor 1 - Número?"))
    vetor1.append(num)

vetor2 = []
for i in range(5):
    num = int(input("Vetor 2 - Número?"))
    vetor2.append(num)

vetor3 =[]
for i in range(5):
    vetor3.append(vetor1[i] + vetor2[i])

print(f"Vetor 1:{vetor1}")
print(f"Vetor 2:{vetor2}")
print(f"Soma   :{vetor3}")

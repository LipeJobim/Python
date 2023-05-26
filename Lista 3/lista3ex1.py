# Exercício 1
neg = 0
pos = 0

for cont in range(5):
    numero = int(input("Qual é o valor?"))
    if numero < 0:
        neg += 1
    else:
        pos += 1

print("Negativos", neg)
print("Positivos", pos)

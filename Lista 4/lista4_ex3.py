# Exercício 3

vetor = []
for i in range(10):
    num = int(input("Número?"))
    vetor.append(num)

achou = False;
procura = int(input("Localizar Número?"))
for i in range(10):
    if procura == vetor[i]:
        print(f"Achei o número na posição {i}.")
        Achou = True

if not achou:
    print("O número informado não foi localizado.")

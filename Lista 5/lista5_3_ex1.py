# Exercício 1
vetor = []


def ler():
    for i in range(5):
        num = int(input("Número?"))
        vetor.append(num)


def exibir():
    print(vetor)
    # ou
    for i in range(5):
        print(vetor[i])


# Bloco Principal
ler()
exibir()

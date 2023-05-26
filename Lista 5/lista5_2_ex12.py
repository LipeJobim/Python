# Exercício 12


def tabuada(num, tab):
    return num*tab


n = int(input("Tabuada?"))
for cont in range(n):
    print(f"{cont+1} x {n} = {tabuada(cont, n)}")
# Exercício 13

n = int(input("Fatorial de quantos números?"))
fat = 1
for elemento in range(n):
    numfat = int(input("Fatorial de?"))
    for cont in range(1, numfat+1):
        fat = 1
        for cont2 in range(1, cont+1):
            fat *= cont2
    print(f"Fatorial de {elemento} é {fat}")

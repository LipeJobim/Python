# Exercício 18

m = 0
contdiv = 0

while m >= 0:
    m = int(input("m?"))
    if m < 0:
        break
    if m%2 == 0:
        contdiv = 0
        for cont in range(1, m+1):
            print(f"Divisores de {cont}")
            for cont2 in range(1, cont+1):
                if cont%cont2 == 0:
                    contdiv += 1
                    print(f"{cont2} é divisor de {cont}")
        print(f"Divisores: {contdiv}")
    elif m%2 != 0 and m < 10:
        print()
    elif m%2 != 0 and m >= 10:
        print()



# Exercício 20


def quadrante(x, y):
    if (x > 0) and (y > 0):
        return 1
    elif (x < 0) and (y > 0):
        return 2
    elif (x < 0) and (y < 0):
        return 3
    elif (x > 0) and (y < 0):
        return 4
    else:
        return -1


vx = int(input("Coordenada X?"))
vy = int(input("Coordenada Y?"))
quad = quadrante(vx, vy)
if quad == -1:
    print("Não pertence a nenhum quadrante.")
else:
    print(f"Pertence ao {quad}º quadrante.")

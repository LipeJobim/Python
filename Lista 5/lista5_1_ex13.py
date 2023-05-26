# Exercício 13


def perimetro(medida):
    return medida * 4


def area(medida):
    return medida * medida


def perim_area(lados, medida):
    if lados == 4:
        return medida * medida
    elif lados == 3:
        return medida * 3
    else:
        return "Pentágono"


def perimetro_area(medida):
    return medida*3, medida*medida, "Pentágono"


lad = int(input("Lados?"))
med = int(input("Medida?"))

p, a, r = perimetro_area(med)
if lad == 3:
    print(p)
elif lad == 4:
    print(a)
else:
    print(r)

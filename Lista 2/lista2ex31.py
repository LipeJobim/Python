# 31. Escreva um algoritmo que leia o valor de 3 ângulos de um triângulo e escreva Se o triângulo é
# ACUTÂNGULO, RETÂNGULO ou OBTUSÂNGULO. OBS: Retângulo: um ângulo reto. Obtusângulo: um ângulo obtuso;
# Acutângulo: 3 ângulos agudos.

angulo1 = float(input("Ângulo 1?"))
angulo2 = float(input("Ângulo 2?"))
angulo3 = float(input("Ângulo 3?"))

if (angulo1 == 90) or (angulo2 == 90) or (angulo3 == 90):
    print("RETÂNGULO")
elif (angulo1 < 90) and (angulo2 < 90) and (angulo3 < 90):
    print("ACUTÂNGULO")
else:
    print("OBTUSÂNGULO")

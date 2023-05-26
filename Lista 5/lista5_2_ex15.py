# Exercício 15


def intervalo(num):
    if valor > 75:
        return 1
    elif valor > 50:
        return 2
    elif valor > 25:
        return 3
    else:
        return 4


def mostrarResultados():
    print(f"[0..25]: {cont1}")
    print(f"[26..50]: {cont2}")
    print(f"[51..75]: {cont3}")
    print(f"[76..100]: {cont4}")


valor = 0
cont1 = 0 # 0..25
cont2 = 0 # 26..50
cont3 = 0 # 51..75
cont4 = 0 # 76..100

while valor >= 0:
    valor = int(input("Qual é o valor?"))
    if valor < 0:
        break
    if intervalo(valor) == 1:
        cont4 += 1
    if intervalo(valor) == 2:
        cont3 += 1
    if intervalo(valor) == 3:
        cont2 += 1
    else:
        cont1 += 1

mostrarResultados()

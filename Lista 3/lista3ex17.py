# Exercício 17

valor = 0

while valor >= 0:
    m = int(input("m?"))
    if m < 0:
        break
    n = int(input("n?"))
    # valor = random.randint(-5, 1000)

    soma = 0
    print(soma)
    for cont in range(m, m+n+1):
        soma += cont
        print(f"+{cont} = {soma}")

    print(f"Soma dos {n} elementos seguidos de {m}: {soma}")

# Exercício 21

produto = 1
valor = -1

while valor != 0:
    valor = int(input("Valor?"))
    if valor < 0:
        break
    if valor > 0 and valor%2 == 0:
        produto *= valor

print(f"Produto dos números pares positivos: {produto}")

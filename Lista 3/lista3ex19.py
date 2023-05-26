# Exercício 19

valor = 1
contpar = 0
cont = 0
somapar = 0
soma = 0

while valor > 0:
    valor = int(input("Valor?"))
    if valor <= 0:
        break
    cont += 1
    soma += valor
    if valor%2 == 0:
        contpar += 1
        somapar += valor

mediapar = somapar / contpar
media = soma / cont
print(f"Qtde de valores pares: {contpar}    Média dos pares: {mediapar:.2f}")
print(f"Qtde de valores impares: {cont-contpar}")
print(f"Qtde de valores: {cont}  Média Geral: {media:.2f}")

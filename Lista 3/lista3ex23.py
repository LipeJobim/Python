# Exercício 23

# Exercício 21

idade = 0
cont1 = 0 # homens com olhos azuis maiores que 20 anos.
cont2 = 0 # mulheres entre 18 e 35 anos com olhos verdes e cabelos louros

while idade >= 0:
    idade = int(input("Idade?"))
    if idade < 0:
        break
    sexo = input("Sexo (M/F)?")
    olhos = input("Olhos (A/C/V)? ")
    cabelos = input("Cabelos (L/C/P/R)?")

    if sexo == "M" and olhos == "A" and idade > 20:
        cont1 += 1
    if sexo == "F" and olhos == "V" and cabelos == "L" and 18 < idade < 35:
        cont2 += 1

print(f"Homens com olhos azuis maiores que 20 anos: {cont1}")
print(f"Mulheres entre 18 e 35 anos com olhos verdes e cabelos louros: {cont2}")

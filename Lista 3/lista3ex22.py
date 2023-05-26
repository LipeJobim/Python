# Exercício 21

idade = 0
somasalario = 0
cont = 0
maioridade = -999
menoridade = 999
contSalarioF100 = 0

while idade >= 0:
    idade = int(input("Idade?"))
    if idade <= 0:
        break
    sexo = input("Sexo?")
    salario = float(input("Salário?"))

    cont += 1
    somasalario += salario
    if idade > maioridade:
        maioridade = idade
    if idade < menoridade:
        menoridade = idade
    if sexo == "F" and salario <= 100:
        contSalarioF100 += 1

mediasalario = somasalario / cont

print(f"Média de Salário do Grupo: {mediasalario:.2f}")
print(f"Maior idade: {maioridade}   Menor idade: {menoridade}")
print(f"Mulheres com salário até R$100,00: {contSalarioF100}")

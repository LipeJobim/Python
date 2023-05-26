# 9. Tendo como entrada a altura e o sexo (codificado da seguinte forma: 1 : feminino   2 : masculino) de uma pessoa,
# construa um algoritmo que calcule e imprima seu peso ideal, utilizando as seguintes fórmulas:
# (a) para homens: (72.7 * h) - 58
# (b) para mulheres: (62.1 * h) - 44.7

sexo = int(input("Sexo: informe 1 para Feminino ou 2 para Masculino?"))
altura = float(input("Qual é a altura?"))
if sexo == 1:
    pesoideal = (62.1 * altura) - 44.7
else:
    pesoideal = (72.7 * altura) - 58
print("Peso Ideal:", pesoideal)

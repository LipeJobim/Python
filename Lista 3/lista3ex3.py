# Exercício 3

salario = 0
somasalario = 0
somafilhos = 0
maiorsalario = 0
salarioAte100 = 0
habitantes = 0

while salario >= 0:
    salario = int(input("Informe Salário?"))
    if salario < 0:
        break

    somasalario += salario  # somasalario (0) = somasalario (0) + salario (1000)

    filhos = int(input("Informe Número de Filhos?"))
    somafilhos += filhos

    if maiorsalario < salario:
        maiorsalario = salario

    if salario <= 100:
        salarioAte100 += 1

    habitantes += 1

print("a) média salário:", somasalario / habitantes)
print("b) média filhos:", somafilhos / habitantes)
print("c) maior salário:", maiorsalario)
print("d) percentual salario até R$100:", salarioAte100 * 100 / habitantes)




numeroEmpregados = int(input("Quantos empregados há na loja?"))
salarioMinimo = float(input('Qual o valor do salário mínimo?'))
custoBicicleta = float(input('Qual o custo de uma bicicleta?'))
bicicletasVendidas = int(input("Quantas bicicletas foram vendidas?"))

salarioVendedor = 2 * salarioMinimo
precoVenda = custoBicicleta * (150/100)
comissaoVendedores = ((custoBicicleta * bicicletasVendidas) * (15/100)) / numeroEmpregados
totalVendas = precoVenda * bicicletasVendidas
salarioVendedor = salarioVendedor + comissaoVendedores;
totalDespesas = (custoBicicleta * bicicletasVendidas) + (salarioVendedor * numeroEmpregados)
lucro = totalVendas - totalDespesas

print("O salário de cada um dos", numeroEmpregados, "vendedores será de", salarioVendedor)
print("O lucro da loja será de", lucro)






precoLitro = 4.50
hodoInicial = int(input("Qual a quilometragem inicial?"))
hodoFinal = int(input("Qual a quilometragem inicial?"))
litrosGastos = float(input("Quantos litros foram gastos?"))
totalRecebido = float(input("Quantos R$ foi recebido pelas viagens?"))

km = hodoFinal - hodoInicial
kmL = km / litrosGastos

totalCombustivel = litrosGastos * precoLitro

lucro = totalRecebido - totalCombustivel

print("Média de Consuma (km/l):", kmL)
print("Lucro do Dia:", lucro)
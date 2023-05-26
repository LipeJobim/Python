
identificacao = input("Qual é a Identificação do Funcionário?")
salariofixo = float(input("Qual é o Salário Fixo?"))
comissaocarro = float(input("Qual é a Comissão por Carro?"))
carrosvendidos = int(input("Quantos carros foram vendidos?"))
totalvendas = float(input("Qual é o Total de Vendas?"))

comissaocarros = comissaocarro * carrosvendidos
comissaovendas = totalvendas * 0.05

salariototal = salariofixo + comissaocarros + comissaovendas
print("Identificação do Vendedor:", identificacao)
print("Comissão pelos carros vendidos:", comissaocarros, "reais")
print("Comissão sobre as vendas:", comissaovendas, "reais")
print("Salário a pagar:", salariototal, "reais")

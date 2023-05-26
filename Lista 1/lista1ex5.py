
salarioatual = float(input("Qual é o Salário Atual?"))
percprod = float(input("Qual é o Percentual de Produtividade?"))
numfunc = input("Qual é o Número do Funcionário??")
aumento = salarioatual * (8/100)
produtividade = salarioatual * (percprod/100)
novosalario = salarioatual + aumento + produtividade
print("Número do Funcionário:", numfunc)
print("Aumento:", aumento, "reais")
print("Produtividade:", produtividade, "reais")
print("Novo Salário:", novosalario, "reais")


# 28.	Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#  Combustível	Litros	        Desconto
#  Álcool	    Até 20	        3%
#               Mais de 20	    5%
#  Gasolina     Até 15	        3,5%
#               Mais de 15	    6%
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma:
# 1-álcool 2-Gasolina), calcule e imprima o valor a ser pago pelo cliente, sabendo-se que o preço da gasolina é
# de R$ 1,90 o litro e o álcool R$ 1,28.

alcool = 1.28
gasolina = 1.90

litros = float(input("Litros vendidos?"))
combustivel = int(input("Combustível? 1-Álcool ou 2-Gasolina "))

if combustivel == 1:
    if litros >= 20:
        desconto = 5 / 100
    else:
        desconto = 3 / 100
    valorpagar = litros * alcool
else:
    if litros >= 15:
        desconto = 6 / 100
    else:
        desconto = 3.5 / 100
    valorpagar = litros * gasolina

valorfinal = valorpagar - valorpagar * desconto
print("Valor Final ao Cliente:", valorfinal)

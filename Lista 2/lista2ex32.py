# 32. Um mercado está vendendo frutas com a seguinte tabela de preços:
#             Até 5 Kg	    Acima de 5 Kg
#   Morango:  R$ 5,00 p/Kg	Morango: R$ 4,00 p/Kg
#   Maçã:     R$ 3,00 p/Kg 	Maçã:R$ 2,00 p/Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 35,00, receberá ainda um
# desconto de 20% sobre esse total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
# (em Kg) de maçãs adquiridas e escreva o valor a ser pago pelo cliente.

macas = float(input("Maçãs?"))
morangos = float(input("Morangos?"))
if morangos > 5:
    precomorango = 4
else:
    precomorango = 5

if macas > 5:
    precomaca = 2
else:
    precomaca = 3

desconto = 0
totalapagar = precomorango * morangos + precomaca * macas
if ((morangos + macas) > 8) or (totalapagar > 35):
    desconto = totalapagar * (20 / 100)

totalfinal = totalapagar - desconto
print("Total a pagar", totalfinal)

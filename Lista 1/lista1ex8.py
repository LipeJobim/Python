valorhora = float(input("Qual é o valor hora?"))
horasnormais = float(input("Quantas horas normais?"))
horasextras = float(input("Quantas horas extras?"))
print("Valor a pagar:", horasnormais*valorhora+horasextras*(valorhora*1.5))




turmaC = 60
turmaD = 20
percReprovC = float(input("Qual % de Reprovados em C?"))
percAprovD = float(input("Qual % de Aprovados em C?"))

numeroReprovC = turmaC * percReprovC / 100
numeroReprovD = turmaD - (turmaD * percAprovD / 100)
totalReprovados = numeroReprovC + numeroReprovD
percReprovados = totalReprovados / (turmaC + turmaD) * 100

print("Reprovados da turma C:", numeroReprovC)
print("Reprovados da turma D:", numeroReprovD)
print("% de Reprovados:", percReprovados)




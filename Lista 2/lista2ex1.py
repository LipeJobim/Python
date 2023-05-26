# 1. Escreva um algoritmo para ler as notas das duas avaliações de um aluno no semestre, calcular e Escreva a média
# semestral e a seguinte mensagem: ‘PARABÉNS! Você foi aprovado’ somente Se o aluno foi aprovado (considere 8.0 a
# nota mínima para aprovação).

nota1 = float(input("Nota 1?"))
nota2 = float(input("Nota 2?"))
media = (nota1 + nota2) / 2
print(media)
if media >= 8:
    print("PARABÉNS! Você foi aprovado")5
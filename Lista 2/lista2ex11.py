# 11. Escreva um algoritmo para ler as notas da 1ª e 2ª avaliações de um aluno, calcular a média e Escreva Se este
# aluno foi APROVADO, REPROVADO ou Se está EM EXAME. Escreva também a média calculada. OBS: Para ter direito ao
# exame o aluno deve obter média mínima 5.5.

nota1 = float(input("Nota 1?"))
nota2 = float(input("Nota 2?"))
media = (nota1 + nota2) / 2
if media >= 8:
    print("APROVADO")
elif media > 5.5:
    print("EM EXAME")
else:
    print("REPROVADO")

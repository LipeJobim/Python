# Exercício 7

codigo = -1

while codigo != 0:
    codigo = int(input("Código do Aluno?"))
    if codigo == 0:
        break
    nota1 = float(input("Nota 1?"))
    nota2 = float(input("Nota 2?"))
    nota3 = float(input("Nota 3?"))
    media = (nota1 + nota2 + nota3) / 3
    print(f"Média do aluno {codigo}: {media:.1f}")

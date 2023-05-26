# Exercício 10

codigo = 0

while codigo >= 0:
    codigo = int(input("Código do Aluno?"))
    if codigo < 0:
        break

    nota1 = float(input("Nota 1?"))
    nota2 = float(input("Nota 2?"))
    nota3 = float(input("Nota 3?"))
    notas = [nota1, nota2, nota3]
    notas.sort()

    media = (notas[0]*3 + notas[1]*3 + notas[2]*4) / 10
    print(f"Média do aluno: {media:.2f}")
    if media >= 5:
        print("APROVADO")
    else:
        print("REPROVADO")


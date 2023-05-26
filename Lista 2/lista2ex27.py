# 27.	Escreva um algoritmo para ler as 4 notas obtidas por um aluno em 4 avaliações.
# Calcular a média usando a seguinte fórmula:
#    Média = (N1 + (N2 * 2) + (N3 * 3) + N4) / 7
# A seguir imprima o conceito do aluno baseado na seguinte tabela:
#   Média	                        Conceito
#   9,0 ou acima de 9,0	            A
#   entre 7,5 (inclusive) e 9,0	    B
#   entre 6,0 (inclusive) e 7,5     C
#   abaixo de 6,0	                D

n1 = float(input("Nota 1?"))
n2 = float(input("Nota 1?"))
n3 = float(input("Nota 1?"))
n4 = float(input("Nota 1?"))
media = (n1 + (n2 * 2) + (n3 * 3) + n4) / 7

if media >= 9.0:
    print("A")
elif media >= 7.5:
    print("B")
elif media >= 6.0:
    print("C")
else:
    print("D")

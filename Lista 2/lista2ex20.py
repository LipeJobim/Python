# 20. Escreva um algoritmo para ler as coordenadas (X,Y) de um ponto no sistema cartesiano e Escreva o quadrante ao
# qual o ponto pertence. Se o ponto estiver sobre os eixos, ou na origem, Escreva NÃO ESTÁ EM NENHUM QUADRANTE.
# Considere que o usuário poderá informar qualquer valor para as coordenadas.

x = int(input("Coordenada X?"))
y = int(input("Coordenada Y?"))

# 1º Quad (x,y)
# 2º Quad (-x,y)
# 3º Quad (-x,-y)
# 4º Quad (x, -y)

if (x > 0) and (y > 0):
    print("1º Quadrante")
elif (x < 0) and (y > 0):
    print("2º Quadrante")
elif (x < 0) and (y < 0):
    print("3º Quadrante")
elif (x > 0) and (y < 0):
    print("4º Quadrante")
else:
    print("Não está em nenhum quadrante")

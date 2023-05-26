# 13. Escreva um algoritmo para ler o número de lados de um polígono regular, e a medida do lado. Calcular e
# imprimir o seguinte:
# (a) Se o número de lados for igual a 3, Escreva: TRIÂNGULO e o valor do seu perímetro;
# (b) Se o número de lados for igual a 4 Escreva: QUADRADO e o valor da sua área;
# (c) Se o número de lados for igual a 5 Escreva: PENTÁGONO.

lados = int(input("Polígono de quantos lados?"))
if lados == 5:
    print("PENTÁGONO")
else:
    medida = float(input("Qual a medida do lado?"))
    if lados == 3:
        print("TRIÂNGULO:", medida * 3)
    else:
        print("QUADRADO:", medida * medida)


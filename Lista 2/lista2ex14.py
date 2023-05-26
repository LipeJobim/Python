# 14. Acrescente as seguintes mensagens à solução do exercício anterior conforme o caso.
# (a) Caso o número de lados seja inferior a 3 Escreva: NÃO E’ UM POLÍGONO.
# (b) Caso o número de lados seja superior a 5 Escreva: POLÍGONO NÃO IDENTIFICADO.

lados = int(input("Polígono de quantos lados?"))
if lados < 3:
    print("NÃO É POLÍGONO")
elif lados == 5:
    print("PENTÁGONO")
elif lados > 5:
    print("POLÍGONO NÃO IDENTIFICADO")
else:
    medida = float(input("Qual a medida do lado?"))
    if lados == 3:
        print("TRIÂNGULO:", medida * 3)
    elif lados == 4:
        print("QUADRADO:", medida * medida)

# Exercício 16
# import random


lista = []
valor = 0
linha = 0

while valor >= 0:
    valor = int(input("Qual o valor?"))
    # valor = random.randint(-5, 1000)
    if valor < 0:
        break
    lista.append(valor)

print("   #      Valor     Quadrado            Cubo          Raiz")
for cont in lista:
    linha += 1
    print(f"{linha:4} {cont:10.0f}   {pow(cont,2):10.0f}      {pow(cont,3):10.0f}         {pow(cont,1/2):5.2f}")
    if linha == 20 and len(lista)%20 != 0:
        print("   #      Valor     Quadrado            Cubo          Raiz")
        linha = 0

# 12. Escreva um algoritmo para ler o número de gols marcados pelo Grêmio e o número de gols marcados pelo Inter em
# um GRENAL. Escreva o Nome do Vencedor. Caso não haja vencedor deverá ser impresso a palavra EMPATE.

golsInter = int(input("Gols do Inter?"))
golsGremio = int(input("Gols do Grêmio?"))
if golsInter == golsGremio:
    print("EMPATE")
elif golsInter > golsGremio:
    print("INTER")
else:
    print("GRÊMIO")

# 33. Para participar da categoria OURO do 1º Campeonato Mundial de  Bolinha de Gude o jogador deve pesar
# entre 70 Kg (inclusive) e 80 Kg (inclusive) e medir de 1,75 m (inclusive) a 1,90 m (inclusive).
# Escreva um algoritmo para ler a altura e o peso de um jogador e determine Se o jogador está apto a participar do
# campeonato escrevendo uma das seguintes mensagens conforme cada situação.
# (a) ‘RECUSADO POR ALTURA’: Se somente a altura do jogador for inválida
# (b) ‘RECUSADO POR PESO’: Se somente o peso do jogador for inválido
# (c) 'TOTALMENTE RECUSADO’: Se a altura e o peso do jogador for inválido
# (d) ‘ACEITO': Se a altura e o peso do jogador estiverem dentro da faixa especificada

peso = float(input("Peso?"))
altura = float(input("Altura?"))

peso_ok = (70 <= peso <= 80)
altura_ok = (1.75 <= altura <= 1.90)

if peso_ok and altura_ok:
    print("ACEITO")
elif not peso_ok and not altura_ok:
    print("TOTALMENTE RECUSADO")
elif not peso_ok:
    print("RECUSADO POR PESO")
elif not altura_ok:
    print("RECUSADO POR ALTURA")

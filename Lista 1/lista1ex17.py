
comprimentoPista = float(input("Qual o comprimento da pista?"))
numeroVoltas = int(input("Qual o número de voltas?"))
numeroReabast = int(input("Qual o número de reabastecimentos?"))
consumo = float(input("Qual o consumo do carro (km/l)?"))

totalKmCorrida = (comprimentoPista * numeroVoltas)/1000;
kmReabast = totalKmCorrida / (numeroReabast + 1)
litrosMinimos = kmReabast / consumo

print("Nùmero mínimo de litros em cada reabastecimento:", litrosMinimos)


# Exercício 6

voto = -1
cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
nulos = 0
brancos = 0

while voto != 0:
    voto = int(input("Voto?"))
    if voto == 1:
        cand1 += 1
    elif voto == 2:
        cand2 += 1
    elif voto == 3:
        cand3 += 1
    elif voto == 4:
        cand4 += 1
    elif voto == 5:
        nulos += 1
    elif voto == 6:
        brancos += 1

print(f"Votos no candidato 1: {cand1}")
print(f"Votos no candidato 2: {cand2}")
print(f"Votos no candidato 3: {cand3}")
print(f"Votos no candidato 4: {cand4}")
print(f"Votos Nulos: {nulos}")
print(f"Votos Brancos: {brancos}")


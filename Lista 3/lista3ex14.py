# Exercício 14

valor = 1
soma = 0
cont = 0
contpos = 0
contneg = 0

while valor != 0:
  valor = float(input("Qual é o valor?"))
  if valor == 0:
      break
  soma += valor
  cont += 1
  if valor > 0:
      contpos += 1
  if valor < 0:
      contneg += 1

media = soma / cont
percneg = contneg/cont*100
percpos = contpos/cont*100

print(f"Média dos valores lidos: {media:.2f}")
print(f"Valores negativos: {contneg} ({percneg:.2f}%)")
print(f"Valores positivos: {contpos} ({percpos:.2f}%)")

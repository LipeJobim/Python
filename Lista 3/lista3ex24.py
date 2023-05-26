# Exercício 24

codigo = 0
cont = 0
soma1 = 0 # sem aumento
soma2 = 0 # com aumento

while codigo >= 0:
    codigo = int(input("Código do produto?"))
    if codigo < 0:
        break
    preco = float(input("Preço de Custo:"))
    novopreco = preco * 1.20

    cont += 1
    soma1 += preco
    soma2 += novopreco
    print(f"Código do produto: {codigo}  >  Novo Preço R$ {novopreco:.2f}")

media1 = soma1/cont
media2 = soma2/cont

print(f"Média dos Preços:  Custo R$ {media1:.2f}   Novo R$ {media2:.2f}")

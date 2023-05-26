# 10. Função para retornar o preço da maça (com parâmetros)


def preco_maca(qtde):
    if qtde < 12:
        return 0.30
    else:
        return 0.25


macas = int(input("Quantas maças foram compradas?"))
total = macas * preco_maca(macas)
print(total)

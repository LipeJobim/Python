# 10. Função para retornar se o número é par ou ímpar (com parâmetro)


def par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"


num = int(input("Qual é o número?"))
print(par_ou_impar(num))

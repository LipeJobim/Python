# 34. O banco GASTADOR Ltda. deseja utilizar o computador para determinar o limite da conta especial de seus
# clientes a partir do saldo da conta corrente e da poupança. Escreva um algoritmo para ler o saldo da conta
# corrente e da poupança de um cliente e Escreva o seguinte:
# (a) A mensagem: ‘SEM CONTA ESPECIAL’ Se o cliente NÃO possuir o requisito necessário para a conta especial.
#     (REQUISITO PARA POSSUIR CONTA ESPECIAL: o saldo em pelo menos uma das duas contas deve estar acima de R$1.000,00)
# (b) O valor do limite da conta conforme especificação abaixo: O valor limite da conta especial  fornecido ao cliente
#     deve ser o dobro do maior saldo (entre conta corrente e poupança) ou o triplo do menor saldo. Deve ser fornecido
#     o valor de limite maior entre essas 2 situações.
# OBS: Considere que os saldos da corrente e poupança não são iguais.

saldoCC = float(input("Saldo em Conta Corrente?"))
saldoPoupanca = float(input("Saldo em Poupança?"))

if (saldoCC > 1000) or (saldoPoupanca > 1000):
    if saldoCC > saldoPoupanca:
        limite1 = saldoCC * 2
        limite2 = saldoPoupanca * 3
    else:
        limite1 = saldoPoupanca * 2
        limite2 = saldoCC * 3
    if limite1 > limite2:
        limite = limite1
    else:
        limite = limite2
    print("Limite fornecido ao cliente:", limite)
else:
    print("SEM CONTA ESPECIAL")

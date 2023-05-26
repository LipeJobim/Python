# 5. Escreva um algoritmo para ler o ano de nascimento de uma pessoa e Escreva uma mensagem que diga Se ela poderá ou
# não votar este ano (não é necessário considerar o mês em que ela nasceu).

anonasc = int(input("Qual é o Ano de Nascimento?"))
anoatual = 2020
idade = 2020 - anonasc;
if idade >= 16:
    print("Pode votar com ", idade, "anos")
else:
    print("Não pode votar com", idade, "anos")

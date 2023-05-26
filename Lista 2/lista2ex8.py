# 8. Escreva um algoritmo que verifique a validade de uma senha fornecida pelo usuário. A senha válida é o número 1234.
# Deve ser impresso as seguintes mensagens:
# (a) ACESSO PERMITIDO caso a senha seja válida
# (b) ACESSO NEGADO caso a senha seja inválida.

senha = int(input("Qual é a senha?"))
if senha == 1234:
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO")


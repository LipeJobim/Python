# 2. Acrescente ao exercício acima a mensagem ‘Você foi REPROVADO! Estude mais.’ caso a média calculada seja
# menor que 8,0.

nota1 = float(input("Nota 1?"))
nota2 = float(input("Nota 2?"))
media = (nota1 + nota2) / 2
print(media)
if media >= 8:
    print("PARABÉNS! Você foi aprovado")
else:
    print("Você foi REPROVADO! Estude mais.")
# 6. As maçãs custam R$ 0,30 ser forem compradas menos do que uma dúzia, e R$ 0,25 ser forem compradas pelo menos doze.
# Escreva um algoritmo que leia o número de maçãs compradas, calcule e escreva o valor total da compra.

macas = int(input("Quantas maçãs foram compradas?"))
if macas < 12:
    print("Total da compra:", macas * 0.30)
else:
    print("Total da compra:", macas * 0.25)

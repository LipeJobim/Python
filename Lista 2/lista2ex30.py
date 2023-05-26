# 30. Escreva um algoritmo que leia a idade de 2 homens e 2 mulheres (considere que a idade dos homens será
# sempre diferente, assim como das mulheres). Calcule e escreva a soma das idades do homem mais velho com a
# mulher mais nova, e o produto das idades do homem mais novo com a mulher mais velha.

homem1 = int(input("Idade do Homem 1?"))
homem2 = int(input("Idade do Homem 2?"))
mulher1 = int(input("Idade da Mulher 1?"))
mulher2 = int(input("Idade da Mulher 2?"))

if homem1 > homem2:
    hvelho = homem1
    hnovo = homem2
else:
    hvelho = homem2
    hnovo = homem1

if mulher1 > mulher2:
    mvelha = mulher1
    mnova = mulher2
else:
    mvelha = mulher2
    mnova = mulher1

soma = hvelho + mnova
print("Soma do homem mais velho com a mulher mais nova:", soma)
produto = hnovo * mvelha
print("Produto do homem mais novo com a mulher mais velha:", produto)

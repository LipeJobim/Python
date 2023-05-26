altura = float(input("Qual é a altura da cozinha?"))
largura = float(input("Qual é a largura da cozinha?"))
comprimento = float(input("Qual é o comprimento da cozinha?"))
parede1 = altura*largura
parede2 = altura*comprimento
area = (2*parede1 + 2*parede2)
azulejos = area / 2;
print("Serão necessárias", azulejos, "caixas de azulejos")



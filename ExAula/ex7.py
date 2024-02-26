#Implemente um programa que leia um preço de um produto e mostre com 5% de desconto
valor = float(input("Valor do produto: "))
print(f"Valor do produto = R$ {valor}\nValor com desconto = R$ {valor-0.05*valor}")
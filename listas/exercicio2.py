
"""
Faça um programa que carregue uma lista com dez números
inteiros, informados pelo usuário. Em seguida, crie e
mostre uma lista resultante ordenada de maneira crescente
e crie e mostre uma lista resultante ordenada de maneira decrescente.
"""
n = []
for i in range(10):
    n.append(int(input("Digite um numero: ")))

n.sort()
print("Ordem crescente:", n)
n.sort(reverse=True)
print("Ordem crescente:", n)

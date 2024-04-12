"""
Faça um programa que carregue duas listas com nomes de animais, 
com 5 posições cada lista. Em seguida, crie uma lista resultante
da intercalação dessas duas listas. No final, mostre os itens
dessa nova lista.
"""

l1 = ['foca','guaxinim','gato','vaca','furão']
l2 = ['rato','paraguaio','dog','avestruz','pato']

new_list = [i for sublist in zip(l1,l2) for i in sublist]

print(', '.join(new_list))
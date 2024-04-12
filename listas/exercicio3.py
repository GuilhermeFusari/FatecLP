"""
Faça um programa que crie duas listas x e y, com dez números
inteiros cada uma. Em seguida, crie:

a) Uma lista resultante da união de x e y
  (todos os elementos de x e os elementos de y que não estão em x).

b) Uma lista resultante da diferença entre x e y
  (todos os elementos de x que não existam em y).

c) Uma lista resultante da some de x e y
  (soma de cada elemento de x com o elemento de y na mesma posição)
"""
x = [1,4,7,9,11,13,15,19,20,21]
y = [2,4,6,8,10,12,14,16,18,20]

#A
#Usando função ja existente
'''uniao = list(set(x).union(y))
print(uniao)'''
uniao = x + [i for i in y if i not in x]
print(uniao)

#B
diff = [i for i in x if i not in y]
print(diff)

#C
soma = [i + j for i, j in zip(x, y)]
print(soma)
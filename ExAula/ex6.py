#Suponhamos que tenhamos que pintar o muro de uma instituição, faça um programa que leia a altura e largura
#do muro e mostre a quantidade de tinta necessaria( 1 l de tinta pode pintar 2 m^2)
import math
altura = float(input("Altura: "))
largura = float(input("Largura: "))
pm = altura*largura
print(f'latas necessarias = {math.ceil(pm/2)}')
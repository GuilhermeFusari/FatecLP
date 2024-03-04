'''Escreva um programa que leia a velocidade de um carro. Se esta velocidade for maior que 80Km/h 
o programa deverá escrever uma mensagem na tela avisando que o usuário levou uma multa e o valor a ser pago. 
Considere R$ 7 reais por cada Km acima do limite.)'''
vel = float(input("Velocidade do carro: "))
if vel > 80:
    print(f"Você foi multado em {(vel-80)*7}")
    

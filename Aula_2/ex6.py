'''Faça um programa para jogar Jokenpô (clássico pedra, papel e tesoura) com você. 
Você deverá informar uma das opções, o programa deverá então sortear uma das três opções possíveis e mostrar quem ganhou na tela.'''
import random  
jogadas = ['Pedra', 'Papel', 'Tesoura']
player = input("Escolha pedra papel ou tesoura: ").lower()
bot = random.choice(jogadas)
print(f'\nSua jogada: {player} --- Jogada do Bot: {bot}\n')
if bot == player:
    print('Empate')
elif bot == 'Pedra' and player == 'papel':
    print('Voce ganhou!')
elif bot == 'Tesoura' and player == 'pedra':
    print('Voce ganhou!')
elif bot == 'Papel' and player == 'tesoura':
    print('Voce ganhou!')
else:
    print("Voce perdeu")
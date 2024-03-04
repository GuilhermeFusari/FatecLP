'''Faça um programa para jogar Jokenpô (clássico pedra, papel e tesoura) com você. 
Você deverá informar uma das opções, o programa deverá então sortear uma das três opções possíveis e mostrar quem ganhou na tela.'''
import random  
jogadas = ['Pedra', 'Papel', 'Tesoura']
player = input("Escolha pedra papel ou tesoura: ").lower()
bot = random.choice(jogadas)
print(f'\nSua jogada: {player} --- Jogada do Bot: {bot}\n')
match player:
    case 'pedra':
        if bot == 'Papel':
            print("Você perdeu!")
        elif bot == 'Tesoura':
            print("Voce ganhou!")
        else:
            print("Empate")
    case 'papel':
        if bot == 'Tesoura':
            print("Você perdeu!")
        elif bot == 'Pedra':
            print("Voce ganhou!")
        else:
            print("Empate")
    case 'tesoura':
        if bot == 'Pedra':
            print("Você perdeu!")
        elif bot == 'Papel':
            print("Voce ganhou!")
        else:
            print("Empate")

#I Faça um programa em que ele sorteie um número entre 0 e 5. O usuário deverá 
#então adivinhar este número e o programa deverá escrever na tela se ele acertou ou não.
import random

computador = random.randint(0, 5)
print(computador)

jogador = int(input('Digite um número entre 0 e 5'))

if jogador == computador:
  print('Você acertou o número')
else:
  print('Você errou')
  print('Não desista, tente novamente!')
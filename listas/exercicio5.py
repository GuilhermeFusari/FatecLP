"""
Implemente o jogo da forca. Um usuário deverá entrar
com uma palavra. Em seguida, outro usuário deverá indicar
as letras dessa palavra. Caso exista, deverá ser mostrada
as letras e as suas posições na palavra. Caso não exista,
o usuário perderá uma chance. No total, o usuário terá
6 chances para acertar.
"""
import os
print("---- JOGO DA FORCA----")
palavra = input("Jogador 1- Digite uma palavra: ")
os.system('cls')
print("Jogador 2 - Você tem 6 chances para acertar a palavra")
estado_da_palavra = ["_"]*len(palavra)
tentativas = 6
while tentativas !=0:
    guess = input("Jogador 2 - Digite uma letra: ")
    if guess in palavra:
        print("você acertou uma letra na posição {}".format(palavra.index(guess)))
        for i in range (len(palavra)):
            if guess == palavra[i]:
                estado_da_palavra[i] = guess
        print(estado_da_palavra)
        if ''.join(estado_da_palavra) == palavra:
            os.system('cls')
            print("Voce ganhou, a palavra era "+palavra)
            break
            
    else: 
        tentativas -= 1
        print(f"Tentativas restantes = {tentativas}")
        print(estado_da_palavra)

    
if tentativas == 0: 
    os.system('cls')
    print ("voce perdeu pois suas tentativas acabaram")
    print("A palavra era "+palavra)             

import sys
import os
from alunos import Alunos

def main():
    menu()
    
def menu():
    while True:
        try:
            os.system("cls")
            print("Sistema de Cadastro de Alunos")
            escolha = input("1 - Cadastrar um novo aluno \n2 - Informações de um aluno \n3 - Lista de alunos \n4 - Excluir um aluno \n5 - Fechar o programa \nOpção: ")
            match int(escolha):
                case 1:
                    aluno = cadastra_aluno()
                case 2:
                    infos(aluno)
                case 3:
                    lista_aluno()
                case 4:
                    exclui_aluno()
                case 5:
                    sys.exit()
        except ValueError:
            print("Digite um numero Válido")
def cadastra_aluno():
    os.system("cls")
    nome = input("Nome do aluno: ")
    idade = input("Idade: ")
    media= input("media do aluno: ")
    os.system("pause")
    return Alunos(nome,idade,media)
def exclui_aluno():
    ...
def infos(aluno):
    os.system("cls")
    print(aluno)
    os.system("pause")
def lista_aluno():
    ...


if __name__ == "__main__":
    main()
'''Faça um program que leia o ano de nascimento de uma pessoa e informe se ele ainda 
vai se alistar ao serviço militar ou se ele está no período de se alistar ou se ele perdeu o prazo para se alistar. 
Além disso, mostre também a quantidade de anos que falta para se alistar ou que passou do prazo.'''
idade = int(input("Idade: "))
if 17 <= idade <=22:
    print("Voce está no periodo de alistamento!")
elif idade < 17:
    print(f"Faltam {17-idade} ano(s) para voce pode se alistar")
else:
    print("Você passou do periodo de alistamento")

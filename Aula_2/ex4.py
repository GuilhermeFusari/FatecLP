'''Faça um programa para aprovar o empréstimo bancário para a compra de uma casa. 
O usuário deverá informar o valor da casa, a quantidade de parcelas que deseja pagar e seu salário.
O empréstimo deverá ser negado caso o valor da parcela exceda 30% do salário.'''
casa = float(input("Valor da casa: "))
parcela = int(input("Quantidade de parcelas: "))
salario = float(input("Salário: "))
vp = casa/parcela
if vp > salario*0.3 :
    print("Emprestimo negado!!")
else:
    print(f"Emprestimo Aceito:\nValor das parcelas = R${vp:.2f}")
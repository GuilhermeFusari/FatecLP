"""
Faça um programa que crie uma lista vazia.
Em seguida, o usuário deverá informar as notas de
trabalhos obtidas (pode variar de 0 até quantos trabalhos
forem informados). Por fim, mostre a média aritmética
das notas obtidas.
"""
notas = []
controle = int(input("Quantas notas serãol adicionadas? "))

for i in range(1,controle+1):
    notas.append(int(input(f"Nota {i}: ")))

media = sum(notas)/controle if controle !=0 else 0
print("A média do aluno é de:",media)
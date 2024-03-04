#Implemente um programa que leia 4 notas de um aluno e mostre a media aritimetica
notas = input("Notas: ").split()
notas = [float(nota) for nota in notas]
print('media = ',sum(notas)/len(notas))
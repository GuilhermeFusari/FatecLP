"""
Faça um programa em que o usuário deverá digitar
os nomes de dez alunos da sala de aula. Em seguida,
caso o programa encontre nomes repetidos, ele deverá
alterar o nome adicionando o número sequencial.
Por exemplo, se na lista tivermos dois "José",
após o processamento a lista deverá conter
"José 1" e "José 2".
"""
alunos = []
for i in range(10):
    alunos.append(input('Digite o nome de um aluno: '))

new_list = []
for aluno in alunos:
    if alunos.count(aluno) > 1:
        cont = 1
        while aluno + " " + str(cont) in new_list:
            cont += 1
        new_list.append(aluno + " " + str(cont))
    else:
        new_list.append(aluno)

for aluno in new_list:
    print(aluno)
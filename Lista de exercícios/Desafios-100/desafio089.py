'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um 
e permita que o usuário possa mostrar as notas de cada aluno individualmente - Desafio 089
'''
from time import sleep
from sys import exit

boletim = []
cores = ('\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;36m','\033[m')

while True:
    qtn = 0 #Quantidade de notas a serem usadas para calcular média

    #Adicionando os dados de cada aluno para uma lista individual
    aluno = []    

    nome = str(input("\nNome: ")) 
    aluno.append(nome)

    nota1 = float(input("Nota 1: "))
    while nota1 < 0 or nota1 > 10: #Limitando a nota entre 0 e 10
        nota1 = float(input(f"Digite uma nota {cores[2]}VÁLIDA{cores[5]} (Entre 0 e 10): "))
    aluno.append(nota1)
    qtn += 1

    nota2 = float(input("Nota 2: "))
    while nota2 < 0 or nota2 > 10: #Limitando a nota entre 0 e 10
        nota2 = float(input(f"Digite uma nota {cores[2]}VÁLIDA{cores[5]} (Entre 0 e 10): "))
    aluno.append(nota2)
    qtn += 1

    media = (nota1 + nota2)/qtn #Média das notas do aluno
    aluno.append(media)
    
    boletim.append(aluno[:]) #Copiando os dados para a lista de boletins dos alunos 
    del aluno 

    conf = str(input(f"\nDeseja continuar? [{cores[1]}S{cores[5]}/{cores[0]}N{cores[5]}]")).lower().strip()[0]
    while conf not in 'sn':
        conf = str(input(f'Por favor, insira apenas {cores[1]}S{cores[5]} para "Sim" e {cores[0]}N{cores[5]} para "Não": ')).lower().strip()[0]

    if conf in 'n':
        break

print("=" * 30)
print(f"""\n{'No.':<4} {cores[2]}{'NOME':<10}{cores[5]} {cores[2]}{'MÉDIA' :>8}{cores[5]}
{'-' * 25}""")


for i, d in enumerate(boletim):
    print(f"""{i:<4} {d[0] :<10} {d[3]:>8.1f}""")
print("-" * 25)

#Percorrendo a lista em busca do aluno solicitado
while True:
    aluno_indiv = int(input('\nMostrar notas de qual aluno? (Digite o No. do Aluno) - (999 para finalizar o programa) '))
    print(f"{cores[2]}PROCESSANDO...{cores[5]}")
    sleep(1.5)

    #Condição caso o usuário queira sair do programa
    if aluno_indiv == 999:
        print(f"{cores[2]}FINALIZANDO PROGRAMA...{cores[5]}")
        sleep(2)
        exit()
    #Condição caso o programa não encontre o aluno solicitado
    elif aluno_indiv >= len(boletim) or aluno_indiv < 0:
        print(f"{cores[0]}ALUNO NÃO ENCONTRADO{cores[5]}! Por favor, digite um No. de aluno {cores[3]}VÁLIDO{cores[5]}")
        sleep(2)
        continue

    print(f"Notas de {cores[2]}{boletim[aluno_indiv][0].upper()}{cores[5]}: [{boletim[aluno_indiv][1]},{boletim[aluno_indiv][2]}]")        
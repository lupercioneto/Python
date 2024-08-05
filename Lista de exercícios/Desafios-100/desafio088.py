'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos 
serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. - Desafio 088 
'''
from time import sleep
from random import randint
from sys import exit

cores = ('\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;36m','\033[m')

print(f"""{'=' * 40}
{'JOGUE NA MEGA SENA' :^40}
{'=' * 40}""")

print(f"\nCada jogo individualmente custa {cores[1]}R$5,00{cores[5]}")
sleep(1)

qttj = int(input(f"Quantos jogos gostaria de sortear? "))

#Limitador para um número de jogos válido
while qttj < 0:
    qttj = int(input(f"Por favor, digite um número de jogos {cores[3]}VÁLIDO{cores[5]}: "))

if qttj == 0:
    conf = str(input(f"Deseja sair do programa? [{cores[1]}S{cores[5]}/{cores[0]}N{cores[5]}]: ")).strip().lower()[0]
    while conf not in 'sn':
        conf = str(input(f'Por favor, digite apenas {cores[1]}S{cores[5]} para "Sim" e {cores[0]}N{cores[5]} para "Não": ')).lower().strip()[0]

    #Finalização do programa caso usuário deseje sair
    if conf == 's':
        print(f"\n{cores[2]}FINALIZANDO PROGRAMA...{cores[5]}")
        sleep(2)
        exit()
    else:
        qttj = int(input(f"Quantos jogos gostaria de sortear? "))

print(f"\n{cores[2]}SORTEANDO...{cores[5]}")
sleep(3)

jogos = []

#Criando listas equivalente a quantidade de jogos solicitados
for j in range(qttj):
    jogo_indiv = []

    #Irá adicionar o número na lista enquanto ela não tiver todos os 6 números
    while len(jogo_indiv) < 6:
        num = randint(1,60) #Gerando número aleatório a ser adicionado
        if num not in jogos: #Caso o número gerado já esteja no jogo, não será adicionado
            jogo_indiv.append(num)

    jogos.append(jogo_indiv[:]) #Adicionando uma cópia do enésimo jogo para a lista jogos 
    del jogo_indiv  

#Exibindo os jogos gerados para o usário (percorrendo a lista jogos)
print(f'\n{"=-" * 25}')
for c, jogo_indiv in enumerate(jogos): #Enumerando os jogos
    print(f"{cores[4]}JOGO {c + 1}{cores[5]}: {jogo_indiv}")
    sleep(0.7)

jgprice = qttj * 5 
print(f"\nO preço total de seus jogos será de {cores[1]}R${jgprice :.2f}{cores[5]}")
print(f'{"=-=" * 5} {cores[2]}{'< BOA SORTE! >'}{cores[5]} {"=-" * 9}')
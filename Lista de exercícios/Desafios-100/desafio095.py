'''
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador - Desafio 095
'''
from time import sleep

cores = {'red': '\033[1;31m', 'green': '\033[1;32m', 'yellow': '\033[1;33m', 
         'blue': '\033[1;34m', 'cyan': '\033[1;36m', 'default': '\033[m'}

jgall = list() #Lista onde será armazenado o aproveitamento de todos os jogadores inseridos

#Lendo os dados do jogador
while True:
    aprovjg = dict() #Dicionário onde será armazenado o aproveitamento de cada jogador individualmente
    qttgols = list() #Lista auxiliar para inserção de gols feitos/partida

    aprovjg['Nome'] = str(input("Nome do jogador: ")).strip().title() #Lendo o nome do jogador

    #Lendo a quantidade de partidas jogadas do jogador
    aprovjg['qttpartidas'] = int(input(f"Quantas partidas {cores['yellow']}{aprovjg['Nome']}{cores['default']} jogou? ")) 
    while aprovjg['qttpartidas'] < 0:
        aprovjg['qttpartidas'] = int(input(f"Por favor, insira um número {cores['green']}VÁLIDO{cores['standard']} de partidas"))

    #Lendo a quantidade de gols feitos/partida
    for p in range(0, aprovjg['qttpartidas']):
        qttgols.append(int(input(f"\t - Quantos gols foram feitos na {p+1}° partida? ")))

    aprovjg['qttgols/part'] = qttgols[:] #Criando uma cópia da quantidade de gols/partida para o dicionário
    jgall.append(aprovjg.copy()) #Adicionando o aproveitamento de um jogador à lista geral
    del qttgols
    del aprovjg
    
    #Confirmação para continuar (ou não) digitando mais dados
    conf = str(input(f"Deseja continuar? [{cores['green']}S{cores['default']}/{cores['red']}N{cores['default']}]: ")).upper().strip()[0]
    while conf not in 'SN':
        conf = str(input(f'Por favor, digite apenas {cores["green"]}S{cores["default"]} para "Sim" e {cores["red"]}N{cores["default"]} para "Não": ')).upper().strip()[0]

    if conf in 'N':
        break

print(f"{cores['yellow']}PROCESSANDO...{cores['default']}")
sleep(2.5)

#Tabela com algumas informações gerais dos jogadores
print(f"""\n{'-=' * 20}
{cores['yellow']}{'CÓDIGO' :<6}{'NOME' :>10}{'TOTAL DE GOLS' :>20}{cores['default']}""")

for i, j in enumerate(jgall):
    print(f"{i :>3}{j['Nome'] :>14}{sum(j['qttgols/part']) :^27}")
    sleep(0.6)
print('-=' * 20)

#Exibindo os dados de um jogador individualmente
while True:

    jg_indiv = int(input(f"\nMostrar dados de qual jogador? ({cores['cyan']}999{cores['default']} para encerrar): "))

    #Finalizando programa caso usuário deseje sair
    if jg_indiv == 999:
        print(f"{cores['yellow']}ENCERRANDO PROGRAMA...{cores['default']}")
        sleep(2)
        exit()

    #Limitando o usuário a escolher apenas os jogadores registrados
    while jg_indiv >= len(jgall) or jg_indiv < 0:
        jg_indiv = int(input(f"JOGADOR {cores['red']}INVÁLIDO!{cores['default']} Por favor, tente inserir um código presente na tabela: ")) 

        if jg_indiv == 999:
            print(f"{cores['yellow']}ENCERRANDO PROGRAMA...{cores['default']}")
            sleep(2)
            exit()

    print(f"{cores['yellow']}ANALISANDO...{cores['default']}")
    sleep(1.5)

    #Dados do jogador solicitado
    print(f"\n-- LEVANTAMENTO DO JOGADOR {cores['yellow']}{jgall[jg_indiv]['Nome']}{cores['default']}")
    for i, g in enumerate(jgall[jg_indiv]['qttgols/part']):
        print(f'\t- Na {i + 1}° partida, fez {g} gol(s)' if g != 0 else f"\t- Na {i + 1}° partida, não fez nenhum gol")
        sleep(0.6)

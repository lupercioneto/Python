'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato - Desafio 093
'''

aprovjg = dict()
qttgols = list() #Lista auxiliar para inserção de gols feitos/partida
cores = {'red': '\033[1;31m','green': '\033[1;32m','yellow': '\033[1;33m','blue': '\033[1;34m','standard': '\033[m'}

#Lendo os dados do jogador
aprovjg['Nome'] = str(input("Nome do jogador: ")).strip().title()

aprovjg['qttpartidas'] = int(input(f"Quantas partidas {aprovjg['Nome']} jogou? ")) 
while aprovjg['qttpartidas'] < 0:
    aprovjg['qttpartidas'] = int(input(f"Por favor, insira um número {cores['green']}VÁLIDO{cores['standard']} de partidas"))

#Lendo a quantidade de gols feitos/partida
for p in range(0, aprovjg['qttpartidas']):
    qttgols.append(int(input(f"     Quantos gols foram feitos na {p+1}° partida? ")))

aprovjg['qttgols/part'] = qttgols[:] #Criando uma cópia para o dicionário
del qttgols

#Exibindo o aproveitamento do jogador
print(f"\n{'=' * 41}")
print(f"O jogador {cores['yellow']}{aprovjg['Nome']}{cores['standard']} jogou {aprovjg['qttpartidas']} partidas")
for np, gols in enumerate(aprovjg['qttgols/part']):
    if gols != 0:
        print(f"    --> Na {np + 1}° partida, {aprovjg['Nome']} fez {gols} gol(s)")
    else: 
        print(f"    --> Na {np + 1}° partida, {aprovjg['Nome']} não fez nenhum gol")
print('=' * 41)

print(f"\nAo total, {cores['yellow']}{aprovjg['Nome']}{cores['standard']} fez {sum(aprovjg['qttgols/part'])} gols") 
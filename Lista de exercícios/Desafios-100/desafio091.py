'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado. - Desafio 091
'''
from random import randint
from time import sleep
from operator import itemgetter 

players = {'Player-1': randint(1,6), 'Player-2': randint(1,6), 'Player-3': randint(1,6), 'Player-4': randint(1,6)}
ranking = dict()
cores = {'red': '\033[1;31m', 'green': '\033[1;32m', 'yellow': '\033[1;33m', 'blue': '\033[1;34m', 'standard': '\033[m'}

print(f"{cores['yellow']}JOGANDO OS DADOS...{cores['standard']}\n")
sleep(2.5)

#Exibindo os resultados dos dados
print("=" * 30)
for k,v in players.items():
    print(f"{cores['yellow']}{k}{cores['standard']} tirou {v} em seu dado")
    sleep(1)
print("=" * 30)

#Organizando o dicionário por ordem decrescente dos dados através da biblioteca Operator (itemgetter())
ranking = sorted(players.items(), key=itemgetter(1), reverse=True) 

#Exibindo o rank dos players
print(f"{'== RANKING ==' :>25}")
for i, v in enumerate(ranking):
    print(f"  {i + 1}° lugar: {cores['green']}{v[0]}{cores['standard']} com o número {v[1]}") 

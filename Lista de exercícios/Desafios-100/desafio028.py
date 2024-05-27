'''
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar 
descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu - Desafio 028
'''
#Importando bibliotecas
from random import randrange 
from time import sleep

print('''Vamos jogar um jogo!\n Irei pensar em um número entre 0 e 5. Tente adivinhá-lo!
Pensando...''')
sleep(4) 
nc = randrange(5)
nu = int(input("Em que número eu pensei? "))

if nu == nc:
    print(f"Droga, você venceu!\n Eu pensei no número {nc} e você digitou {nu}")
else:
    print(f"Perdeu! Eu pensei no número {nc} e você digitou {nu}")
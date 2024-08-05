'''
Faça um programa que tenha uma função, que receba vários parâmetros com valors inteiros. Seu programa tem que analisar todos 
os valores e dizer qual é o maior - Desafio 099
'''
from time import sleep

cores = {'red': '\033[1;31m', 'green': '\033[1;32m', 'yellow': '\033[1;33m', 'blue': '\033[1;34m', 'standard': '\033[m'}

#Definindo função linedetail
def linedetail():
    print('-' * 50)
    

#Definindo a função srchMaior
def srchMaior(* num):

    linedetail()
    print("Analisando os valores...")

    if len(num) == 0:
        print("Nenhum número foi informado.")
        exit()

    for i, n in enumerate(num):
        print(f'{num[i]}', end=' ', flush=True)
        sleep(0.3)

    #Maior e menor valor informados
    maior = max(num)
    menor = min(num)

    print(f"""\n- Foram informados {len(num)} números.
- O {cores['yellow']}MAIOR{cores['standard']} valor informado foi {maior} 
- O {cores['blue']}MENOR{cores['standard']} valor informado foi {menor}""" if len(num) > 1 else f"""\n- Apenas 1 número foi informado
- O {cores['yellow']}MAIOR{cores['standard']} e {cores['blue']}MENOR{cores['standard']} valor informado é {maior}""")
    sleep(3)
 
#Programa Principal
srchMaior(1,2,3,4,6)
srchMaior(12,45,60,1,3,6,8,9,21,5)
srchMaior(3,4)
srchMaior(100)
srchMaior()
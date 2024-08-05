'''
Faça um programa que tenha uma lista chamada números e duas funções. 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''

from time import sleep
from random import randint

cores = {'red': '\033[1;31m', 'green': '\033[1;32m', 'yellow': '\033[1;33m', 'blue': '\033[1;34m', 'clean': '\033[m'}
nums = list()

#Definindo a função sortnum()
def sortnum():
    print(f"\n{cores['yellow']}SORTEANDO 5 VALORES...{cores['clean']}")
    for n in range(0,5):   
        nums.append(randint(1, 100)) 
        print(f"{nums[n]}", end=' ', flush=True)
        sleep(0.3)

#Definindo a função sumnums()
def sumnums():

    #Listas auxiliares para somar os números e facilitar a formatação
    pares = list()
    impares = list()

    #Somando os números PARES e formatando-os
    print(f"\n\nSomando os valores {cores['green']}PARES{cores['clean']} da lista {nums}, temos: ", end='')
    for n in (nums): #Percorrendo a lista de todos os números sorteados
        if n % 2 == 0: #Selecionando apenas os números pares 
            pares.append(n)        
            if len(pares) == 0: #Caso nenhum número PAR tenha sido sorteado
               print(f"\t--> Nenhum número {cores['green']}PAR{cores['clean']} foi sorteado.")
    print(f"{cores['green']}{sum(pares)}{cores['clean']}" if len(pares) >= 1 else '')
    


    #Somando os números ÍMPARES e formatando-os
    print(f"\nSomando os valores {cores['red']}ÍMPARES{cores['clean']} da lista {nums}, temos: ", end='')
    for n in nums: #Percorrendo a lista de todos os números sorteados
        if n % 2 != 0: #Selecionando apenas os números ímpares
            impares.append(n)

            if len(impares) == 0: #Caso nenhum número ÍMPAR tenha sido sorteado 
                print(f"\t--> Nenhum número {cores['red']}ÍMPAR{cores['clean']} foi sorteado.")
    print(f"{cores['red']}{sum(impares)}{cores['clean']}" if len(impares) >= 1 else '')

#Programa Principal
sortnum()
sumnums()

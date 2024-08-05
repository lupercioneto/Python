'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla. - Desafio 074
'''

from random import randint

#5 números randomizados dentro de uma tupla
nsort = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))

#Métodos max e min procuram o maior e menor valor da tupla, respectivamente
maior = max(nsort)
menor = min(nsort)

print(f"""Os números sorteados foram: {nsort}
O maior valor sorteado foi {maior}
O menor valor sorteado foi {menor}""")
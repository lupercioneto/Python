'''
Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta. - Desafio 086
'''
from time import sleep

matriz = [[],[],[],[],[],[],[],[],[]]
cores = ('\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[m')
cont = 0 #Variável auxiliar contadora para percorrer a lista 

for v in matriz[0:9]:
    num = int(input(f"Digite um valor para preecnher a matriz: "))
    matriz[cont].append(num)
    cont += 1

print(f"\n{cores[2]}ORGANIZANDO...{cores[4]}\n")
sleep(2.5)

print(f"""{matriz[0]} {matriz[1]} {matriz[2]}  
{matriz[3]} {matriz[4]} {matriz[5]}
{matriz[6]} {matriz[7]} {matriz[8]}""")

    

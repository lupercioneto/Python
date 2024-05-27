#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR. - Desafio 030
from time import sleep
n = int(input("Qual o número a ser analisado? "))
print("PROCESSANDO...")
sleep(3)

if n % 2 == 0:
    print("O número {} é \033[34mPAR\033[m" .format(n))
else:
    print("O número {} é \033[31mÍMPAR\033[m" .format(n)) 
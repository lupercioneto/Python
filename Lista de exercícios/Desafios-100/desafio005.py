#Faça um programa que leia um número e mostre seu sucessor e seu antecessor na tela - Desafio 005
from time import sleep
n = int(input("Digite um número: "))
print("\033[33mANALISANDO...\033[m")
sleep(3)
print("O sucessor de \033[1;30m{}\033[m é \033[32m{}\033[m e seu antecessor é \033[31m{}\033[m" .format(n,(n+1),(n-1)))
#Também é possível utilizar duas variáveis para a realização desse desafio
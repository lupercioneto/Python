#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome - Desafio 025
n = str(input("Qual o seu nome completo? ")).strip().lower()
srch = 'silva' in n
print("Seu nome possui o sobrenome silva? \n {}" .format(srch))

#Faça um programa que leia um ano qualquer e mostre se ele é bissexto. - Desafio 032
#Biblioteca sobre datas
from datetime import date 
from time import sleep

print("Olá, Usuário!\nQual ano gostaria de analisar? ")
sleep(1.7)

a = int(input("Para analisar o ano em que se encontra, digite 0: "))
print(f"\033[1;36mAnalisando...\033[m")
sleep(3)

if a == 0:
    a = date.today().year
if (a % 4 == 0) and (a % 100 != 0) or (a % 400 == 0): 
    print(f"O ano de \033[34m{a}\033[m é \033[1mbissexto\033[m")
else:
    print(f"O ano de \033[34m{a}\033[m \033[1mnão é bissexto\033[m")




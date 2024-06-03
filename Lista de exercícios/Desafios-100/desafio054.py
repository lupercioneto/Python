'''
Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''

from datetime import date
import sys
from time import sleep

#Pegar o ano atual do computador
todayy = date.today().year
maiores = 0 #Contador da quantidade de pessoas maiores de idade
menores = 0 #Contador da quantidade de pessoas menores de idade (zerado)
for i in range(1,8):
    an = int(input(f"Em que ano nasceu a {i}ª pessoa? "))
    while an > todayy or an < 1900:
        an = int(input(f"\033[1;31mERRO\033[m\nPOR FAVOR, INSIRA UM ANO DE NASCIMENTO ENTRE 1900 e {todayy}: "))
    idade = todayy - an
    
    #Condições para ser maior ou menor de idade
    if idade < 18:
        menores += 1 #Contador da quantidade de pessoas menores de idade 
    else:
        maiores += 1 #Contador da quantidade de pessoas maiores de idade
print("\n\033[33mANALISANDO...\033[m\n")
sleep(3)
    
#Condições - Se não houver nenhum maior/menor de idade
if menores == 0:
    print(f"Não há nenhum menor de idade.")
    sys.exit()
elif maiores == 0:
    print(f"Não há nenhum maior de idade.")
    sys.exit()
print(f"""Ao todo tivemos:
- \033[34m{maiores}\033[m pessoa(s) maior(es) de idade 
- \033[32m{menores}\033[m pessoa(s) menor(es) de idade""")

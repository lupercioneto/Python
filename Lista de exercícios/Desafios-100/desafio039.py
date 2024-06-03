'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. - Desafio 039
'''

from datetime import date
from time import sleep

#Inserção dos valores
an = int(input("Qual seu ano de nascimento? "))
todayy = date.today().year
while an > todayy or an < 1900:
    an = int(input("Por favor, insira apenas um ano de nascimento a partir de 1900 e o ano atual: ")) 

idade = todayy - an
print("\033[1;33mANALISANDO...\033[m")
sleep(2.5)

print(f"\nAno de nascimento: {an}")
print(f"Quem nasceu em {an} tem {idade} anos de idade em {todayy}\n")

#Condições
if idade == 18:
    print("Você deve se alistar \033[1;34mIMEDIATAMENTE\033[m!")
elif idade > 18:  
    print(f"Seu \033[1;32mALISTAMENTO\033[m foi em {an + 18}")
    print(f"Você já deveria ter se \033[1;32mALISTADO\033[m há {todayy - (an + 18)} ano(s)\n")
else: 
    print(f"Seu \033[1;32mALISTAMENTO\033[m será em {todayy + (18 - idade)}")
    print(f"Ainda faltam {18 - idade} ano(s) para seu alistamento\n")


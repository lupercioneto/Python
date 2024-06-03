'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento 
de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER - Desafio 041
'''
from time import sleep
from datetime import date

an = int(input("Ano de nascimento: "))
todayy = date.today().year
idade = todayy - an 
print("\n\033[33mANALISANDO...\033[m")
sleep(3)
print(f"\nO atleta possuí {idade} anos de idade")

#Condições
if idade <= 9:
    print("Classficação: \033[1;36mMIRIM\033[m")
elif idade <= 14:
    print("Classficação: \033[1;33mINFANTIL\033[m")
elif idade <= 19:
    print("Classficação: \033[1;32mJÚNIOR\033[m")
elif idade <= 25:
    print("Classficação: \033[1;35mSÊNIOR\033[m")
else:
    print("Classficação: \033[1;31mMASTER\033[m")
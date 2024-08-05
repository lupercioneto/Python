'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. - Desafio 092
'''
from datetime import date as dt  
from time import sleep

clt = dict()
cores = {'red': '\033[1;31m','green': '\033[1;32m','yellow': '\033[1;33m','blue': '\033[1;34m','standard': '\033[m'}

#Lendo os dados do indivíduo
clt['Nome'] = str(input("Nome: ")) #Nome do indivíduo

todayy = dt.today().year 
an = int(input("Ano de nascimento: "))
while an > todayy or an < 1900: #Limitando o ano de nascimento para que seja válido
    an = int(input(f"Por favor, digite um ano de nascimento {cores['blue']}VÁLIDO{cores['standard']}: "))
clt['Idade'] = todayy - an #Calculando a idade do indivíduo

clt['CTPS'] = int(input("Carteira de Trabalho (Digite 0 caso não tenha): "))
while clt['CTPS'] < 0:
    clt['CTPS'] = int(input(f"Digite uma Carteira de Trabalho {cores['green']}VÁLIDA{cores['standard']}"))
    
#Condições caso o indivíduo apresente (ou não) uma CTPS
if clt['CTPS'] == 0:
    print(f"\n{cores['yellow']}PROCESSANDO...{cores['standard']}\n")
    sleep(2.5)
    for k, v in clt.items():
        print(f"- {cores['blue']}{k}{cores['standard']}: {v}")
        sleep(0.6)

else:

    #Inserindo dados exclusivos para o indíviduo que informou ter CTPS
    clt['Ano de Contratação'] = int(input("Ano de contratação: "))
    clt['Salário'] = float(input("Salário: R$"))
    clt['Aposentadoria'] = clt['Idade'] + (35 - (todayy - clt['Ano de Contratação']))

    print(f"\n{cores['yellow']}PROCESSANDO...{cores['standard']}\n")
    sleep(2.5)

    #Exibindo os dados do indivíduo com CTPS
    for k, v in clt.items():
        if k == 'Salário':
            print(f"- {cores['green']}{k}{cores['standard']}: R${v:.2f}")
            sleep(0.6)
        elif k == 'Aposentadoria' or k == 'Idade':
            print(f"- {cores['yellow']}{k}{cores['standard']}: {v} anos")
            sleep(0.6)
        else:
            print(f"- {cores['blue']}{k}{cores['standard']}: {v}")
            sleep(1)
'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso. - Desafio 072
'''
from time import sleep

extens020 = ('zero','um','dois','três','quatro','cinco',
            'seis','sete','oito','nove','dez',
            'onze','doze','treze','quatorze','quinze',
            'dezesseis','dezessete','dezoito','dezenove','vinte')

cores = {'red':'\033[1;31m', 'green':'\033[1;32m', 'yellow':'\033[1;33m', 'blue':'\033[1;34m', 'standard':'\033[m'}

while True:
    num = int(input("Digite um número entre 0 e 20: "))

    #Restrição de aceitação de dados
    while num < 0 or num > 20:
        num = int(input("Por favor, digite apenas um número entre 0 e 20: "))

    #Leitura do número digitado por extenso
    print(f"O número digitado foi {extens020[num]}")

    conf = str(input(f"Deseja continuar? [{cores['green']}S{cores['standard']}/{cores['red']}N{cores['standard']}]: ")).upper().strip()[0]
    while conf not in 'SN': 
        conf = str(input(f'Por favor, digite apenas {cores["green"]}S{cores["standard"]} para "Sim" e {cores["red"]}N{cores["standard"]} para "Não": ')).upper().strip()[0]

    if conf in 'N':
        print(f"{cores['yellow']}ENCERRANDO PROGRAMA...{cores['standard']}")
        sleep(2.5)
        exit()
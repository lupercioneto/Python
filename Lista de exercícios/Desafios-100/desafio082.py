'''
Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas. - Desafio 082
'''
from time import sleep


listafull = list()
cores = ('\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[m')

while True:
    num = int(input("\nDigite um número: "))

    #Condição para não contabilizar números repetidos
    if num not in listafull:
        listafull.append(num)
    else:
        print(f"Números repetidos {cores[0]}NÃO SERÃO CONTABILIZADOS{cores[4]}\n")
        sleep(2)

    #Confirmação para continuar ou parar de inserir números
    conf = str(input(f"Deseja continuar? [{cores[1]}S{cores[4]}/{cores[0]}N{cores[4]}]: ")).lower().strip()[0]
    while conf not in 'sn':
        conf = str(input(f'Por favor, digite apenas {cores[1]}S{cores[4]} para "Sim" e {cores[0]}N{cores[4]} para "Não": ')).lower().strip()[0]

    if conf in 's': 
        continue
    else:
        break

listapares = list()
listaimpares = list()

#Percorrendo a lista e analisando quais deles são pares e ímpares, assim inserindo-os em suas respectivas listas 
for v in listafull: 
    if v % 2 == 0:
        listapares.append(v)
    else: 
        listaimpares.append(v)
print(f"{cores[2]}\nORGANIZANDO...{cores[4]}")
sleep(2.5)

print(f"""\n- Lista completa: {sorted(listafull)}
- Lista de números {cores[3]}PARES{cores[4]}: {sorted(listapares)}
- Lista de números {cores[2]}ÍMPARES{cores[4]}: {sorted(listaimpares)}""")

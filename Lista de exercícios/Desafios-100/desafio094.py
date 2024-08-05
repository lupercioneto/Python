'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e 
todos os dicionários em uma lista. 
No final, mostre: 

A) Quantas pessoas foram cadastradas 
B) A média de idade
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média - Desafio 094
'''

from time import sleep
 
dadosall = list()  
idades = list()
cores = {'red': '\033[1;31m', 'green': '\033[1;32m', 'yellow': '\033[1;33m','blue': '\033[1;34m', 'standard': '\033[m'}

while True:
    dadosplp = dict()

    #Inserindo os dados dos usuários
    dadosplp['Nome'] = str(input("\nNome: ")).strip().title()

    dadosplp['Sexo'] = str(input(f"Sexo [{cores['blue']}M{cores['standard']}/{cores['red']}F{cores['standard']}]: ")).strip().upper()[0]
    while dadosplp['Sexo'] not in 'MF':
        dadosplp['Sexo'] = str(input(f'Por favor, digite apenas {cores["blue"]}M{cores["standard"]} para "masculino" e {cores["red"]}F{cores["standard"]} para "feminino": ')).strip().upper()[0]

    dadosplp['Idade'] = int(input("Idade: "))
    while (0 < dadosplp['Idade'] < 124) == False:
        dadosplp['Idade'] = int(input("Por favor, insira uma idade entre 1 e 124 anos: "))

    idades.append(dadosplp['Idade'])    
    dadosall.append(dadosplp.copy()) #Enviando uma cópia do dicionário com o dado do usuário para a lista 
    del dadosplp
    
    #Confirmação para continuar ou não
    conf = str(input(f"Deseja continuar? [{cores['green']}S{cores['standard']}/{cores['red']}N{cores['standard']}]: ")).strip().upper()[0]
    while conf not in 'SN':
        conf = str(input('Por favor, digite apenas {cores["green"]}S{cores["standard"]} para "Sim" e {cores["red"]}N{cores["standard"]} para "Não": ')).strip().upper()[0] 
    
    if conf in 'N':
        break 

mediaidade = sum(idades)/len(dadosall) #Média das idades
del idades

#Contando quantas mulheres foram cadastradas 
qttF = 0
for i, p in enumerate(dadosall):
    if dadosall[i]['Sexo'] == 'F':
        qttF += 1

print(f'''\n{"=" * 50}
- Foram cadastradas {len(dadosall)} pessoas
- A média de idade do grupo é de {mediaidade :.2f} anos''')
print(f'- No grupo há {qttF} mulher(es)' if qttF !=0 else '- Nenhuma mulher foi cadastrada') 
print("- Lista com as pessoas com idade acima da média:\n")

#Listando as pessoas com uma idade acima da média
for i, p in enumerate(dadosall):
    if dadosall[i]['Idade'] > mediaidade and dadosall[i]['Sexo'] == 'M':
        print(f"\t{cores['yellow']}{dadosall[i]['Nome'].upper()}{cores['standard']} - Sexo: {cores['blue']}{dadosall[i]['Sexo']}{cores['standard']} - {dadosall[i]['Idade']} anos")
    elif dadosall[i]['Idade'] > mediaidade and dadosall[i]['Sexo'] == 'F':
        print(f"\t{cores['yellow']}{dadosall[i]['Nome'].upper()}{cores['standard']} - Sexo: {cores['red']}{dadosall[i]['Sexo']}{cores['standard']} - {dadosall[i]['Idade']} anos")
print(f'=' * 50)

'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.                                                                                                  
B) Uma listagem com as pessoas mais pesadas.                                                      
C) Uma listagem com as pessoas mais leves. - Desafio 084


NOTA: Refazer o código
'''
from time import sleep

plp = [] #Lista com os dados das pessoas cadastradas
dados = [] #Lista auxiliar para dados temporários
pesos = [] #Lista para armazenar pesos temporariamente
cores = ('\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[m')

while True:
    #Adicionando os dados para a lista auxiliar
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso (Kg): ")))

    #Fazendo uma cópia para a lista principal e deletando os dados temporários da lista "dados"
    plp.append(dados[:]) 
    dados.clear()

    conf = str(input(f"Deseja continuar? [{cores[1]}S{cores[4]}/{cores[0]}N{cores[4]}]")).lower().strip()[0]
    while conf not in 'sn': 
        conf = str(input(f'Por favor, digite apenas {cores[1]}S{cores[4]} para "Sim" e {cores[0]}N{cores[4]} para "Não": ')).lower().strip()[0]

    if conf in 's':
        continue
    else:
        break

for peso in plp:
    pesos.append(peso[:][1])

count = 0 #Contador de cadastrados
for pess in plp:
    count += 1
         
#Maior e menor peso dentre os listados
maior = max(pesos)   
menor = min(pesos)
pesos.clear()

print(f"\n{cores[2]}ANALISANDO...{cores[4]}")
sleep(2.5)

print(f'''\nQuantidade de pessoas cadastradas: {count}
- O {cores[3]}MAIOR{cores[4]} peso registrado foi de {maior :.2f} Kg 
- O {cores[0]}MENOR{cores[4]} peso registrado foi de {menor :.2f} Kg''')

print(f"\n--> Pessoas com {maior :.2f} Kg: ", end='')
for p in plp:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')

print(f"\n--> Pessoas com {menor :.2f} Kg: ", end='')
for p in plp:
    if p[1] == menor: 
        print(f"[{p[0]}]", end='')
 

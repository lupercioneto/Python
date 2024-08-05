'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. - Desafio 078
'''
from time import sleep

lista = []
cores = ('\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[m')

#Adicionando 5 números inteiros dentro da lista
for n in range(1,6):
    lista.append(int(input(f"Digite o {n}° número: ")))

print(f"\n{cores[2]}ANALISANDO...{cores[4]}\n")
sleep(2.6)
print(f"Você digitou os valores {lista}")

#Maior e menor valores
maior = max(lista)
menor = min(lista)

#Quantidade de vezes que o maior e menor valor apareceram
contmaior = lista.count(max(lista))
contmenor = lista.count(min(lista))

print(f"O {cores[1]}maior{cores[4]} valor digitado foi {maior}, apareceu {contmaior} vez(es) no(s) índice(s) ", end='')

#Percorrendo a lista, enumerando cada índice em busca do índice do(s) maior(es) número(s)
for i, v in enumerate(lista):
    if v == maior:
        print(f"{i}",end=' ')
print(f"\nO {cores[1]}menor{cores[4]} valor digitado foi {menor}, apareceu {contmenor} vez(es), no(s) índice(s) ", end='')

#Percorrendo  lista, enumerando cada índice em busca do índice do(s) menor(es) número(s)
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i}",end=' ')
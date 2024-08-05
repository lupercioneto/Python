'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares - Desafio 075
'''
from time import sleep

cores = ('\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[m')
num = []

#Adicionando os números digitados pelo usuário na lista num
for i in range(1,5):
    n = int(input(f"Digite o {i}° número: "))
    num.append(n)

#Convertendo uma lista em uma tupla
num = tuple(num)

print(f"\n{cores[2]}ANALISANDO...{cores[4]}")
sleep(3)

#Condição caso não há nenhum número 9 ou pelo menos um
if 9 not in num:
    print("\nO valor nove não foi digitado nenhuma vez")
else:
    print(f"O número 9 apareceu {cores[1]}{num.count(9)}{cores[4]} vez(es)")

#Condição para garantir saída caso o número 3 seja digitado ou não
if 3 not in num:
    print("O valor 3 não foi digitado em nenhuma posição")
else: 
    print(f"O valor 3 apareceu na {cores[3]}{num.index(3) + 1}ª{cores[4]} posição")

print("Os valores pares digitados foram:", end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
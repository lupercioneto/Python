'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados 
os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente - Desafio 085
'''
from time import sleep

numbers = [[],[]]
cores = ('\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[m')
for v in range(1,8):
    num = int(input(f"Digite o {v}° número: "))
    if num % 2 == 0: 
        numbers[0].append(num)
    else:
        numbers[1].append(num)

#Organizando as listas em ordem crescente
numbers[0].sort()
numbers[1].sort()

print(f"\n{cores[2]}ORGANIZANDO...{cores[4]}\n")
sleep(2.5)

print(f"""- Os números {cores[1]}PARES{cores[4]} digitados foram: {numbers[0]}
- Os números {cores[0]}ÍMPARES{cores[4]} digitados foram: {numbers[1]}""")
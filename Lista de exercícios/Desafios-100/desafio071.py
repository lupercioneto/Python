'''
Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues. 
- OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1 - Desafio 071
'''
from time import sleep

#Variáveis com preços das cédulas
cedulas = [50,20,10,1]
qtcl = []

print(f"""{'=' * 30}
{'\033[1;32mBANCO LUPPPS\033[m' :>30}
{'=' * 30}""")

vs = int(input("Qual valor gostaria de sacar? R$"))
print("\033[1;34mPROCESSANDO...\033[m\n") 
sleep(2.5)

for cedula in cedulas:
    qtc = vs // cedula #Irá contabilzar apenas a quantidade inteira de cédulas daquele valor necessáris 
    qtcl.append(qtc) #Adiciona a quantidade de células à lista qtcl
    vs %= cedula 

print(f"""Quantidade de cédulas:
R$50: {qtcl[0]} cédula(s) 
R$20: {qtcl[1]} cédula(s)
R$5: {qtcl[2]} cédula(s)
R$1: {qtcl[3]} cédula(s)
{"=" * 30}
Volte sempre ao \033[1;32mBANCO LUPPPS\033[m! Tenha um bom dia!""")
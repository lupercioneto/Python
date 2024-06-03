'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. 
Para os inferiores ou iguais, o aumento é de 15%. - Desafio 034
'''
from time import sleep
print("""Olá funcionário! Para saber mais sobre seu aumento, veja as informações abaixo: 
1. Salários de até \033[32mR$1.250,00:\033[m \033[33m+15%\033[m de aumento
2. Salários acima de \033[32mR$1.250,00:\033[m \033[33m+10%\033[m de aumento\n""")
sleep(6)

s = float(input("Qual seu salário atual? "))

if s > 1250:
    ns = s + (10/100 * s) 
if s <= 1250:
    ns = s + (15/100 * s)
print("\033[32mCALCULANDO...\033[m")
sleep(3)
print(f"\033[31mX\033[m Seu antigo salário era de \033[32mR${s :.2f}\033[m\n\033[32m✓\033[m Seu novo salário será de \033[32mR${ns :.2f}\033[m")


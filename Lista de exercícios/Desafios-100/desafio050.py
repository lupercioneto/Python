'''
Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o. - Desafio 050
'''
from time import sleep
soma = 0
qt = 0
for s in range(1,7):
    n = int(input(f"Digite o {s}° valor a ser somado: "))
    if n % 2 == 0:
        soma += n #Equivale a: soma = soma + n (variável "soma" recebe os valores inseridos no teclado (variável "n") e soma-os)  
        qt += 1 #Equivale a: qt = qt + 1 (variável "qt" recebe a quantidade de termos que atendem a condição descrita na linha 10)
print(f"\nQuantidade de números pares informados: \033[34m{qt}\033[m\nA \033[32msoma\033[m entre estes números resulta em {soma}")

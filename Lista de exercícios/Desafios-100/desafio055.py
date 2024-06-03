#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos. - Desafio 055
from time import sleep

maior = 0
menor = 0
for pessoa in range(1,6):
    p = float(input(f"Peso da {pessoa}ª pessoa (Kg): ")) 
    if pessoa == 1: #A primeira inserção sempre será a maior/menor enquanto outra não for inserida para ser comparada.
        maior = p
        menor = p
    else:
        #A cada absorção de pesos, a comparação será feita até que nenhum valor seja maior/menor que atual o absorvido     
        if p > maior: 
            maior = p
        if p < menor:
            menor = p 
print("\n\033[1;33mANALISANDO...\033[m\n")
sleep(3)
print(f"O maior peso lido foi \033[31m{maior :.2f}Kg\033[m\nO menor peso lido foi \033[34m{menor :.2f}Kg\033[m")
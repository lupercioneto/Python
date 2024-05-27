'''
 Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
 em que posição ela aparece a primeira vez e em que posição ela aparece a última vez - Desafio 026
'''

frs = str(input("Digite ua frase: ")).strip().lower()
cont = frs.count('a')
apar = frs[:].find('a') 
lastapar = frs[:].rfind('a')

print("""Nesta frase:  
- A letra "A" aparece {} vezes
- Sua primeira aparição foi na posição {} 
- Sua última aparição foi na posição {}""" .format(cont, (apar + 1), (lastapar + 1) ))
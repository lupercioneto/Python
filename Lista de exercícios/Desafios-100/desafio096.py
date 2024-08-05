'''
Faça um programa que tenha uma função chamada área(), 
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno. - Desafio 096
'''
from time import sleep

#Definindo a função para calcular a área de um terreno (Largura e Comprimento)
def area(l,c):
    a = l * c  
    print(f"A área de um terreno com {l :.2f} x {c :.2f} é de {a :.2f}m².")

#Programa principal
cores = {'red': '\033[1;31m','green': '\033[1;32m','yellow': '\033[1;33m',
         'blue': '\033[1;34m','cyan': '\033[1;36m','clean': '\033[m'}

print(f"""\n{cores['yellow']}CONTROLE DE TERRENOS{cores['clean']}
{'-' * 20}""")
area(float(input("LARGURA (m): ")), float(input("COMPRIMENTO (m): "))) #Recebendo os parâmetros diretamente pelo teclado

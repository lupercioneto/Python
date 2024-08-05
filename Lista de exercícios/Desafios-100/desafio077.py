'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais - Desafio 077
'''

palavras = ('Kleber','Joaquim','Joseph','Carla','Joana','Curso','Playstation','Xbox','Nintendo','Insomniac')

#Aninhamento em tuplas
for p in palavras:
    print(f"\nNa palavra {p.upper()} temos", end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(),end=' ')
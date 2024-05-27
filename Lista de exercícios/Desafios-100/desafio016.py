#Crie um programa que leia um número real e mostre sua porção inteira - Desafio 016
from math import trunc
n = float(input("Digite um número real:"))
i = trunc(n)
print("A parte inteira do número {} é {}" .format(n, i))
#A funcionalidade "trunc" da biblioteca "math" retorna a porção inteira de um número real (float)

#Também é possível realizar este exercício sem importar a biblioteca "math"
num = float(input("Digite um número real: "))
print("A parte inteira do número {} é {}" .format(num, int(num)))
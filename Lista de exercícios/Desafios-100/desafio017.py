#Crie um programa que leia o valor dos dois catetos de um triângulo retângulo e mostre o valor da hipotenusa
from math import hypot

co = float(input("Digite o valor do cateto oposto:"))
ca = float(input("Digite o valor do cateto adjacente:"))
h = hypot(co, ca)
print("O valor da hipotenusa, com os catetos {} e {} é igual a {:.2f}" .format(co, ca, h))

#Também é possível realizar esta atividade sem importar a biblioteca "math"
co2 = float(input("Digite o valor do cateto oposto:"))
ca2 = float(input("Digite o valor do cateto adjacente:"))
hi = ((co ** 2) + (ca ** 2)) ** (1/2)
print("O valor da hipotenusa, com os catetos {} e {} é igual a {:.2f}" .format(co, ca, h))
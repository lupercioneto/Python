#Crie um programa que leia um número e imprima seu dobro, seu triplo e sua raiz quadrada - Desafio 006
"""from time import sleep

n = float(input("Digite um número: "))
d = n * 2
t = n * 3
r = n**(1/2)

print("\033[32mCALCULANDO...\033[m")
sleep(3)

print(f"O dobro do número {n} é \033[34m{d}\033[m\nSeu triplo é \033[31m{t}\033[m\nE sua raiz quadrada é \033[36m{r :.2f}\033[m")
"""
#Utilizando a biblioteca Math

from time import sleep
from math import sqrt

n1 = float(input("Digite um número: "))
dobro = n1 * 2
triplo = n1 * 3
raiz = sqrt(n1)
print("\033[1;32mCALCULANDO...\033[m")
sleep(2.5)

print(f"""- Dobro de {n1}: {dobro}
- Triplo de {n1}: {triplo}
- Raiz quadrada de {n1}: {raiz :.2f} """)

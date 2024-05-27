'''Crie um programa que leia a altura e a largura de uma parede e calcule a sua área. 
Em seguida, calcule a quantidade de tinta necessária para pintá-la.
Leve em consideração: 1L de tinta pinta 2m^2
- Desafio 011
''' 
from time import sleep

a = float(input("Digite a \033[33maltura\033[m da parede: "))
l = float(input("Digite a \033[34mlargura\033[m da parede: "))
area = (a * l)

#A cada 2 metros quadrados, 1 litro de tinta será usado para pintar a parde
tinta = area / 2
print("\n\033[32mCALCULANDO...\033[m")
sleep(3)
print("A área da sua parede {} x {} é de {} m^2" .format(a, l, area))
sleep(2)
print("A quantidade de tinta necessária (em litros) para pintar esta parede é de {}{}L{}" .format('\033[36m',tinta,'\033[m'))

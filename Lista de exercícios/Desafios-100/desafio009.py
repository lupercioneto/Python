#Faça um programa que leia um número e exiba na tela toda a sua tabuada - - Desafio 009
n = int(input("Digite um número para ver sua tabuada:"))
print("\n", '=' * 12)
print(f"{n :2} x 1 = {n*1} \n {n} x 2 = {n*2} \n {n} x 3 = {n*3} \n {n} x 4 = {n*4} \n {n} x 5 = {n*5} \n {n} x 6 = {n*6} \n {n} x 7 = {n*7} \n {n} x 8 = {n*8} \n {n} x 9 = {n*9} \n {n} x 10 = {n*10}")
print('=' * 12)
#Também é possível usar vários prints ou .format
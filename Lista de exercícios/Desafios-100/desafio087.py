'''
Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.  
B) A soma dos valores da terceira coluna. 
C) O maior valor da segunda linha. - Desafio 087
'''

'''
Objetivo Extra: Tentar fazer este desafio com apenas um laço de reptição for
'''
from time import sleep

matriz = [[0,0,0],[0,0,0],[0,0,0]]
cores = ('\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[m')

#Variáveis contadoras
somapares = soma3column =  0

#Inserção e exibição dos números na matriz (Linhas 11 e 16)
for line in range(0,3):
    for column in range(0,3):
        matriz[line][column] = int(input(f"Digite um número na posição {line}, {column}: "))
print("=" * 35)

print(f"\n{cores[2]}ORGANIZANDO A MATRIZ...{cores[4]}\n")
sleep(3)

for line in range(0,3):
    for column in range(0,3):
        print(f"[{matriz[line][column]:^5}]", end='')
    print()

#Percorrendo a lista e somando os valores pares
for line in range(0,3):
    for column in range(0,3):
        if matriz[line][column] % 2 == 0:
            somapares += matriz[line][column]

#Percorrendo a lista e somando os valores da 3° coluna
for line in range(0,3):
    for column in range(0,3):
        if column == 2:
            soma3column += matriz[line][2]

#Percorrendo a lista e pegando o maior valor da linha 2
for line in range(0,3):
    if line == 1:
        for column in range(0,3):
            maior = max(matriz[1])

print(f"""\n- A soma dos números {cores[3]}PARES{cores[4]} da matriz é igual a {somapares}
- A soma dos números da {cores[1]}3° COLUNA{cores[4]} da matriz é igual a {soma3column}
- O {cores[0]}MAIOR{cores[4]} valor da 2° {cores[2]}LINHA{cores[4]} é {maior}""")



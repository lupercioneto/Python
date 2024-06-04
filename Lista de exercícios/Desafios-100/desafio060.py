#Faça um programa que leia um número qualquer e mostre o seu fatorial.

#Método usando biblioteca math e função factorial
from time import sleep
from math import factorial

#Inserção de dados
n = int(input("""Digite um número 
para calcular seu Fatorial: """))

print("\n\033[1;33mPROCESSANDO...\033[m")
sleep(3)

f = factorial(n) 
print(f"""\nO fatorial de {n} é igual a {f}""")
print("=-=" * 10)

# --------------------------------------------------------------------------------


#Método usando estrutura de repetição (While)
from time import sleep 

#Inserção de dados
n1 = int(input("""\nDigite um número
para calcular seu Fatorial: """))
c = n1
f = 1

print('\n\033[1;33mCALCULANDO...\033[m\n')
sleep(3)

#Estrutura de geração de fatorial
while c > 0:
    print(f'{c}', end='')
    print(" x " if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
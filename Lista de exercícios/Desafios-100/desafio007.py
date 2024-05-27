#Desenvolva um programa que leia as duas notas de um aluno, calcule e faça sua média - Desafio 007
from time import sleep
n1 = float(input("Digite a \033[34mprimeira\033[m nota do aluno: "))
while n1 < 0 or n1 > 10:
    n1 = float(input("Por favor, digite uma nota \033[32mválida\033[m, entre 0 e 10: "))
n2 = float(input("Digite a \033[33msegunda\033[m nota do aluno: "))
while n2 < 0 or n2 > 10:
    n2 = float(input("Por favor, digite uma nota \033[32mválida\033[m, entre 0 e 10: "))

#Cálculo da média do aluno 
m = (n1 + n2)/2   
print("\n\033[32mCALCULANDO...\033[m")
sleep(3)

print("A média das notas do aluno é \033[34m{:.1f}\033[m" .format(m))
#Cuidado com a ordem de precedência! PEMDAS 
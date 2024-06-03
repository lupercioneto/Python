# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. - Desafio 035
from time import sleep
print('-=-' * 9)
print("\033[36mAnalisador de Triângulos △\033[m")
print('-=-' * 9)
print("Irei analisar se é possível construir um triângulo\ncom base nas medidas que me der!\n")
sleep(3)

c1 = float(input("Digite a primeira medida: "))
c2 = float(input("Digite a segund medida: "))
c3 = float(input("Digite a terceira medida: "))
print("\n\033[33mANALISANDO...\033[m")
sleep(3)

#Módulos de cada segmento do trângulo (função "abs" retorna o valor absoluto/módulo de um número)
abs_1 = abs(c2 - c3)
abs_2 = abs(c1 - c3)
abs_3 = abs(c1 - c2)

#Soma dos outros dois lados para cada segmento do triângulo
sum_1 = c2 + c3
sum_2 = c1 + c3
sum_3 = c1 + c2

if abs_1 < c1 < sum_1 and abs_2 < c2 < sum_2 and abs_3 < c3 < sum_3:
    print(f"Os valores de \033[31m{c1}, {c2} \033[me\033[m \033[31m{c3}\033[m podem formar um triângulo! \033[32m△\033[m\n")
else:
    print("Os valores fornecidos não formam podem formar um triângulo \033[31m△\033[m\n")


 
    
 

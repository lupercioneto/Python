'''
 Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, 
 de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO  - Desafio 040
'''
from time import sleep
import sys #Finalizar o código imediatamente utilizando sys.exit()

print("Insira as notas do aluno logo abaixo:")
sleep(1)
n1 = float(input("Primeira nota: "))
while n1 > 10 or n1 < 0:
    n1 = float(input("Por favor, insira uma nota \033[32mválida\033[m, entre 0 e 10: "))

n2 = float(input("Segunda nota: "))
while n2 > 10 or n2 < 0:
    n2 = float(input("Por favor, insira uma nota \033[32mválida\033[m, entre 0 e 10: "))

m = (n1 + n2)/2
print("\n\033[33mCALCULANDO...\033[m\n")
sleep(3)

#Condições
if m >= 7:
    print("Situação do aluno: \033[1;34mAPROVADO\033[m")  
elif m < 5.0: 
    print("Situação do aluno: \033[1;31mREPROVADO\033[m")
elif 5.0 < m < 6.9:
    print("Situação do aluno: \033[1;33mAVALIAÇÃO FINAL\033[m")
print(f"A média entre as notas {n1 :.1f} e {n2 :.1f} é \033[32m{m :.1f}\033[m")

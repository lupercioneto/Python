#Faça um programa que leia três números e mostre qual é o maior e qual é o menor
from time import sleep
print("Olá! Digite abaixo os números a serem comparados!")
sleep(3)
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

#Verificando o menor número
menor = n1 #Uso de variável auxiliar
if n2 < n1 and n2 < n3: 
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

#Verificando o maior número
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3 
print("\n\033[33mANALISANDO...\033[m")
sleep(3)

print(f"\nO menor valor digitado foi \033[34m{menor}\033[m\nO maior valor digitado foi \033[31m{maior}\033[m")

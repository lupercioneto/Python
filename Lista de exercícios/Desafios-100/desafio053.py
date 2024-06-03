'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços e acentos. Exemplos de palíndromos:
'''
from time import sleep

#Inserção dos dados
f = str(input("Digite uma palavra ou frase: ")).strip().lower()
fwws = ''.join(f.split()) #Separação da palavra/frase em uma lista e junção da mesma com um espaço vazio entre elas (Espaço vazio != White Space)
revers = fwws[::-1] #Leitura da palavra/frase de trás para frente (start: -1, end: 0, step: -1)
print("\n\033[33mANALISANDO...\033[m\n")
sleep(3)
print(f"O inverso de {fwws} é {revers}")

#Condições
if fwws[:] == revers:
    print("A frase digitada é um \033[34mPALÍNDROMO\033[m")
else:
    print("A frase digitada \033[31mNÃO é um PALÍNDROMO\033[m")
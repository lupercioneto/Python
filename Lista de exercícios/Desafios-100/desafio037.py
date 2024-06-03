'''
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário 
escolher qual será a base de conversão: 
1 para binário, 2 para octal e 3 para hexadecimal - Desafio 037
'''
from time import sleep

#Apresentação
print("=-=" * 9)
print(f"\033[1;32mBase de Conversão Numérica\033[m")
print("=-=" * 9)
d = int(input("Digite um número: "))

#Escolha de conversão
print("""\nPara qual base deseja converter?
[ 1 ] - \033[1;32mBinário\033[m
[ 2 ] - \033[1;33mOctal\033[m
[ 3 ] - \033[1;34mHexadecimal\033[m\n""")
c = int(input("Escolha a forma de conversão: "))
print("\033[35mPROCESSANDO...\033[m")
sleep(3)

#Condições aninhadas
if c == 1:
    print(f"{d} convertido para \033[1;32mBINÁRIO\033[m é {bin(d)[2:]}")
elif c == 2:
    print(f"{d} convertido para \033[1;33mOCTAL\033[m é {oct(d)[2:]}")
elif c == 3:
    print(f"{d} convertido para \033[1;34mHEXADECIMAL\033[m é {hex(d)[2:]}")
else: 
    print("Por favor, insira um número \033[32minteiro!\033[m")

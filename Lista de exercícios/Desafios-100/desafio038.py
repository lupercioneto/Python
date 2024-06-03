'''
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais. - Deasfio 038
'''
from time import sleep
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
print("\n\033[34mANALISANDO...\033[m")
sleep(3)

#Condições
if n1 > n2: 
    print(f"O \033[31mprimeiro\033[m número é maior \033[1m({n1} > {n2})\033[m")
elif n2 > n1:
    print(f"O \033[32msegundo\033[m número é maior \033[1m({n2} > {n1})\033[m")
else:
    print("Os dois números são iguais ({} = {})" .format(n1, n2))
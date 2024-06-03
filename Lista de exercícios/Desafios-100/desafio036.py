'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado. - Desafio 036
'''
from time import sleep

print(f"""\033[36m<--------------------------->\033[m
  \033[1mEmpréstimos Residenciais\033[m
\033[36m<--------------------------->\033[m""")

#Inserção de valores
pc = float(input("Preço da casa: R$"))
scompr = float(input("Salário do comprador: R$"))
af = int(input("Quantos anos de financiamento? "))

print("\n||| \033[32mCALCULANDO...\033[m |||\n")

p = pc/(12 * af)
sleep(3)

print(f"Para pagar uma casa de \033[32mR${pc :.2f}\033[m em \033[1;34m{af}\033[m anos, a prestação será de R$\033[32m{p :.2f}\033[m")
if p > (30/100 * scompr):
    print("Empréstimo \033[31mNEGADO!\033[m\nA prestação \033[1mEXCEDEU 30%\033[m de seu salário")
else: 
    print("Empréstimo \033[32mCONCEDIDO!\033[m")

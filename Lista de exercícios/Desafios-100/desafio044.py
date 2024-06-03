'''
Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal 
- 3x ou mais no cartão: 20% de juros - Desafio 044
'''
from time import sleep

print(f"""{'=' * 10} 
\033[1mLOJAS LUPS\033[m
{'=' * 10}""")
p = float(input("Preço das compras: R$"))

print("""FORMAS DE PAGAMENTO:
[ 1 ] À vista \033[32m(dinheiro/cheque)\033[m
[ 2 ] À vista \033[35m(cartão)\033[m
[ 3 ] 2x no \033[35mcartão\033[m
[ 4 ] 3x ou mais no \033[35mcartão\033[m""")

fp = int(input("Escolha sua opção: "))
while fp <= 0 or fp > 4:
    fp = int(input("Forma de pagamento \033[31minválida!\033[m Por favor, digite entre 1 e 4: "))
print("\033[1;33mPROCESSANDO...\033[m")
sleep(2.5)

#Condições
if fp == 1:
    pavs = p - (10/100 * p)
    print(f"Sua compra de R${p :.2f} custará \033[32mR${pavs :.2f}\033[m, com 10% de desconto\n")
elif fp == 2:
    pavsc = p - (5/100 * p)
    print(f"Sua compra de R${p :.2f} custará \033[32mR${pavsc :.2f}\033[m, com 5% de desconto\n")
elif fp == 3: 
    parc = int(input("Pagamento em 1 ou 2 parcelas? "))
    if parc == 1: 
        print(f"O preço da sua compra será de \033[32mR${p :.2f}\033[m\n")
    else:
        print(f"O preço da sua compra, parcelada em duas vezes será de \033[32mR${p/2 :.2f}\033[m, sem acréscimos.\n")
elif fp == 4:
    parcelas = int(input("Quantas parcelas?\nNOTA: Parcelamos em até 12x \033[31m(COM JUROS - 20%)\033[m "))
    while parcelas < 3 or parcelas >= 13:
        parcelas = int(input("Por favor, selecione de 3 a 12 parcelas: "))
   
    tj = p + (20/100 * p)
    pp = tj/parcelas
    print("\033[1;33mPROCESSANDO...\033[m")
    print(f"""\nSua compra será parcelada em {parcelas}x de \033[32mR${pp :.2f}\033[m
Sua compra de R${p :.2f}, ao final custará \033[32mR${tj :.2f}\033[m\n""")
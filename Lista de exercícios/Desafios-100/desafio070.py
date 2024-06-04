'''
Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato - Desafio 070
'''
from time import sleep
from decimal import Decimal, getcontext

#Definindo a precisão dos decimais monetários (R$)
getcontext().prec = 10

totalprice = qtprodut = cheaprodut = qtprodut1000 = cpp = 0 #Variáveis de contagem
print(f"""{'=' * 15 :^15}
{'LOJAS LUPPPS' :^15}
{'=' * 15 :^15}""")
while True:
    name = str(input("Nome do produto: "))
    qtprodut += 1 #Quantidade de produtos comprados

    price = input("Preço: R$").replace(',', '.') #Ajustando o preço para aceitar valor monetário com vírgulas
    pricedec = Decimal(price) #Convertendo a string em um decimal

    contin = str(input("Quer continuar? [\033[34mS\033[m/\033[31mN\033[m]")).strip().upper()[0]
    while contin not in 'SN':
        contin = str(input('Por favor, digite apenas \033[34mS\033[m para "Sim" ou \033[31mN\033[m para "Não": ')).upper().strip()[0]
    
    #Preço total da compra
    totalprice += pricedec

    #Produtos que custam mais de R$1000
    if pricedec > 1000: 
        qtprodut1000 += 1

    #Produto mais barato
    if qtprodut == 1:
        cheaprodut = name
        cpp = pricedec
    else: 
        if cpp > pricedec:
            cheaprodut = name
            cpp = pricedec
        
    #Saída do loop caso o usuário deseje para de inserir 
    if contin in 'N': 
        break
print("\n\033[1;32mCALCULANDO...\033[m")
sleep(2.5)
print(f"""\n- Quantidade de produtos comprados: {qtprodut}
- Preço total da compra: \033[32mR${totalprice :.2f}\033[m
- Há {qtprodut1000} produto(s) custando mais de \033[32mR$1000,00\033[m
- O produto mais barato foi \033[1;34m{cheaprodut.upper()}\033[m que custa \033[32mR${cpp :.2f}\033[m""")
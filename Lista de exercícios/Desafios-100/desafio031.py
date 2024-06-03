'''
 Desenvolva um programa que pergunte a distância de uma viagem em Km.
 Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km 
 e R$0,45 parta viagens mais longas - Desafio 031
'''
from time import sleep

print(f"""Olá! Irá fazer uma viagem? A seguir seguem os preços das passagens:  
     - Percursos de até 200 Km: \033[32mR$0,50/km\033[m 
     - Percursos +200 Km: \033[32mR$0,45/km\033[m
     ---> Viagens com mais de 200 Km estão em \033[33mpromoção!\033[m""")
sleep(6)

d = float(input("\nQual a distância a ser percorrida? "))
if d <= 200:
    pv1 = 0.50 * d
    print("O preço da sua passagem será de \033[32mR${:.2f}\033[m\nTenha uma boa viagem!\n" .format(pv1))  
else: 
    pv2 = 0.45 * d
    print("""O preço da sua passagem será de \033[32mR${:.2f}\033[m 
    \033[31mNOTA\033[m: Preço calculado com desconto da promoção de percurso +200 Km \n""" .format(pv2))

#Crie um conversor de moedas - - Desafio 010
from time import sleep

r = float(input("Quanto dinheiro você tem atualmente? R$"))
print("\n\033[32mANALISANDO...\033[m")
sleep(4)

#Cotação do dia 02/04/2024 (04/02/2024, US format)
D = r / 5.06
L = r / 6.35
E = r / 5.44
Y = r / 0.033
print("-" * 39)
print("Com R${}{:.2f}{} você pode comprar {}$US {:.2f}{}" .format('\033[32m',r ,'\033[m','\033[32m', D,'\033[m'))
print("Com R${}{:.2f}{} você pode comprar {}{:.2f}€{}" .format('\033[32m', r,'\033[m', '\033[32m', E, '\033[m'))
print("Com R${}{:.2f}{} você pode comprar {}{:.2f}£{}" .format('\033[32m', r, '\033[m', '\033[32m', L, '\033[m'))
print("Com R${}{:.2f}{} você pode comprar {}{:.2f}¥{}" .format('\033[32m', r, '\033[m', '\033[32m', Y, '\033[m'))
print("-" * 39)

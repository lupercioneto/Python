'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem 
dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite. - Desafio 029
'''
from time import sleep

v = float(input("Qual a velocidade do veículo? "))
print("PROCESSANDO...")
sleep(2)

m = 7 * (v - 80)
if v <= 80:
    print("Tenha um bom dia! Dirija com cuidado!")
else:
    print(f"""MULTADO! Limite de velocidade de 80km/h excedido!
Você deve pagar uma multa de R${m :.2f}!
Tenha um bom dia e dirija com segurança!""")
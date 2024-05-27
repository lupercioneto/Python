#Escreva um programa que leia um valor em metros e o exiba em centímetros e milímetros converta - Desafio 008
from time import sleep
v = float(input("Digite um valor, em metros: "))
print("\n\033[32mCALCULANDO...\033[m")
sleep(3)

#Conversão do sistema métrico
km = (v/1000)
hc = (v/100)
dam = (v/10)
dm = (v * 10)
cm = (v * 100)
mm = (v * 1000)
print(f"\nA medida de \033[36m{v}\033[mm corresponde a:\n{km}km\n{hc}hc\n{dam}dam\n{dm}dm\n{cm:.2f}cm\n{mm :.2f}mm\n")

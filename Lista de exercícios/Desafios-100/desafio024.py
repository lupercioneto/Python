#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO” - Desafio 024
nc = str(input("Em que cidade você nasceu?" )).strip()
a = nc.lower().find("santo")
aux = a == 0
print("Sua cidade começa com santo? \n {}" .format(aux))

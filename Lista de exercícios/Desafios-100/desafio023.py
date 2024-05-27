#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados - Desafio 023
print("Bem-vindo ao analisador de dígitos numéricos!")
num = int(input("Digite abaixo um número para ser analisado (limite: 9999):"))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("Unidade do número {}: {}" .format(num, u))
print("Dezena do número {}: {}".format(num, d))
print("Centena do número {}: {}" .format(num, c))
print("Milhar do número {}: {}" .format(num, m))

#É possível otimzar este código através do uso de ifelse

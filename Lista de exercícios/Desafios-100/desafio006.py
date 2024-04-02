#Crie um programa que leia um número e imprima seu dobro, seu triplo e sua raiz quadrada - Desafio 006
n = int(input("Digite um número:"))
d = n * 2
t = n * 3
r = n**(1/2)
print("O dobro do número {} é {} \n Seu triplo é {} \n E sua raiz quadrada é {:.2f}" .format(n, d, t, r))
#Também é possível realizar esta atividade sem as variáveis

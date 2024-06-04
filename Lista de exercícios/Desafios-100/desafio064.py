'''
Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag). - Desafio 064
'''
n = count = soma = 0 #Variáveis número, contador de termos e soma
flag = 999 
while n != 999:
    n = int(input("Digite um número [\033[1;31m999\033[m para finalizar a contagem]: "))
    if n == flag:
        break #Finaliza a estrutura, assim desconsiderando flag na soma dos termos
    soma += n
    count += 1
print(f"Você digitou {count} termos e a \033[32msoma\033[m entre eles é igual a {soma}")
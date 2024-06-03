# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. - Desafio052
n = int(input("Digite um número: "))
t = 0 #Contador - Quantas vezes o número foi divisíel (de 1 até n)
for p in range(1, n+1): 
    if n % p == 0: #Condição para um número ser primo
        print('\033[33m',end=' ') 
        t += 1 #Contador - Quantas vezes o número foi divisíel (de 1 até n) 
    else:
        print('\033[31m', end=' ')
    print(f"{p}", end=' ') #Repetição de p  

print(f"\n\033[mO número {n} foi divisível {t} vezes")
if t == 2:
    print(f"Portanto, {n} é \033[33mPRIMO!\033[m")
else:
    print(f"Portanto, {n} \033[1;31mNÃO É PRIMO\033[m")
'''
Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
from time import sleep 
n = 0
conf = 'S'
count = maior = menor = somamed = media = 0 #Variáveis: contador de termos, maior e menor número, soma dos números para média e média
while conf == 'S':
    n = int(input("\nDigite um número: "))
    count += 1 
    conf = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]
    somamed += n
    media = somamed / count 

    #Maior e menor valores
    if count == 1:
        maior = menor = n
    else:
        if n > maior: 
            maior = n
        if n < menor:
            menor = n   
print("\n\033[1;36mPROCESSANDO...\033[m")
sleep(2.5)
print(f'''\n- Você digitou {count} termo(s) e a \033[1;32mMÉDIA\033[m entre eles é {media :.2f}
- O \033[1;34mMAIOR\033[m valor digitado foi {maior} e o \033[1;33mMENOR\033[m foi {menor}''')

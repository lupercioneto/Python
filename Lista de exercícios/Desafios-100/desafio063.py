'''
Escreva um programa que leia um número N inteiro qualquer 
e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci - Desafio 062
'''

from time import sleep

print(f"""{'-' * 22} 
Sequência de Fibonacci 
{'-' * 22}""")
qtt = int(input("Quantos termos gostaria de ver? "))
print("\033[1;36mPROCESSANDO...\033[m")
sleep(3)

term1 = 0
term2 = 1
print(f"{term1} -> {term2}", end=' -> ')
ct = 3 #Contador de termos
while ct <= qtt:
    term3 = term1 + term2 
    print(f"{term3}", end=' -> ')

    #Os termos 1 e 2 recebem os valores de seus sucessores (Explicação ao final do programa)
    term1 = term2
    term2 = term3 
    ct += 1 
print("\033[1;33mFIM\033[m")


'''
Primeira instância:
0 - 1 - 1 - 2 - 3
t1 t2  t3

Segunda instância:
0 - 1 - 1 - 2 - 3  
    t1  t2  t3  

Terceira instância:
0 - 1 - 1 - 2 - 3
        t1  t2  t3

Quarta instância
... 1 - 1 - 2 - 3 - 5 ...
            t1  t2  t3 ...
'''
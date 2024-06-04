'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso. - Desafio 059
'''
from time import sleep 
from sys import exit

#Inserção de dados
n1 = float(input("Primeiro valor: "))
n2 = float(input("Segundo valor: "))
opc = 0
print('\n\033[1;33mPROCESSANDO...\033[m')
sleep(2)

#Repetição de opções
while opc != 5:  
    print("""\n[ 1 ] - Somar
[ 2 ] - Multiplicar
[ 3 ] - Maior número
[ 4 ] - Novos números
[ 5 ] - Sair do programa""")    
    opc = int(input('\n>> O que deseja fazer? <<: '))

    #Somar
    if opc == 1:
        soma = n1 + n2
        print(f"\nA soma entre {n1} e {n2} é {soma}")

    #Multiplicar
    elif opc == 2:
        mult = n1 * n2
        print(f"\nA multiplicação entre {n1} e {n2} é igual a {mult}")

    #Maior número
    elif opc == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f"\nEntre {n1} e {n2}, o maior é {maior}") 
            
    #Novos números
    elif opc == 4:
        print("\nInforme os novos números")
        n1 = float(input("Primeiro valor: "))
        n2 = float(input("Segundo valor: "))
    
    #Opção inválida
    elif opc < 1 or opc > 5:
        print("""Opção \033[31minválida\033[m\nPor favor, escolha uma opção válida (entre 1 e 5): """)
    print('=-=' * 10)
    sleep(1.5)


#Saída do programa
print("\n\033[33mFinalizando programa...\033[m")
sleep(2)
print("Programa finalizado.")

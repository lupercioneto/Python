'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente. - Desafio 079
'''

valores = []
cores = ('\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[m')

while True:
    num = int(input("Digite um número: "))

    #Estrutura de controle para analisar se um número está na lista 
    while True:   
        while num in valores:
            num = int(input("Número duplicado! Por favor, digite novamente: "))
        else: 
            break
    valores.append(num)
    
    #Confirmação para continuar ou não
    conf = str(input(f"Deseja continuar? [{cores[1]}S{cores[4]}/{cores[0]}N{cores[4]}]: ")).lower().strip()[0]
    while conf not in 'sn': 
        conf = str(input(f'Por favor, digite apenas {cores[1]}S{cores[4]} para "Sim" e {cores[0]}N{cores[4]} para "Não": ')).lower().strip()[0]

    if conf in 's':
        continue
    elif conf in 'n': 
        break
    
print(f"Você digitou os valores {sorted(valores)}")
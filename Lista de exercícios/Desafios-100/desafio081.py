'''
Crie um programa que vai ler vários números e colocar em uma lista.               
Depois disso, mostre:                                                                                                                                                                                                                                                                                      A) Quantos números foram digitados.                                                                                                                    B) A lista de valores, ordenada de forma decrescente.                                                                                          
A) Quantos números foram digitados;
B) A lista de valores, ordenada de forma decrescente;
C) Se o valor 5 foi digitado e está ou não na lista. - Desafio 081
'''
from time import sleep

numeros = list()
cores = ('\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[m')

while True: 
    num = int(input("\nDigite um número: "))
    if num not in numeros:
        numeros.append(num)
    else:
        print(f"Números repetidos {cores[0]}NÃO SERÃO CONTABILIZADOS{cores[4]} para a contagem!\n")
        sleep(2)

    #Condição de continuação (Sim ou Não)
    conf = str(input(f"Quer continuar? [{cores[0]}S{cores[4]}/{cores[1]}N{cores[4]}]: ")).lower().strip()[0]
    while conf not in 'sn':
        conf = str(input(f'Por favor, digite {cores[0]}S{cores[4]} para "Sim" e {cores[1]}N{cores[4]} para "Não": ')).lower().strip()[0]
    
    #Retorna para o começo do loop caso o usuário deseje continuar
    if conf in 's':
        continue

    #Finaliza o loop
    else: 
        break
print(f"\n{cores[2]}ORGANIZANDO...{cores[4]}\n")
numerosreverse = sorted(numeros,reverse=True)
sleep(2.5)

print(f"""{'=' * 60}
- Quantidade de números digitados: {len(numeros)}     
- Os valores digitados em {cores[2]}ORDEM DECRESCENTE{cores[4]} são: {numerosreverse}""")

if 5 not in numeros: 
    print(f"- O valor 5 (cinco) {cores[0]}NÃO{cores[4]} está presente na lista!")
else:
    print(f"- O valor 5 está presente na lista, no índice {numerosreverse.index(5)}")
print(f"{'=' * 65}\n")
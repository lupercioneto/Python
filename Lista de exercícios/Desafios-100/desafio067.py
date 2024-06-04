'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo. - Desafio 067
'''
from time import sleep

tab = 1 
result = 0
print(f"""{'=' * 10}
{'TABUADA' :^10} 
{'=' * 10}""")

#Tabuada com estrutura de repetição aninhada (While > for)
while True: 
    n = int(input("Digite um número para ver sua tabuada.\nPara sair, digite um número \033[1;30mNEGATIVO\033[m: "))

    #Finalizando o programa com valor negativo
    if n < 0:
        break
    elif n == 0:
        print("\nA tabuada de zero é \033[1;30mNULA\033[m para todo e qualquer valor.\n")
        sleep(1.5)
        continue
    #Tabuada com for
    print('=-=' * 5)
    for i in range(1,11):
        tab = n * i
        result = tab 
        print(f"{n} x {i :^2} = {result}")
        sleep(0.3)
    print("=-=" * 5)
    sleep(1)
print("\n\033[1;33mFINALIZANDO...\033[m\n")
sleep(2)
print("PROGRAMA TABUADA \033[1;31mENCERRADO\033[m!")
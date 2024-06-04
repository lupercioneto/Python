'''
Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. - Desafio 068
'''

from time import sleep
from random import randint

print(f"""{'=' * 12}
PAR OU ÍMPAR
{'=' * 12}""")

qtwin = 0

#Escolhendo os números e o time (Par ou Ímpar)
print('=-' * 15)
nj = int(input("Vamos jogar Par ou Ímpar!\nIrei sortear um valor na minha memória e vamos jogar!\nDiga seu valor: "))
while nj > 10 or nj < 0:
    nj = int(input("Por favor, digite um valor \033[31mválido\033[m: "))

pi = str(input("\033[34mPar\033[m ou \033[31mÍmpar\033[m? [P/I]: ")).upper().strip()[0]
while pi not in 'PI':
    pi = str(input("Por favor, selecione apenas \033[34mPar\033[m ou \033[31mÍmpar\033[m, com estas letras --> [P/I]: ")).upper().strip()[0] 

#Contagem para a jogada
print("\nUm...")
sleep(0.7)
print("Dois...")
sleep(0.7) 
print("Já!")

#Jogando o jogo até o jogador perder
while True:
    nc = randint(0,10)
    soma = nc + nj 
    
    #Condição de vitória para o jogador 
    if (pi in 'Pp' and soma % 2 == 0) or (pi in 'Ii' and soma % 2 != 0):
        qtwin += 1
        print(f"""\n{'-' * 40} 
Você jogou {nj} e o computador jogou {nc} - O resultado foi {soma}
{'-' * 40}\n
Você \033[1;32mVENCEU\033[m!
Droga! Mais uma vez!""")
        
        nj = int(input("Diga um valor: "))
        pi = str(input("\033[34mPar\033[m ou \033[31mÍmpar\033[m? [P/I]: ")).upper().strip()
        continue

    #Condição de derrota para o jogador
    else:
        print(f"""\n{'-' * 20} 
Você jogou {nj} e o computador jogou {nc} - O resultado foi {soma}
{'-' * 20}\n 
Você \033[1;31mPERDEU\033[m!""")
        break

#Saída após o break (caso não haja nenhuma vitória)
if qtwin == 0:
    print("Que pena, você não ganhou nenhuma vez consecutivamente :(")
    exit()
else:
    #Saída após o break (caso haja pelo menos uma vitória)
    print(f"""\n\033[1;31mGAME OVER\033[m\nVocê venceu {qtwin} vez(es)""")
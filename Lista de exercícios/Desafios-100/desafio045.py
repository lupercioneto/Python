# Crie um programa que faça o computador jogar Jokenpô com você. - Desafio 045
from time import sleep
from random import randint

na = randint(1,3)
print("""Vamos jogar Pedra, papel ou tesoura!
[ 1 ] - Pedra
[ 2 ] - Papel
[ 3 ] - Tesoura""")
e = int(input("Esolha sua opção: "))
while e <= 0 or e >= 4: 
    print("Escolha \033[31minválida!\033[m Tente novamente: ")

print("\nJO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO!!!\n")

#Condições 
#Empate
if e == na:
    print("=-=" * 10)
    if e == 1 and na == 1:
        print("Computador jogou Pedra\nJogador jogou Pedra")
    elif e == 2 and na == 2:
        print("Computador jogou Papel\nJogador jogou Papel")
    elif e == 3 and na == 3:
        print("Computador jogou Tesoura\nJogador jogou Tesoura")
    print("=-=" * 10)
    print("\033[1;33mEMPATE!\033[m\n")

#Vitória do Computador
elif e == 3 and na == 1:
    print(f"""{'=-=' * 10}
Computador jogou Pedra\nJogador jogou \033[31mTesoura\033[m
{'=-=' * 10}
Computador \033[1;32mVENCEU\033[m\n""")
   
elif e == 2 and na == 3:
    print(f"""{'=-=' * 10}
Computador jogou \033[31mTesoura\033[m\nJogador jogou Papel
{'=-=' * 10}
Computador \033[1;32mVENCEU\033[m\n""")

elif e == 1 and na == 2:
    print(f"""{'=-=' * 10}
Computador jogou \033[34mPapel\033[m\nJogador jogou Pedra
{'=-=' * 10}
Computador \033[1;32mVENCEU\033[m\n""")
    
#Vitória do Jogador 
elif e == 1 and na == 3:
    print(f"""{'=-=' * 10}
Computador jogou \033[31mTesoura\033[m\nJogador jogou Pedra
{'=-=' * 10}
Jogador \033[1;32mVENCEU\033[m\n""")
    
elif e == 2 and na == 1:
    print(f"""{'=-=' * 10}
Computador jogou Pedra\nJogador jogou \033[34mPapel\033[m
{'=-=' * 10}
Jogador \033[1;32mVENCEU\033[m\n""")

elif e == 3 and na == 2:
    print(f"""{'=-=' * 10}
Computador jogou \033[34mPapel\033[m\nJogador jogou \033[31mTesoura\033[m
{'=-=' * 10}
Jogador \033[1;32mVENCEU\033[m\n""")
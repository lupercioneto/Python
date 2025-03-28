from Mapa import Mapa
from Player import Player
import os
from time import sleep

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def Exibir_Menu():
    print(" > Bem-vindo ao Wumpus' World!")
    # sleep(1.5)

    print("\n\U0001F6A9 Regras:")
    print("- Você está em uma caverna com Wumpus e alguns buracos;")
    print("- Encontre o ouro \U0001F4B0 e saia da caverna por onde entrou;")
    print("- Não caia em buracos \U0001F573  e não seja devorado pelo Wumpus! \U0001F47E")
    print("""\n- Comandos:\n 
\U00002B06  W (cima) 
\U00002B05  A (esquerda) 
\U00002B07  S (baixo) 
\U000027A1  D (direita) 
\U0001F3F9 F (Atirar com Arco)\n""")
    
    # sleep(5)

    print("Dificuldades:")
    print("1. Easy \U0001F37C (Mapa 4x4)")
    print("2. Normal \U00002696 (Mapa 6x6)")
    print("3. Extreme \U00002694 (Mapa 10x10)\n")


def Select_Mode():
    while True:
        escolha = input("Escolha a dificuldade (1 para Easy, 2 para Normal, 3 para Extreme): ").strip()
        if escolha == "1":
            return (4, 2)  # Mapa 4x4 e 2 buracos
        elif escolha == "2":
            return (6, 9)  # Mapa 6x6 e 9 buracos
        elif escolha == "3":
            return (10, 15)  # Mapa 10x10 e 15 buracos
        else:
            print("Opção inválida! Tente novamente.")


def Start_Game():
    clear_terminal()
    Exibir_Menu()

    # Seleção de dificuldade
    tamanho, pits = Select_Mode()

    # Criação do mapa e Player
    mapa = Mapa(tamanho, pits)
    player = Player(mapa)

    clear_terminal()

    print("Boa sorte! O jogo começará em", end="", flush=True)
    for i in range(3, 0, -1):
        print(f" {i}", end="", flush=True)
        sleep(1)

    clear_terminal()

    while player.vivo:
        mapa.Show_Map()
        player.Show_Pos()

        if player.ouro_coletado and (player.x, player.y) == (0, 0):
            clear_terminal()
            mapa.Show_Map()
            print("\U0001F389 Você pegou o ouro e saiu da caverna! Vitória! \u2713")
            break

        movimento = input("> Digite um comando (W | A | S | D | F): ").upper()
        if movimento in ["W", "A", "S", "D"]:
            clear_terminal()
            player.Move(movimento)

        elif movimento in ["F"]:
            direction = input("\U0001F3F9 Para qual direção deseja atirar (W | A | S | D)? -> ").upper()

            while direction not in ["W", "A", "S", "D"]:
                print("Direção inválida!")
                sleep(1)
                clear_terminal()
                direction = input("\U0001F3F9 Para qual direção deseja atirar (W | A | S | D)? -> ").upper()
            
            clear_terminal()
            player.attack_with_bow(direction) 
        
        else:
            print("Comando inválido!")
            sleep(1)
            clear_terminal()
    
    print("\n\U0001F38A Fim do jogo!")



Start_Game()
from Mapa import Mapa
from Player import Player
import os
from time import sleep
import random as ram

players = []
easy_rank = {}
normal_rank = {}
xtreme_rank = {}

# Deixa o terminal menos poluído
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_a_sec(secs=1, hide=True):
    if hide:
        for i in range(secs, 0, -1):
            sleep(1)
    else:
        for i in range(secs, 0, -1):
            print(f" {i}", end="", flush=True)
            sleep(1)

# Auto-Explicativa :p
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

# Pega a escolha de dificuldade do player
def Select_Mode():
    while True:
        escolha = input("Escolha a dificuldade (1 para Easy, 2 para Normal, 3 para Extreme): ").strip()
        if escolha == "1":
            return (6, 4)  # Mapa 4x4 e 4 buracos
        elif escolha == "2":
            return (8, 12)  # Mapa 6x6 e 12 buracos
        elif escolha == "3":
            return (10, 20)  # Mapa 10x10 e 20 buracos
        else:
            print("Opção inválida! Tente novamente.")

# Auto-Explicativa :p
def insert_nickname():
    nick = input("Qual seu apelido (nickname)? -> ")
    return nick


def view_ranking():
    list_of_ranks = []

    # Garantindo que só será mostrado ranks em que alguém já tenha jogado antes
    try:
        if easy_rank:
            list_of_ranks.append(sorted(([name_key, score_value] for name_key, score_value in easy_rank.items()), key=lambda x: x[1], reverse=True))
        if normal_rank:
            list_of_ranks.append(sorted(([name_key, score_value] for name_key, score_value in normal_rank.items()), key=lambda x: x[1], reverse=True)) 
        if xtreme_rank:
            list_of_ranks.append(sorted(([name_key, score_value] for name_key, score_value in xtreme_rank.items()), key=lambda x: x[1], reverse=True))
    except NameError():
        print("Erro! Nenhum ranking de jogadores foi definido!")
    
    dificulties = ['Easy', 'Normal', 'Extreme']

    print("\nRanking dos melhores jogadores (Por dificuldade):")
    wait_a_sec()

    for i, rank_list in enumerate(list_of_ranks):
        mode = dificulties[i]
        sleep(1)

        print(f"\nRANKING - {mode.upper()} MODE")

        for pos, (player_nick, player_score) in enumerate(rank_list, start=1):
            medal = "\U0001F947" if pos == 1 else "\U0001F948" if pos == 2 else "\U0001F949" if pos == 3 else "" # Mealhas de Ouro, Prata e Bronze
            print(f"{medal} {pos}° Lugar: {player_nick} - {player_score} pontos")



def putting_players_at_rank(player: Player):
    player_name = player.nickname

    # Colocando os jogadores em suas respectivas escolhas de dificuldade
    if player_name not in easy_rank:
        easy_rank[player_name] = 0

    elif player_name not in normal_rank:
        normal_rank[player_name] = 0

    else:
        xtreme_rank[player_name] = 0 


def catalog_player_score(player: Player, score: int):
    player_nick = player.nickname

    if player_nick in easy_rank: 
        easy_rank[player_nick] += score

    elif player_nick in normal_rank:
        normal_rank[player_nick] += score
    
    else:
        xtreme_rank[player_nick] += score


# Auto-Explicativa :p
def Start_Game():
    clear_terminal()
    Exibir_Menu()

    # Seleção de dificuldade
    tamanho, pits = Select_Mode()
    
    # Criação do mapa e Player
    mapa = Mapa(tamanho, pits)
    nickname = insert_nickname()
    player = Player(mapa, nickname)

    putting_players_at_rank(player) # Armazenando os jogadores para organizar os ranks

    clear_terminal()

    # Jogo iniciando
    print("Boa sorte! O jogo começará em", end="", flush=True)
    wait_a_sec(3, False)

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
                wait_a_sec()
                clear_terminal()
                direction = input("\U0001F3F9 Para qual direção deseja atirar (W | A | S | D)? -> ").upper()
            
            clear_terminal()
            player.attack_with_bow(direction) 
        
        else:
            print("Comando inválido!")
            wait_a_sec()
            clear_terminal()
    
    print("\n\U0001F38A Fim do jogo!")
    wait_a_sec()
    print(f"Pontuação: {player.player_score} pontos")
    catalog_player_score(player, player.player_score)
    wait_a_sec(2)

    # Visualização do Ranking
    view_score = input("Deseja visualizar a sua classificação e a dos outros jogadores? (S/N) -> ").strip().upper()[0]
    while view_score not in ['S', 'N']:
        view_score = input("Comando inválido! Insira S para SIM e N para NÃO: ").strip().upper()[0]
    
    if view_score == "S":
        view_ranking()
        wait_a_sec()
    
    play_again = input("\nDeseja jogar novamente? (S/N) -> ").strip().upper()[0]
    while play_again not in ['S', 'N']:
        play_again = input("Comando inválido! Digite S para SIM e N para NÃO: ")
    
    if play_again == 'S':        
        msgs = ["\nDica: Já tentou visitar a cova de Wumpus? \U000026B0", "\n\U0001F9E0 Wumpus pode ser mais inteligente do que você pensa...",
                "\nSe você já teve sorte no azar, entenderá esta frase; Não é, Wumpus- BLAARGH! \U0001F47E", 
                "\nO Wumpus é enorme! Atente-se a esse detalhe \U0001F50D."]
        
         
        clear_terminal()
        fun_value = len(msgs)
        print("Reiniciando o jogo...") 
        count = 0
        
        while count < 4: 
            random_index = ram.randint(0, fun_value - 1) 
            wait_a_sec(2)
            current_msg = msgs[random_index] # Escolhendo uma mensagem aleatória das existentes
            print(current_msg)
            count += 1
    
        clear_terminal()
        Start_Game()
    
    else: 
        print("Encerrando...")
        wait_a_sec(3)

Start_Game()
import random as ram
import os
from time import sleep

class Player():


    def __init__(self, mapa, player_nick):
        self.player_score = 0 # É atualizado conforme as ações que faz no mapa (andar, pegar gold, morrer)
        self.nickname = player_nick
        self.mapa = mapa
        self.x, self.y = 0, 0  # Começa no canto superior esquerdo
        self.vivo = True
        self.ouro_coletado = False
        self.mapa.visible_map[self.x][self.y] = "\U0001F93A"  # Marca a posição inicial do player
        self.__wumpus_position = self.mapa._map["W"]
    

    # Move o player para uma das 4 direções
    def Move(self, direcao):
        """ Move o personagem no mapa e verifica interações com outros elementos"""
        if not self.vivo:
            print("Você já morreu! Não pode se mover.")
            return

        old_x, old_y = self.x, self.y
        self.player_score -= 7 # Cada passo diminue pontuação. Quanto mais andar, mais penalizado player será

        if direcao == "W" and self.x > 0:  # Andar para cima
            self.x -= 1
            
        elif direcao == "S" and self.x < self.mapa.tamanho - 1:  # Andar para baixo
            self.x += 1

        elif direcao == "A" and self.y > 0:  # Andar para a esquerda
            self.y -= 1 

        elif direcao == "D" and self.y < self.mapa.tamanho - 1:  # Andar para a direita
            self.y += 1
        else:
            print("Movimento inválido!")
            return
        
        # Atualiza a posição no mapa visível
        self.mapa.visible_map[old_x][old_y] = "\U00002753"  # Marca onde já passou
        self.mapa.visible_map[self.x][self.y] = "\U0001F93A" # Posição da nova casa
        
        if self.wumpus_is_dead():
            x, y = self.mapa._map["W"]
            self.mapa.visible_map[x][y] = "\U0001F940"

        self.Verify_Pos()

    # Ataca uma linha/coluna
    def attack_with_bow(self, direction):
        # Inicia o processo de ataque com arco e flecha contra o Wumpus
        if self.wumpus_is_dead():
            print("\U0001F9E0 Você repensa e decide não gastar uma de suas preciosas flechas.")

        elif self.Try_Attack_Wumpus(direction):
            print("\U0001FA78 Você acertou um tiro fatal em Wumpus! Agora ele está morto.\n")
            self.player_score += 900

        else:
            self.move_wumpus_randomly()
            print("Você ouviu a flechar atingir uma parede. \nO Wumpus percebe sua intenção e se move \U0001F47E.\n")
            print("- 200 pontos")
            self.player_score -= 200

    # Verifica se determinada coordenada contém um wumpus e mata ele
    def Wumpus_pierced_by_arrow(self, target_x, target_y):
        pierced = False

        if (target_x, target_y) == self.mapa._map["W"]:
            # Ataque foi bem-sucedido
            pierced = True
            
            # Remove o Wumpus do mapa e sua casa fica como Túmulo
            self.__wumpus_position = "Tomb"
            self.mapa.visible_map[target_x][target_y] = "\U0001F940" # Mostra o wumpus morto ao jogador
            
        return pierced  # Se não acertar o Wumpus, ele se move para uma casa aleatória do mapa (Vá para Was_Wumpus_Fainted)
       

    # Verifica se o wumpus está morto
    def wumpus_is_dead(self):
        return self.__wumpus_position == "Tomb"   


    # Percorre a linha/coluna vendo se o wumpus esta lá
    def Try_Attack_Wumpus(self, typeDir):
        """
        Ataca o Wumpus com um arco e flecha, verificando se ele está na linha ou coluna
        na direção especificada.
        """
         
        target_x = self.x 
        target_y = self.y
        was_fainted = False

        if typeDir == "W":
            for straight_coord in range(self.x - 1, -1, -1): # Percorre toda a coluna acima
                target_x, target_y = straight_coord, self.y  
                
                # Verifica se wumpus foi acertado e está morto (o mesmo para as outras direções)
                was_fainted = self.Wumpus_pierced_by_arrow(target_x, target_y)
                if was_fainted and self.wumpus_is_dead():
                    return was_fainted

        elif typeDir == "S":
            for straight_coord in range(self.x + 1, self.mapa.tamanho): # Percorre toda a coluna abaixo
                target_x, target_y = straight_coord, self.y  

                was_fainted = self.Wumpus_pierced_by_arrow(target_x, target_y)
                if was_fainted and self.wumpus_is_dead():
                    return was_fainted

        elif typeDir == "A":
            for straight_coord in range(self.y - 1, -1, -1): # Percorre toda a linha a esquerda
                target_x, target_y = self.x, straight_coord    
                
                was_fainted = self.Wumpus_pierced_by_arrow(target_x, target_y)
                if was_fainted and self.wumpus_is_dead():
                    return was_fainted
                
        elif typeDir == "D":     
            for straight_coord in range(self.y + 1, self.mapa.tamanho): # Percorre toda a linha a direita
                target_x, target_y = self.x, straight_coord 
                
                was_fainted = self.Wumpus_pierced_by_arrow(target_x, target_y) 
                if was_fainted and self.wumpus_is_dead():
                    return was_fainted
                
        if str(was_fainted) == "False":
            return was_fainted
        

    # Altera a posição do wumpus 
    def move_wumpus_randomly(self):
        """Move o Wumpus para uma posição aleatória no mapa"""
        if self.wumpus_is_dead():
            return
        
        max_trys = 100
        trys = 0
        
        while trys < max_trys:
            new_x, new_y = ram.randint(0, self.mapa.tamanho - 1), ram.randint(0, self.mapa.tamanho - 1)
            
            # Garante que o Wumpus não se mova para a posição do jogador, do ouro ou de buracos
            if (new_x, new_y) != (self.x, self.y) and (new_x, new_y) != self.mapa._map["G"] and (new_x, new_y) not in self.mapa._map["B"]:
                self.mapa._map["W"] = (new_x, new_y)
                self.__wumpus_position = (new_x, new_y) 
                self.Verify_Perceptions() # Caso Wumpus spawne em adjacentes, o player seja avisado
                break
            trys += 1
        
        if max_trys == trys: 
            print("Que sorte \U0001F340! Wumpus não ouviu sua flecha! Ele ainda está no mesmo lugar de antes!\n")
            return


    # Verifica o que há na nova posição do player
    def Verify_Pos(self):
        """Verifica a posição que Player acabou de pisar
        -> Se houver um Wumpus ou um Pit, ele perde;
        -> Se houver um Gold, ele o coletará em segurança"""

        if (self.x, self.y) == self.mapa._map["G"]:
            self.ouro_coletado = True
            print("\U0001F389 Você encontrou o ouro! Agora saia da caverna.")
            print("+1000 pontos \U00002728")
            self.player_score += 1000
            self.mapa._map["G"] = None # Retira o ouro daquela posição, pois já foi coletado   

        elif (self.x, self.y) == self.mapa._map["W"]:
            
            # O Wumpus morreu e o player está na posição onde ele morreu
            if self.wumpus_is_dead():
                print("Aqui jaz Wumpus... \U000026B0\nVocê olha para seu cadáver, mas decide deixar quieto.")

            # Wumpus está vivo e o player pisou na casa onde ele está
            else:
                self.vivo = False  
                self.mapa.visible_map[self.x][self.y] = "\U0001F480"
                
                self.mapa.Show_Map() 
                print("\U0001F480 Você foi devorado pelo Wumpus!")
                print("- 700 pontos \U0000274C")
                self.player_score -= 700
                return 

        elif (self.x, self.y) in self.mapa._map["B"]:
            self.vivo = False
            self.mapa.visible_map[self.x][self.y] = "\U0001F573" # Mostar em que buraco você caiu

            self.mapa.Show_Map()
            print("Você caiu em um buraco! \U0001F573")
            print("- 300 pontos")
            self.player_score -= 300
            return
        
        self.Verify_Perceptions()


    # Verifica se as adjacentes tem alguma percepção (brisa, wumpus)
    def Verify_Perceptions(self):
        """Verifica o que há por perto, em casas adjacentes ao Player"""
    
        perigo = []
        for adj_x, adj_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # direções adjacentes a casa atual do player
            nx, ny = self.x + adj_x, self.y + adj_y
            if not self.wumpus_is_dead() and (nx, ny) == self.mapa._map["W"]: 
                perigo.append("\U0001F443 Você sente um fedor terrível!")
            if (nx, ny) in self.mapa._map["B"]:
                perigo.append("\U0001F4A8 Você sente uma brisa estranha...")

        for msg in perigo:
            print(msg)
        sleep(0.1)


    # Mostra a posição atual do player
    def Show_Pos(self):
        print(f"\U0001F4CD Posição atual: ({self.x}, {self.y})")

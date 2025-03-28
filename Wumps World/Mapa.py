import random as ram

class Mapa():
    
    PLAYER_START_POS = (0, 0) # Posição Global Inicial do Player
    
    def __init__(self, tamanho, pits):
        self.tamanho = tamanho
        self._map = {}
        self.visible_map = [["\U00002753" for _ in range(tamanho)] for _ in range(tamanho)] # Gera o mapa visível para o usuário

        # Gera os elementos do mapa
        while True:       
            self._map["W"] = self.Generate_Wumpus()
            self._map["B"] = self.Generate_Pits(pits, self._map["W"])
            self._map["G"] = self.Generate_Gold(self._map["B"], self._map["W"])

            if not (self.Is_Wumpus_Locked(self._map["W"], self.tamanho, self._map["B"])):
                break


    # Gera uma coordenada aleatória do tamanho do mapa
    def Random_Safety_Coord(self, typeE):
        """Gera uma coordenada (X, Y) aleatória do tamanho do mapa definido """

        if typeE == "W":
            x, y = ram.randint(2, self.tamanho - 1), ram.randint(2, self.tamanho - 1)
            return x, y
            
        elif typeE == "B":
            x, y = ram.randint(1, self.tamanho - 1), ram.randint(2, self.tamanho - 1)
            return x, y 

        elif typeE == "G":
            x, y = ram.randint(2, self.tamanho - 1), ram.randint(2, self.tamanho - 1)
            return x, y
            


    def Is_Adjacent_To_Player(self, x, y):
        """Verifica se a posição (x, y) está ao lado da posição inicial do jogador"""

        player_x, player_y = self.PLAYER_START_POS
        
        # direções adjacentes (em relação à posição do jogador)
        adjacente_direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for adj_x, adj_y in adjacente_direcoes:
            if (x, y) == (player_x + adj_x, player_y + adj_y):
                return True
        return False


    def Generate_Gold(self, pits_positions, wumpus_pos):
        """Gera 1 (um) Gold (Ouro) em uma posição aleatória do mapa;"""

        while True:
           x, y = self.Random_Safety_Coord("G")
           if (x, y) != self.PLAYER_START_POS and (x, y) not in pits_positions and (x, y) != wumpus_pos:    
                return x, y


    def Generate_Pits(self, pits: int, wumpus_pos):
        """Gera Pits (Buracos) em posições aleatórias do mapa.
        Também realiza verificações a fim de evitar sobreposições de elementos"""

        pit_positions = set()
        while len(pit_positions) < pits:
            x, y = self.Random_Safety_Coord("B")

            if (x, y) not in pit_positions and (x , y) != self.PLAYER_START_POS and (x, y) != wumpus_pos:
                if not self.Is_Adjacent_To_Player(x, y):
                    pit_positions.add((x, y))
        
        return list(pit_positions)


    def Is_Wumpus_Locked(self, wumpus_pos, tamanho: int, pits):
        """Verifica se o Wumpus tem algum espaço livre para fugir
        (Se não está cercado de buracos)"""

        x, y = wumpus_pos
        free_spaces = 0 

        for adj_x, adj_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + adj_x, y + adj_y
            if 0 <= new_x < self.tamanho and 0 <= new_y < self.tamanho:
                if (new_x, new_y) not in self._map["B"]:  # Se não for um buraco
                    free_spaces += 1
        return free_spaces == 0  # Está preso se não houver espaços livres


    def Generate_Wumpus(self, min_distance=2):
        """Gera um Wumpus em uma posição aleatória do mapa;
        Também realiza verificações a fim de evitar sobreposições de elementos"""
        

        if self.tamanho <= 4:
            min_distance = 1 

        while True:
            x, y = self.Random_Safety_Coord("W") # Coordenada para o Wumpus
            
            player_x, player_y = self.PLAYER_START_POS
            distancia_player = abs(x - player_x) + abs(y - player_y) # Distancia de Manhattan (Não-Euclidiana)

            if distancia_player >= min_distance:
                if (x, y) != self.PLAYER_START_POS and not self.Is_Adjacent_To_Player(x, y):
                    return (x, y)
        


    def Show_Map(self):
        """ Mostra o mapa visível para o jogador"""
        print()
        for linha in self.visible_map:
            print(" ".join(linha))
        print()
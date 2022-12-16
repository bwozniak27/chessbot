import pygame

class piece():
    def __init__(self, type, color, pos):
        self.type = type
        self.color = color
        self.pos = pos
        
        #fetch the image
        self.icon = pygame.image.load("piece_icons/" + self.type + "_" + self.color + ".svg").convert_alpha()
        self.icon = pygame.transform.scale(self.icon, (80, 80))
    
    def valid_move(self, new_pos, game_state):
        #check if the move is valid
        if self.type == "pawn":
            return self.valid_pawn_move(new_pos, game_state)
        if self.type == "rook":
            return self.valid_rook_move(new_pos, game_state)
        if self.type == "knight":
            return self.valid_knight_move(new_pos, game_state)
        if self.type == "bishop":
            return self.valid_bishop_move(new_pos, game_state)
        if self.type == "queen":
            return self.valid_queen_move(new_pos, game_state)
        if self.type == "king":
            return self.valid_king_move(new_pos, game_state)
        else:
            return False
    
    def valid_pawn_move(self, new_pos, game_state):
        #check if the move is valid
        translation = (new_pos[0] - self.pos[0], new_pos[1] - self.pos[1])
        negator = -1 if self.color == "white" else 1
        starting_rank = 6 if self.color == "white" else 1
        valid = False
        # starting rank, move 2
        if translation == (negator * 2, 0) and self.pos[0] == starting_rank and game_state[new_pos[0]][new_pos[1]] is None:
            valid = True
        # move 1
        elif translation == (negator, 0) and game_state[new_pos[0]][new_pos[1]] is None:
            valid = True
        # capture
        elif (translation == (negator, 1) or translation == (negator, -1)) and game_state[new_pos[0]][new_pos[1]] is not None:
            if game_state[new_pos[0]][new_pos[1]].color != self.color:
                valid = True
        if valid:
            self.pos = new_pos
        return valid
    
    def valid_rook_move(self, new_pos, game_state):
        translation = (new_pos[0] - self.pos[0], new_pos[1] - self.pos[1])
        direction = 1 if translation[0] > 0 or translation[1] > 0 else -1
        if translation[0] != 0 and translation[1] != 0:
            return False
        elif translation[0] == 0:
            for i in range(direction, translation[1], direction):
                if game_state[self.pos[0]][self.pos[1] + i] is not None:
                    return False
        elif translation[1] == 0:
            for i in range(direction, translation[0], direction):
                if game_state[self.pos[0] + i][self.pos[1]] is not None:
                    return False
        if game_state[new_pos[0]][new_pos[1]] is not None:
            if game_state[new_pos[0]][new_pos[1]].color == self.color:
                return False
        self.pos = new_pos
        return True
    
    def valid_knight_move(self, new_pos, game_state):
        translation = (new_pos[0] - self.pos[0], new_pos[1] - self.pos[1])
        if (abs(translation[0]) == 2 and abs(translation[1]) == 1) or (abs(translation[0]) == 1 and abs(translation[1]) == 2):
            if game_state[new_pos[0]][new_pos[1]] is not None:
                if game_state[new_pos[0]][new_pos[1]].color == self.color:
                    return False
            self.pos = new_pos
            return True
        return False
    
    def valid_bishop_move(self, new_pos, game_state):
        translation = (new_pos[0] - self.pos[0], new_pos[1] - self.pos[1])
        if abs(translation[0]) != abs(translation[1]):
            return False
        direction = 1 if translation[0] > 0 or translation[1] > 0 else -1
        for i in range(direction, translation[0], direction):
            if game_state[self.pos[0] + i][self.pos[1] + i] is not None:
                return False
        if game_state[new_pos[0]][new_pos[1]] is not None:
            if game_state[new_pos[0]][new_pos[1]].color == self.color:
                return False
        self.pos = new_pos
        return True
    
    def valid_queen_move(self, new_pos, game_state):
        translation = (new_pos[0] - self.pos[0], new_pos[1] - self.pos[1])
        if abs(translation[0]) != abs(translation[1]) and translation[0] != 0 and translation[1] != 0:
            return False
        direction = 1 if translation[0] > 0 or translation[1] > 0 else -1
        if translation[0] == 0:
            for i in range(direction, translation[1], direction):
                if game_state[self.pos[0]][self.pos[1] + i] is not None:
                    return False
        elif translation[1] == 0:
            for i in range(direction, translation[0], direction):
                if game_state[self.pos[0] + i][self.pos[1]] is not None:
                    return False
        else:
            for i in range(direction, translation[0], direction):
                if game_state[self.pos[0] + i][self.pos[1] + i] is not None:
                    return False
        if game_state[new_pos[0]][new_pos[1]] is not None:
            if game_state[new_pos[0]][new_pos[1]].color == self.color:
                return False
        self.pos = new_pos
        return True
    
    def valid_king_move(self, new_pos, game_state):
        translation = (new_pos[0] - self.pos[0], new_pos[1] - self.pos[1])
        if abs(translation[0]) > 1 or abs(translation[1]) > 1:
            return False
        if game_state[new_pos[0]][new_pos[1]] is not None:
            if game_state[new_pos[0]][new_pos[1]].color == self.color:
                return False
        self.pos = new_pos
        return True

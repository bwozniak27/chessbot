import abc

class Player(abc.ABC):
    def __init__(self, color):
        self.color = color
    
    @abc.abstractmethod
    def make_move(self, game_state):
        pass

class HumanPlayer(Player):
    
    def make_move(self, game_state):
        pass
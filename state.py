from piece import piece


class GameState:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turn = "white"
        self.game_over = False
        self.board = [
            [piece("rook", "black", (0, 0)), piece("knight", "black", (0, 1)), piece("bishop", "black", (0, 2)), piece("queen", "black", (0, 3)), piece("king", "black", (0, 4)), piece("bishop", "black", (0, 5)), piece("knight", "black", (0, 6)), piece("rook", "black", (0, 7))],
            [piece("pawn", "black", (1, 0)), piece("pawn", "black", (1, 1)), piece("pawn", "black", (1, 2)), piece("pawn", "black", (1, 3)), piece("pawn", "black", (1, 4)), piece("pawn", "black", (1, 5)), piece("pawn", "black", (1, 6)), piece("pawn", "black", (1, 7))],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [piece("pawn", "white", (6, 0)), piece("pawn", "white", (6, 1)), piece("pawn", "white", (6, 2)), piece("pawn", "white", (6, 3)), piece("pawn", "white", (6, 4)), piece("pawn", "white", (6, 5)), piece("pawn", "white", (6, 6)), piece("pawn", "white", (6, 7))],
            [piece("rook", "white", (7, 0)), piece("knight", "white", (7, 1)), piece("bishop", "white", (7, 2)), piece("queen", "white", (7, 3)), piece("king", "white", (7, 4)), piece("bishop", "white", (7, 5)), piece("knight", "white", (7, 6)), piece("rook", "white", (7, 7))],
        ]
    
    def update_game_state(self, selected_square, new_square):
        # Update the game state
        print("\nold square: ", selected_square)
        print("new square: ", new_square)

        if self.board[selected_square[0]][selected_square[1]] is not None:
            if self.board[selected_square[0]][selected_square[1]].valid_move(new_square, self.board):
                print("Valid move")
                self.board[new_square[0]][new_square[1]] = self.board[selected_square[0]][selected_square[1]]
                self.board[selected_square[0]][selected_square[1]] = None
                return True
        return False
    
    def get_move(self):
        pass


import pygame
import sys
import argparse
from piece import piece
from state import GameState



def main(player1, player2):
    # Initialize Pygame
    pygame.init()

    # Set the width and height of the screen [width, height]
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 800
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Title and Icon
    pygame.display.set_caption("Chess")

    # Loop until the user clicks the close button
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Set the width and height of the chess board
    BOARD_WIDTH = 640
    BOARD_HEIGHT = 640

    # create the board surface
    board = pygame.Surface((BOARD_HEIGHT, BOARD_WIDTH))

    light = (232, 235, 239)
    dark = (125, 135, 150)
    selected = (236, 227, 161)
    size = BOARD_HEIGHT // 8

    # Function to draw the chess board
    def draw_board(surface, selected_square):
        # Draw the chess board
        for row in range(8):
            for col in range(8):
                if col == selected_square[0] and row == selected_square[1]:
                    color = selected
                else:
                    color = light if (row + col) % 2 == 0 else dark
                rect = (row * size, col * size, size, size)
                pygame.draw.rect(surface, color, rect)

    # Function to draw the chess pieces
    def draw_pieces(surface, game_state):
        # Draw the chess pieces
        for row in range(8):
            for col in range(8):
                if game_state.board[row][col] is not None:
                    piece = game_state.board[row][col]
                    surface.blit(piece.icon, (col * size, row * size))

    # Function to determine the square that is selected
    def get_square(pos):
        x, y = pos
        row = (y - 100) // size
        col = (x - 100) // size
        return row, col



    def handle_square_click(game_state, selected_square, pos):
        new_selected_square = get_square(pos)
        # click is off the board
        if new_selected_square[0] < 0 or new_selected_square[0] > 7 or new_selected_square[1] < 0 or new_selected_square[1] > 7:
            return (-1, -1)
        # nothing is selected
        if selected_square == (-1, -1):
            # TODO: player can only move their own pieces
            if game_state.board[new_selected_square[0]][new_selected_square[1]] is not None:
                return new_selected_square
            else:
                return selected_square
        # something is selected and new selection is an occupied square
        if game_state.board[new_selected_square[0]][new_selected_square[1]] is not None:
            # if piece move
            if game_state.update_game_state(selected_square, new_selected_square):
                return (-1, -1)
            # if new square is occupied by same color piece
            if game_state.board[selected_square[0]][selected_square[1]].color == game_state.board[new_selected_square[0]][new_selected_square[1]].color:
                return new_selected_square
            else:
                return selected_square
        # else, something is selected and new selection is an empty square
        if game_state.update_game_state(selected_square, new_selected_square):
            return (-1, -1)
        return selected_square

    selected_square = (-1, -1)
    game_state = GameState(player1, player2)

    # Call the draw_board function to draw the chess board
    # -------- Main Program Loop -----------
    while not done:
        
        
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                selected_square = handle_square_click(game_state, selected_square, pos)

        # --- Game logic should go here

        # --- Drawing code should go here

        # Draw the chess board and pieces here
        draw_board(board, selected_square)
        
        draw_pieces(board, game_state)
        screen.blit(board, (100, 100))
        
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()


def create_players(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-w",
        "--white",
        choices=["human", "bot"],
        default="human",
        help="white player type"
    )
    parser.add_argument(
        "-b",
        "--black",
        choices=["human", "bot"],
        default="human",
        help="black player type"
    )
    args = parser.parse_args(argv)
    return args.white, args.black

if __name__ == "__main__":
    player1, player2 = create_players(sys.argv[1:])
    main(player1, player2)



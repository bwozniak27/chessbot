import pygame
from piece import piece

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
            if row == selected_square[0] and col == selected_square[1]:
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
            if game_state[col][row] is not None:
                piece = game_state[col][row]
                surface.blit(piece.icon, (row * size, col * size))

# Function to determine the square that is selected
def get_square(pos):
    x, y = pos
    row = (y - 100) // size
    col = (x - 100) // size
    return row, col


game_state = [
    [piece("rook", "black", (0, 0)), piece("knight", "black", (0, 1)), piece("bishop", "black", (0, 2)), piece("queen", "black", (0, 3)), piece("king", "black", (0, 4)), piece("bishop", "black", (0, 5)), piece("knight", "black", (0, 6)), piece("rook", "black", (0, 7))],
    [piece("pawn", "black", (1, 0)), piece("pawn", "black", (1, 1)), piece("pawn", "black", (1, 2)), piece("pawn", "black", (1, 3)), piece("pawn", "black", (1, 4)), piece("pawn", "black", (1, 5)), piece("pawn", "black", (1, 6)), piece("pawn", "black", (1, 7))],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [piece("pawn", "white", (6, 0)), piece("pawn", "white", (6, 1)), piece("pawn", "white", (6, 2)), piece("pawn", "white", (6, 3)), piece("pawn", "white", (6, 4)), piece("pawn", "white", (6, 5)), piece("pawn", "white", (6, 6)), piece("pawn", "white", (6, 7))],
    [piece("rook", "white", (7, 0)), piece("knight", "white", (7, 1)), piece("bishop", "white", (7, 2)), piece("queen", "white", (7, 3)), piece("king", "white", (7, 4)), piece("bishop", "white", (7, 5)), piece("knight", "white", (7, 6)), piece("rook", "white", (7, 7))],
]
selected_square = (-1, -1)
# Call the draw_board function to draw the chess board
# -------- Main Program Loop -----------
while not done:
    
    
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Left Click")
            pos = pygame.mouse.get_pos() 
            selected_square = get_square(pos)

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

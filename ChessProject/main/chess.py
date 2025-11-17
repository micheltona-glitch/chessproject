import chess
import pygame
import os

pygame.init()
WIDTH, HEIGHT = 480, 480  # 480 / 8 = 60 pixels per square
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Puzzle Game")

# --- Constants ---
SQUARE_SIZE = WIDTH // 8
COLORS = {
    "light": (238, 238, 210),
    "dark": (118, 150, 86)
}

PIECE_THEME = "pieces"
def draw_board(screen):
    for r in range(8):
        for c in range(8):
            if (r + c) % 2 == 0:
                color = COLORS["light"]
            else:
                color = COLORS["dark"]
            pygame.draw.rect(screen, color, pygame.Rect(c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
def load_piece_images():
    images = {}
    pieces = ['wR', 'wN', 'wB', 'wQ', 'wK', 'wP', 'bR', 'bN', 'bB', 'bQ', 'bK', 'bP']
    for piece in pieces:
        image_path = os.path.join(PIECE_THEME, f"{piece}.png")
        images[piece] = pygame.image.load(image_path)
    return images
def get_piece_symbol(piece):
    if piece is None:
        return None
    symbol = piece.symbol()
    if piece.color == chess.WHITE:
        return f'w' + symbol.upper()
    else:
        return f'b' + symbol.upper()

def draw_pieces(screen, board, images):
    for i in range(64):
        piece = board.piece_at(i)
        if piece is not None:
            piece_symbol = get_piece_symbol(piece)
            row = 7 - (i // 8)
            col = i % 8
            screen.blit(images[piece_symbol], pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def main():
    board = chess.Board()
    images = load_piece_images()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_board(SCREEN)
        draw_pieces(SCREEN, board, images)
        pygame.display.flip()

    pygame.quit(res)




fff



'''positions_lyst = [ ] 
def positions():
    for p in positions_lyst:
        fen = p

    board = chess.Board(fen) 

'''

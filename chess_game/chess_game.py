import chess
import pygame
import os

pygame.init()
WIDTH, HEIGHT = 480, 480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Puzzle Game")

SQUARE_SIZE = WIDTH // 8
COLORS = {
    "light": (238, 238, 210),
    "dark": (118, 150, 86)
}

PIECE_THEME = "pieces"

def draw_board(screen):
    for r in range(8):
        for c in range(8):
            color = COLORS["light"] if (r + c) % 2 == 0 else COLORS["dark"]
            pygame.draw.rect(
                screen,
                color,
                pygame.Rect(c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            )

def load_piece_images():
    images = {}
    pieces = ['wR', 'wN', 'wB', 'wQ', 'wK', 'wP',
              'bR', 'bN', 'bB', 'bQ', 'bK', 'bP']

    for piece in pieces:
        path = os.path.join(PIECE_THEME, f"{piece}.png")
        img = pygame.image.load(path)
        img = pygame.transform.scale(img, (SQUARE_SIZE, SQUARE_SIZE))
        images[piece] = img
    return images

def get_piece_symbol(piece):
    if piece is None:
        return None
    return ('w' if piece.color == chess.WHITE else 'b') + piece.symbol().upper()

def draw_pieces(screen, board, images, dragging_piece=None, dragging_pos=None):
    for square in range(64):
        piece = board.piece_at(square)
        if piece:
            if dragging_piece is not None and square == dragging_piece:
                continue

            symbol = get_piece_symbol(piece)
            row = 7 - (square // 8)
            col = square % 8
            screen.blit(
                images[symbol],
                pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            )

    if dragging_piece is not None:
        piece = board.piece_at(dragging_piece)
        symbol = get_piece_symbol(piece)
        img = images[symbol]
        SCREEN.blit(img, (dragging_pos[0] - SQUARE_SIZE // 2, dragging_pos[1] - SQUARE_SIZE // 2))

def mouse_to_square(pos):
    mx, my = pos
    col = mx // SQUARE_SIZE
    row = 7 - (my // SQUARE_SIZE)
    return row * 8 + col

def main():
    board = chess.Board()
    images = load_piece_images()

    dragging = False
    dragging_square = None
    mouse_x, mouse_y = 0, 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                sq = mouse_to_square(event.pos)
                piece = board.piece_at(sq)
                if piece:
                    dragging = True
                    dragging_square = sq
                    mouse_x, mouse_y = event.pos

            if event.type == pygame.MOUSEMOTION and dragging:
                mouse_x, mouse_y = event.pos

            if event.type == pygame.MOUSEBUTTONUP and dragging:
                target_sq = mouse_to_square(event.pos)
                move = chess.Move(dragging_square, target_sq)

                if move in board.legal_moves:
                    board.push(move)

                dragging = False
                dragging_square = None

        draw_board(SCREEN)
        draw_pieces(
            SCREEN,
            board,
            images,
            dragging_piece=dragging_square if dragging else None,
            dragging_pos=(mouse_x, mouse_y)
        )

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

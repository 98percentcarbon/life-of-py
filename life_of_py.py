import pygame, sys, time, os
import numpy as np
pygame.init()
CELL_SIZE = 25
GRID_WIDTH = 2
DEFAULT_DELAY = 150
SPACE_DELAY = 67
FAST_DELAY = 20
WHITE = (255, 255, 255)
BLACK = (5, 5, 5)
DARK_GREY = (20, 20, 20)
GREEN = (144, 238, 144)
SELECTED_WHITE = (255, 255, 255)
HI_COLOR = (255, 255, 255)
width, height = 1000, 1000
GRID_SIZE_X = width // (CELL_SIZE + GRID_WIDTH)
GRID_SIZE_Y = height // (CELL_SIZE + GRID_WIDTH)
GRID_SIZE = min(GRID_SIZE_X, GRID_SIZE_Y)
GRID_SIZE_X = GRID_SIZE
GRID_SIZE_Y = GRID_SIZE
grid = np.zeros((GRID_SIZE_Y, GRID_SIZE_X), dtype=int)
script_dir = os.path.dirname(os.path.realpath(__file__))
icon_path = os.path.join(script_dir, 'life.png')
icon = pygame.image.load(icon_path)
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Life of Py")
clock = pygame.time.Clock()
running = False
generation_time = 0
generation_delay = DEFAULT_DELAY
fast_mode = False
def neighbors(y, x):
    top, bottom, left, right = (y - 1) % GRID_SIZE_Y, (y + 1) % GRID_SIZE_Y, (x - 1) % GRID_SIZE_X, (x + 1) % GRID_SIZE_X
    return [grid[top, left], grid[top, x], grid[top, right], grid[y, left], grid[y, right], grid[bottom, left], grid[bottom, x], grid[bottom, right]]
def set_grid_from_hex(hex_code):
    binary_string = bin(int(hex_code, 16))[2:]
    binary_array = np.array(list(binary_string.zfill(GRID_SIZE_X * GRID_SIZE_Y)), dtype=int)
    grid[:] = binary_array.reshape((GRID_SIZE_Y, GRID_SIZE_X))
while True:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not running:
            if event.button == 1:
                x, y = pygame.mouse.get_pos()
                grid_x = x // (CELL_SIZE + GRID_WIDTH)
                grid_y = y // (CELL_SIZE + GRID_WIDTH)
                grid[grid_y, grid_x] = 1 - grid[grid_y, grid_x]
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = not running
                generation_time = time.time()
            elif event.key == pygame.K_v:
                fast_mode = not fast_mode
                if not running:
                    generation_time = time.time()
            elif event.key == pygame.K_c and not running:
                grid = np.zeros((GRID_SIZE_Y, GRID_SIZE_X), dtype=int)
            elif event.key == pygame.K_h and not running:
                hex_input = input("Enter a hex code: ")
                set_grid_from_hex(hex_input)
            elif event.key == pygame.K_g and not running:
                hex_code = hex(int(''.join(map(str, grid.flatten())), 2))[2:]
                print("Hex Code:", hex_code)
    if running and time.time() - generation_time > generation_delay / 1000:
        new_grid = np.copy(grid)
        for y in range(GRID_SIZE_Y):
            for x in range(GRID_SIZE_X):
                neighbors_sum = np.sum(neighbors(y, x))
                if grid[y, x] == 1 and not (2 <= neighbors_sum <= 3):
                    new_grid[y, x] = 0
                elif grid[y, x] == 0 and neighbors_sum == 3:
                    new_grid[y, x] = 1
        grid = new_grid
        generation_time = time.time()
    generation_delay = FAST_DELAY if fast_mode else DEFAULT_DELAY
    for y in range(GRID_SIZE_Y):
        for x in range(GRID_SIZE_X):
            color = SELECTED_WHITE if grid[y, x] == 1 else BLACK
            rect = pygame.Rect(x * (CELL_SIZE + GRID_WIDTH), y * (CELL_SIZE + GRID_WIDTH), CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, DARK_GREY, rect, width=GRID_WIDTH)
    hi_rect = pygame.Rect((GRID_SIZE_X * (CELL_SIZE + GRID_WIDTH)) + 50, (GRID_SIZE_Y * (CELL_SIZE + GRID_WIDTH)) + 50, CELL_SIZE, CELL_SIZE)
    hi_text = pygame.font.Font(None, 36).render("HI", True, HI_COLOR)
    pygame.draw.rect(screen, BLACK, hi_rect)
    screen.blit(hi_text, hi_rect)
    pygame.display.flip()
    clock.tick(60)

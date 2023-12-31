import pygame
from maze import MazeSolver, initialize_maze, print_maze

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CELL_SIZE = 40

maze = [
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['e', '0', '0', '1', '0', '1', '0', '1', '0', '1'],
    ['1', '1', '0', '1', '0', '1', '0', '1', '0', '1'],
    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
    ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '0', '0', '0', '0', '0', '0', '1', '0', '1'],
    ['1', '0', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', 'm', '1']
]

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Labirinto")

def draw_maze():
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == '1':
                pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif cell == '0':
                pygame.draw.rect(screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif cell == 'e':
                pygame.draw.rect(screen, GREEN, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif cell == 'm':
                pygame.draw.circle(screen, RED, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)

def main():
    running = True

    file_path = "maze.py" 
    maze = initialize_maze(file_path)

    print("Labirinto Inicial:")
    print_maze(maze)

    solver = MazeSolver(maze)
    start_row, start_col = 1, maze[0].index('e')
    solver.solve_maze(start_row, start_col)
    solver.mark_visited_cells()

    print("\nLabirinto após percorrer:")
    print_maze(maze)

    exit_row, exit_col = 9, maze[9].index('m')
    solver.exit_maze(start_row, start_col, exit_row, exit_col)

    print("\nLabirinto após encontrar a saída:")
    print_maze(maze)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        draw_maze()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

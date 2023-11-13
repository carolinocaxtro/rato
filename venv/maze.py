class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.visited = [[False] * self.cols for _ in range(self.rows)]
        self.path = []

    def is_valid_move(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols and self.maze[row][col] in ['0', 'm']

    def solve_maze(self, row, col):
        if not self.is_valid_move(row, col) or self.visited[row][col]:
            return False

        self.path.append((row, col))
        self.visited[row][col] = True

        if self.maze[row][col] == 'm':
            return True  # Cheese found!

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for d_row, d_col in directions:
            if self.solve_maze(row + d_row, col + d_col):
                return True

        self.path.pop()
        return False

    def mark_visited_cells(self):
        for row, col in self.path:
            self.maze[row][col] = '.'  # Mark visited cells with a dot

    def exit_maze(self, start_row, start_col, exit_row, exit_col):
        maze_stack = []
        current_cell = (start_row, start_col)
        exit_cell = (exit_row, exit_col)

        while current_cell != exit_cell:
            self.visited[current_cell[0]][current_cell[1]] = True

            neighbors = [(current_cell[0] + dr, current_cell[1] + dc) for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
            unvisited_neighbors = [(r, c) for r, c in neighbors if self.is_valid_move(r, c) and not self.visited[r][c]]

            if not unvisited_neighbors:
                if not maze_stack:
                    print("Caminho de saída não encontrado.")
                    return
                current_cell = maze_stack.pop()
            else:
                maze_stack.append(current_cell)
                current_cell = unvisited_neighbors[0]

def initialize_maze(file_path):
    with open(file_path, 'r') as file:
        maze = [list(line.strip()) for line in file]
    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(row))

if __name__ == "__main__":
    file_path = "maze.txt"  # Substitua pelo caminho real do seu arquivo
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

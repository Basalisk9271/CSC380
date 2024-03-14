import copy
import random
import sys

def initialize_grid_random(rows, cols, density):
    # Initialize the grid with random living cells.
    grid = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]
    return grid

def initialize_grid_from_file(file_path):
    # Initialize the grid from a file.
    try:
        with open(file_path, 'r') as file:
            # Read the lines from the file, remove leading and trailing spaces, and concatenate them into a single string
            input_data = file.read()

        # Split the input data into rows
        rows = input_data.strip().split('\n')

        # Create a 2D array (grid) and populate it with 1's for 'X' and 0's for '0'
        grid = [[1 if cell == 'X' else 0 for cell in row.split()] for row in rows]

        return grid
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error opening file '{file_path}': {e}")
        sys.exit(1)

def print_grid(grid):
    # Print the current state of the grid with red 'X' characters.
    for row in grid:
        colored_row = ["\033[91mX\033[0m" if cell >= 1 else "." for cell in row]
        print(" ".join(colored_row))
    print()


def apply_rules(grid):
    # Apply the Game of Life rules to compute the next generation.
    new_grid = copy.deepcopy(grid)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            neighbors = count_neighbors(grid, i, j)

            # Rules 1 and 4: Loneliness or overpopulation
            if neighbors <= 1 or neighbors >= 4:
                new_grid[i][j] = 0
            # Rule 2: Stability
            if neighbors == 2:
                if grid[i][j] == 0:
                    new_grid[i][j] = grid[i][j]
                else:
                    new_grid[i][j] = grid[i][j] + 1
            # Rule 3: Birth or Perseverence
            if neighbors == 3:
                if grid[i][j] == 0:
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = grid[i][j] + 1
            # Rule 5: Aging more than 10 generations
            if grid[i][j] >= 11:
                new_grid[i][j] = 0

    return new_grid

def count_neighbors(grid, row, col):
    # Count the number of neighbors for a given cell with values >= 1 but does not count itself
    neighbors = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < rows and 0 <= j < cols and not (i == row and j == col):
                if grid[i][j] >= 1:
                    neighbors += 1

    return neighbors



def get_valid_generations():
    # Prompt the user for the number of generations.
    while True:
        try:
            generations = int(input("\n\033[94mEnter the number of generations (1-99): "))
            print("\033[0m")
            if 1 <= generations <= 100:
                return generations
            else:
                print("How many generations would you like to simulate? (min of 1, max of 100)")
        except ValueError:
            print("Invalid input. Please enter a positive integer between 1 and 100.")

def run_simulation(rows, cols, generations, density=0.5, file_path=None):
    # Run the Game of Life simulation.
    if file_path:
        grid = initialize_grid_from_file(file_path)
    else:
        grid = initialize_grid_random(rows, cols, density)

    # # Write the initial grid to start.txt
    # with open("start.txt", "w") as start_file:
    #     for row in grid:
    #         start_file.write(" ".join(['X' if cell == 1 else '0' for cell in row]) + "\n")

    print("Initial File Colony Prior to Evolution\n************************************************\n")
    print_grid(grid)

    for generation in range(generations):
        
        # Adjust sleep duration for desired speed
        # time.sleep(0.5)

        grid = apply_rules(grid)
        print(f"How Colony Has Evolved After {generation + 1} Generation(s)")
        print("************************************************")
        print_grid(grid)

    # # Write the final grid to final.txt
    # with open("final.txt", "w") as final_file:
    #     for row in grid:
    #         final_file.write(" ".join(map(str, row)) + "\n")

if __name__ == "__main__":
    rows, cols = 20, 20
    file_path = None

    if len(sys.argv) == 3 and sys.argv[1] == "-f":
        file_path = sys.argv[2]
    elif len(sys.argv) > 1:
        print("Usage: python script.py [-f filename]")
        sys.exit(1)

    print("\n\033[94mArtificial Life Simulation of Game of Life")
    print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\033[0m")
    print("\n\033[93mEach cell with one or no neighbors dies, as if by loneliness.\033[0m")
    print("\n\033[93mEach cell with four or more neighbors dies, as if by overpopulation.\033[0m")
    print("\n\033[93mEach cell with two or three neighbors survives.\033[0m")
    print("\n\033[93mEach cell with three neighbors becomes populated.\033[0m")
    print("\n\033[93mEach cell that ages over 10 generations dies.\033[0m")

    generations = get_valid_generations()
    run_simulation(rows, cols, generations, file_path=file_path)


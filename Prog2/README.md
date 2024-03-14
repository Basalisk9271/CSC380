# Game of Life Simulation

**Name:** Gabe Imlay

**Class:** CSC 380: Artificial Intelligence

**Due Date:** Gabe Imlay
## Overview
The program simulates the Game of Life, a cellular automaton devised by John Conway. It models the evolution of a grid of cells based on simple rules.

## Algorithm Outline

1. **Initialization**
   - Initialize a 20x20 grid with random living and dead cells or read from a file.
   - Write the initial grid to `start.txt`.

2. **Simulation Loop**
   - Iterate through the specified number of generations.
   - Print the current generation and grid.
   - Apply the Game of Life rules to compute the next generation.
   - Sleep (optional) for visualization purposes.

3. **Write Final Grid**
   - Write the final grid to `final.txt`.

4. **Rules for Computing Next Generation**
   - Iterate through each cell in the grid.
   - Count the number of living neighbors for each cell.
   - Apply the rules:
      - If a cell has 0 or 1 neighbors, it dies (loneliness).
      - If a cell has 2 neighbors, it remains stable.
      - If a cell has 3 neighbors, it either survives or a new cell is born.
      - If a cell has 4 or more neighbors, it dies (overcrowding).
      - A cell ages; if it ages more than 10 generations, it dies.

5. **File I/O**
   - Read from a file if specified by the user.
   - Write the initial and final grids to `start.txt` and `final.txt`.

## Efficiency Comments

- **Grid Representation**: The grid is represented as a list of lists in Python. While this representation is simple, it might not be the most memory-efficient for very large grids. 

- **Simulation Optimization**: The current implementation computes the next generation in a straightforward manner. Depending on the size of the grid, there might be opportunities for parallelization or other optimization techniques to speed up the simulation process, but as it stands, this method is not too slow at computing each generation. 

- **File Reading and Writing**: File operations are kept simple for clarity. For larger grids or datasets, optimized file I/O techniques, such as buffered reading/writing, could be explored.

## Conclusion
The current algorithm provides a clear and understandable implementation of the Game of Life simulation. Depending on specific requirements, further optimizations might be explored to enhance performance and scalability.

## Sources
Chat-GPT was uniquely helpful when referencing python syntax and helped me out of a few binds along the way when troubleshooting my code bugs. It was also good at explainign better ways to do something, such as counting all of the neighbors. 
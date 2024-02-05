# The Game of Nim
### Gabriel Imlay
### CSC 380: Artificial Intelligence 
### Sources: Chat-GPT for general uquestions on syntax and formatting, classmates for code review and sanity-checking, and online websites about The Game of Nim. 
### Due: February 5th, 2024

*This directory contains Python scripts for playing the Game of Nim. The game can be played in two modes: Machine vs. Machine or Human vs. Machine.*

## Files:

1. **nim.py**
   - This file contains the core functions and logic for playing the Nim game.
   - It can be executed using the `python3` command.
   - The file supports both Machine vs. Machine and Human vs. Machine games.

2. **nim_command_line.py**
   - This file is specifically designed for running the Machine vs. Machine game of Nim from the command line.
   - It is called by the `run_nim.py` file for automated testing purposes.
   - It can be executed using the `python3` command with three integer arguments representing the initial size of piles A, B, and C.

3. **nim_no_xor.py**
   - This file operates similarly to `nim.py` with the same capabilities, but it does not utilize the `binary_xor()` function.
   - It can be executed using the `python3` command.
   - It supports both Machine vs. Machine and Human vs. Machine games.

### Functions:

1. **print_piles(piles)**
   - Displays the current state of piles.

2. **generate_variants(move)**
   - Generates all possible move variants for a given move.

3. **binary_xor(piles)**
   - Calculates the XOR result of binary representations of pile counts.

4. **machine_move(piles, name, unsafe_moves)**
   - Implements the machine's move based on XOR strategy.
   - Updates unsafe moves with the variants of the chosen move.

5. **read_unsafe_moves(filename)**
   - Reads unsafe moves from a file.

6. **write_unsafe_moves(filename, unsafe_moves)**
   - Writes unsafe moves to a file.

7. **human_move(piles)**
   - Takes user input for a valid human move.

8. **is_game_over(piles)**
   - Checks if the game is over by examining pile counts.

9. **get_initial_piles()**
    - Takes user input for the initial number of chips in each pile.

10. **main()**
    - The main game loop and user interaction.
    - Reads and writes unsafe moves.
    - Manages game modes (Machine vs. Machine or Human vs. Machine).

### How to Run:

- **nim.py**:
  Execute the following command in the terminal:
  ```bash
  python3 nim.py
  ```
  Follow the on-screen prompts to set up the game and make moves.

- **nim_command_line.py**:
  Execute the following command in the terminal:
  ```bash
  python3 nim_command_line.py <pile_A_size> <pile_B_size> <pile_C_size>
  ```
  Replace `<pile_A_size>`, `<pile_B_size>`, and `<pile_C_size>` with the desired initial sizes of piles A, B, and C.

- **nim_no_xor.py**:
  Execute the following command in the terminal:
  ```bash
  python3 nim_no_xor.py
  ```
  Follow the on-screen prompts to set up the game and make moves, just like in `nim.py`.

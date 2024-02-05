import random
import sys

def print_piles(piles):
    print("A: {} B: {} C: {}".format(piles['A'], piles['B'], piles['C']))

def generate_variants(move):
    variants = set()
    copy_move = move
    # Add the original variant
    # first_variant = (move[0], move[1], move[2])
    # variants.add(first_variant)
    for i in range(1, 4):
            move = copy_move
            variant_move = (move[0] + i, move[1], move[2])
            variants.add(variant_move)
            variant_move = (move[0], move[1] + i, move[2])
            variants.add(variant_move)
            variant_move = (move[0], move[1], move[2] + i)
            variants.add(variant_move)

    return variants

def machine_move(piles, name, unsafe_moves):
   # Filter out piles with zero chips
    available_piles = [pile for pile, chips in piles.items() if chips > 0]

    if not available_piles:
        return  # No valid move, end the turn

    pile = random.choice(available_piles)
    if piles[pile] == 2:
        chips_to_remove = 1
    else:
        chips_to_remove = random.randint(1, min(3, piles[pile]))
    # Determine the number of chips to remove (sequential)
    # chips_to_remove = min(3, piles[pile])

    # Check if the move leads to a losing position
    original_piles = dict(piles)
    future_piles = dict(piles)
    future_piles[pile] -= chips_to_remove
    if is_game_over(future_piles) or tuple(future_piles.items()) in unsafe_moves:
        print("Machine {} takes {} chip(s) from pile {} and leads to a losing position.".format(name, chips_to_remove, pile))

        # Add the variants to the unsafe_moves set
        original_move = (original_piles['A'], original_piles['B'], original_piles['C'])
        unsafe_moves.update(generate_variants(original_move))
        piles[pile] -= chips_to_remove
    else:
        print("Machine {} takes {} chip(s) from pile {}.".format(name, chips_to_remove, pile))
        piles[pile] -= chips_to_remove

def read_unsafe_moves(filename):
    unsafe_moves = set()
    try:
        with open(filename, 'r') as file:
            for line in file:
                values = tuple(map(int, line.strip().split()))
                unsafe_moves.add(values)
    except FileNotFoundError:
        pass  # File doesn't exist yet, ignore

    return unsafe_moves

def write_unsafe_moves(filename, unsafe_moves):
    with open(filename, 'w') as file:
        for move in unsafe_moves:
            file.write("{} {} {}\n".format(move[0], move[1], move[2]))

def human_move(piles):
    while True:
        try:
            move = input("Enter the pile letter (A, B, C) and the number of chips to remove: ")
            pile, chips_to_remove = move.split()
            chips_to_remove = int(chips_to_remove)
            if pile.upper() in piles and 1 <= chips_to_remove <= min(3, piles[pile.upper()]):
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Try again.")
    
    print("You take {} chip(s) from pile {}.".format(chips_to_remove, pile.upper()))
    piles[pile.upper()] -= chips_to_remove

def is_game_over(piles):
    return all(value == 0 for value in piles.values())

def get_initial_piles():
    while True:
        try:
            input_values = input("Enter a positive number of chips for piles A B C (separated by spaces): ")
            values = list(map(int, input_values.split()))
            
            if all(value > 0 for value in values) and len(values) == 3:
                return {'A': values[0], 'B': values[1], 'C': values[2]}
            else:
                print("Invalid input. Please enter three positive integers separated by spaces.")
        except ValueError:
            print("Invalid input. Please enter three positive integers separated by spaces.")

def main():
    unsafe_moves = read_unsafe_moves('unsafe')

    piles = get_initial_piles()

    print("The number of chips in each pile initially")
    print_piles(piles)

    game_mode = int(input("\nType 0 if you want Machine A and Machine B to play each other, and 1 if YOU want to play against Machine A: "))
    if game_mode == 1:
        start_player = int(input("\nType 0 if you want the MACHINE to start, and 1 if YOU want to start: "))
    else:
        start_player = 0
    

    while not is_game_over(piles):
        
        if game_mode == 1:
            # Section for the player vs machine option
            if start_player % 2 == 0:
                print("\nMachine A's Turn:")
                machine_move(piles, "A", unsafe_moves)
            else:
                print("\nHuman's Move:")
                human_move(piles)
        else:        
            #  Section for the Machine vs Machine option
            if start_player % 2 == 0:
                print("\nMachine A's Turn:")
                machine_move(piles, "A", unsafe_moves)
            else:
                print("\nMachine B's Turn:")
                machine_move(piles, "B", unsafe_moves)



        print("\nTHE NUMBER OF CHIPS IN EACH PILE NOW:")
        print_piles(piles)

        start_player += 1

    if game_mode == 1:
        # Determines the output message for when the user plays the computer
        if start_player % 2 == 0:
            print("\n*** The machine WON! Better luck next time! :( ***")
        else:
            print("\n*** You WON! You are a TOUGH little cookie! :) ***")
    else:
        # Determines the output message for when the computer plays itself
        if start_player % 2 == 0:
            print("\n*** Machine A won! Better luck next time! :( ***")
        else:
            print("\n*** Machine B won! Better luck next time! :( ***")

    # Sort the unsafe moves and write them back to the file
    write_unsafe_moves('unsafe', sorted(unsafe_moves))

if __name__ == "__main__":
    main()
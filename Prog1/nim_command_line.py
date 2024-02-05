import random
import sys

def print_piles(piles):
    print("A: {} B: {} C: {}".format(piles['A'], piles['B'], piles['C']))

def generate_variants(move):
    variants = set()
    copy_move = moves

    # Generate all variants
    for i in range(1, 4):
            move = copy_move
            variant_move = (move[0] + i, move[1], move[2])
            variants.add(variant_move)
            variant_move = (move[0], move[1] + i, move[2])
            variants.add(variant_move)
            variant_move = (move[0], move[1], move[2] + i)
            variants.add(variant_move)

    return variants

def binary_xor(piles):
    binary_piles = [bin(count)[2:] for count in piles.values()]

    # Pad the binary representations with leading zeros to ensure equal length
    max_length = max(len(binary) for binary in binary_piles)
    binary_piles = [binary.zfill(max_length) for binary in binary_piles]

    # Calculate XOR of corresponding bits in the binary representations
    xor_result = ''.join(str(sum(int(binary[i]) for binary in binary_piles) % 2) for i in range(max_length))

    return xor_result

def machine_move(piles, name, unsafe_moves):
    # Filter out piles with zero chips
    available_piles = [pile for pile, chips in piles.items() if chips > 0]

    if not available_piles:
        return  # No valid move, end the turn

    # Calculate the XOR result of the binary representations of pile counts
    xor_result = binary_xor(piles)

    # Find the first pile where flipping the bits lowers the count
    for pile in available_piles:
        chips_to_remove = min(3, piles[pile])
        future_piles = dict(piles)
        future_piles[pile] -= chips_to_remove

        # Calculate the XOR result for the future state
        future_xor_result = binary_xor(future_piles)

        # If the XOR result changes from 1 to 0, make this move
        if '1' in future_xor_result and future_xor_result.count('1') < xor_result.count('1'):
            print("Machine {} takes {} chip(s) from pile {}.".format(name, chips_to_remove, pile))
            original_move = (piles['A'], piles['B'], piles['C'])
            unsafe_moves.update(generate_variants(original_move))
            
            piles[pile] -= chips_to_remove
            return

    # If no optimal move is found, remove 1 chip
    pile = random.choice(available_piles)
    chips_to_remove = 1
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

def is_game_over(piles):
    return all(value == 0 for value in piles.values())

def main():
    unsafe_moves = read_unsafe_moves('unsafe')

    if len(sys.argv) != 4:
        print("Usage: python nim.py <pile_A_size> <pile_B_size> <pile_C_size>")
        return

    try:
        # Extract pile sizes from command line arguments
        pile_A_size = int(sys.argv[1])
        pile_B_size = int(sys.argv[2])
        pile_C_size = int(sys.argv[3])

        piles = {'A': pile_A_size, 'B': pile_B_size, 'C': pile_C_size}

        print("The number of chips in each pile initially")
        print_piles(piles)
        start_player = 0

        while not is_game_over(piles):
            if start_player % 2 == 0:
                print("Machine A's Turn:")
                machine_move(piles, "A", unsafe_moves)
            else:
                print("Machine B's Turn:")
                machine_move(piles, "B", unsafe_moves)

            print("\nTHE NUMBER OF CHIPS IN EACH PILE NOW:")
            print_piles(piles)

            start_player += 1

        # Determines the output message for when the computer plays itself
        if start_player % 2 == 0:
            print("*** Machine A won! Better luck next time! :( ***")
        else:
            print("*** Machine B won! Better luck next time! :( ***")

        # Sort the unsafe moves and write them back to the file
        write_unsafe_moves('unsafe', sorted(unsafe_moves))

    # Exception error for invalid values
    except ValueError:
        print("Invalid input. Please enter valid integer values for pile sizes.")

if __name__ == "__main__":
    main()

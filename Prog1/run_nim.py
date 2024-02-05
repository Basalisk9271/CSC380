import subprocess
import random

# Loop 1000 times
for _ in range(1000):
    # Generate random numbers between 1 and 10 for the three arguments
    arg1 = str(random.randint(1, 10))
    arg2 = str(random.randint(1, 10))
    arg3 = str(random.randint(1, 10))

    # Command to run nim.py with the generated arguments
    command = f"python3 nim_command_line.py {arg1} {arg2} {arg3}"

    # Use subprocess to run the command
    subprocess.run(command, shell=True)

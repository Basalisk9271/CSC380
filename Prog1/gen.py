with open("unsafe.superlong.txt", "w") as file:
    leftmost = 0
    middle = 0
    rightmost = 0

    for i in range(5000):
        set_of_numbers = f"{leftmost} {middle} {rightmost}\n"
        file.write(set_of_numbers)

        rightmost += 1
        if rightmost > 30:
            rightmost = 0
            middle += 1

        if middle > 30:
            middle = 0
            leftmost += 1

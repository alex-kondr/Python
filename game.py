from random import randint

SIZE_N = 5
SIZE_M = 5

char_x = 0 #randint(0, SIZE_N - 1)
char_y = 0 #randint(0, SIZE_M - 1)
char_sign = "X"

exit_x = randint(0, SIZE_N - 1)
exit_y = randint(0, SIZE_M - 1)

turns = 0

while True:
    world_map = ""
    win_condidititon = char_x == exit_x and char_y == exit_y

    if win_condidititon:
        char_sign = "W"

    for j in range(SIZE_M):
        row = "|"

        for i in range(SIZE_N):

            if char_x == i and char_y == j:
                row += f"{char_sign}|"
            elif exit_x == i and exit_y == j:
                row += "O|"
            else:
                row += " |"

        world_map += f"{row}\n"

    print(world_map)

    if win_condidititon:
        print(f"You WON in {turns} turns")
        break

    direction = input("Enter direction (u/d/l/r): ")

    if direction == "u" and char_y > 0:
        char_y -= 1
    elif direction == "d" and char_y < SIZE_M - 1:
        char_y += 1
    elif direction == "l" and char_x > 0:
        char_x -= 1
    elif direction == "r" and char_x < SIZE_N - 1:
        char_x += 1

    turns += 1

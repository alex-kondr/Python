def safe_pawns(pawns: set) -> int:
    # add your code here   

    count = 0

    for item in pawns:

        difencive1 = chr(ord(item[0]) - 1) + str(int(item[1]) - 1)
        difencive2 = chr(ord(item[0]) + 1) + str(int(item[1]) - 1)

        if difencive1 in pawns or difencive2 in pawns:
            count += 1

    return count


print("Example:")
print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))

assert safe_pawns({"d2", "f4", "d4", "b4", "e3", "g5", "c3"}) == 6
assert safe_pawns({"f4", "g4", "d4", "b4", "e4", "e5", "c4"}) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")

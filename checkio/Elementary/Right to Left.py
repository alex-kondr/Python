from cmath import phase


def left_join(phrases: tuple) -> str:
    """
    Join strings and replace "right" to "left"
    """
    
    list = []

    for item in phrases:           
        list.append(item.replace("right", "left"))

    return ",".join(list)


print("Example:")
print(left_join(("left", "right", "left", "stop")))

assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
assert left_join(("brightness wright",)) == "bleftness wleft"
assert left_join(("enough", "jokes")) == "enough,jokes"

print("The mission is done! Click 'Check Solution' to earn rewards!")

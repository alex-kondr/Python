def is_even(num):
    if num == 0:
        return True
    else:
        return is_odd(num-1)

def is_odd(num):
    return not is_even(num)

print(is_odd(10))
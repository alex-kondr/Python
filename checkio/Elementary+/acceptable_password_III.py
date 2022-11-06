# Taken from mission Acceptable Password II

# Taken from mission Acceptable Password I

def is_acceptable_password(password: str) -> bool:
    # your code here
    if len(password) > 6:

        in_number = False
        in_alpha = False

        for char in password:            

            if char.isdigit():
                in_number = True

            elif char.isalpha():
                in_alpha = True

            if in_number and in_alpha:
                return True

    return False


assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == False
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")

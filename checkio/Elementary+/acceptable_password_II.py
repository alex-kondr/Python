# Taken from mission Acceptable Password I

def is_acceptable_password(password: str) -> bool:
    # your code here
    list_numb = [True for i in range(11) if str(i) in password]

    if len(password) > 6 and True in list_numb:
        return True
    
    return False


assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == False
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")

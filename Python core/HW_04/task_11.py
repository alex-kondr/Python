def is_valid_password(password):

    one_upper_char = False
    one_lower_char = False
    one_numeric_char = False
    len_8 = True if len(password) == 8 else False

    pass_set = set(password)

    for char in pass_set:

        if char.isupper() and not one_upper_char:
            one_upper_char = True
            continue

        if char.islower() and not one_lower_char:
            one_lower_char = True
            continue

        if char.isnumeric() and not one_numeric_char:
            one_numeric_char = True

    return one_upper_char and one_lower_char and one_numeric_char and len_8
            

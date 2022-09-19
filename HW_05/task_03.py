def sanitize_phone_number(phone):

    import re

    number = re.findall("\d", phone)

    return "".join(number)
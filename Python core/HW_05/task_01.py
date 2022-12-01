def real_len(text):

    import re

    return len(re.findall("\S", text))
    
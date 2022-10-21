import re

txt = "2+ 34-5 * 3"

def token_parser(s):

    return re.findall(r"\d+|[+-/*)()]")

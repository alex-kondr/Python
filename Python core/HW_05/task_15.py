import re


def find_all_links(text):
    result = []
    iterator = re.finditer(r"htt(p|ps)://([\w]+\.[a-zA-Z]+)[\w\.]+", text)
    for match in iterator:
        result.append(match.group())
    return result
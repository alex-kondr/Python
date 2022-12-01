import re


def find_all_phones(text):
    result = re.findall(
        r"[+380(]{5}\d{2}[)]\d{3}[-]\d[-]\d{3}|[+380(]{5}\d{2}[)]\d{3}[-]\d\d[-]\d\d", text)
    return result

import re


def find_all_emails(text):
    result = re.findall(r"[a-zA-Z]\S{1,}@\w{1,}[.]\w{2,}", text)
    return result

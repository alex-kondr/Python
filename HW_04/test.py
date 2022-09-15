lang = {"Python": 1991, "Java": 1995, "JS": 1995}


def lookup_key(data, value="JSS"):
    for key in data:
        if key == value:
            print(key)

lookup_key(lang)
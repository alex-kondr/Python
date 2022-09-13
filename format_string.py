def format_string(string, length):
    if len(string) < length:
        
        space_count = (length - len(string)) // 2
        string = space_count * " " + string

    return(string)

print(format_string(length=12, string="aaaaaaaaaaaaaaaaac"))
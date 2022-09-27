def formatted_numbers():

    list_number = ["|{:^10}|{:^10}|{:^10}|".format("decimal", "hex", "binary")]

    for numb in range(16):
        
        list_number.append("|{:<10d}|{:^10x}|{:>10b}|".format(numb, numb, numb))

    return list_number

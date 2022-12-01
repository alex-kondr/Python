data = ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]

def decode(data):

    data.reverse()

    def dec(data):

        if not data:
            return []
        else:
            out_list = dec(data[2:])
            if not out_list:
                out_list = list(data[1] * data[0])
            else:
                out_list.extend(data[1] * data[0])
            return out_list
    
    return dec(data)

print(decode(data))



data = ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]
data1 = "XXXZZXXYYYZZ"
data2 = ""

# def encode(data):

#     out_list = []
#     n = 1
#     i = 0

#     for i, char in enumerate(data):
#         if i > 0:
#             if char == data[i-1]:
#                 n += 1
#             else:
#                 out_list += [data[i-1], n]
#                 n = 1
#     if i:
#         out_list += [data[i-1], n]

#     return out_list


def encode(data):
    def count(string):
        if not string:
            return 0
        else:
            n = count(string[1:])
            n += 1
        return n

    out_list = []
    temp = ""
    i = 0

    for i, char in enumerate(data):
        if i > 0:
            if char == data[i-1]:
                temp += char
            else:
                temp += data[i-1]
                n = count(temp)
                out_list += [data[i-1], n]
                temp = ""

    if i:
        temp += data[i-1]
        n = count(temp)
        out_list += [data[i-1], n]

    return out_list


print(encode(data2))

data1 = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]



def flatten(data):
    out_list = []

    def recursiv(data):

        for item in data:

            if type(item) == list:
                recursiv(item)

            else:
                out_list.append(item)
            
    recursiv(data)
    
    return out_list

print(flatten(data1))

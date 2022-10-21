list_data = [[1,2,3],[3,4], [5,6]]


def data_preparation(list_data):

    output_list = []

    for item in list_data:

        if len(item) > 2:
            item.sort()
            item.pop(len(item)-1)
            item.pop(0)
        
        output_list += item
    
    output_list.sort(reverse=True)

    return output_list


print(data_preparation(list_data))

        



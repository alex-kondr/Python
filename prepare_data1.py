from datetime import datetime
def prepare_data(data):

    time_start = datetime.now()

    big_num = 0
    small_num = data[0]

    for num in data:
        if num > big_num:
            big_num = num
        elif num < small_num:
            small_num = num

    data.remove(big_num)
    data.remove(small_num)
    data.sort()
    
    print(datetime.now() - time_start)

    return data

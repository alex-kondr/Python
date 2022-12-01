from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):

    getcontext().prec = signs_count

    sum = 0

    decimal_number = [Decimal(i) for i in number_list]

    for num in decimal_number:
        sum += num
    
    average = sum / Decimal(len(decimal_number))

    return average


print(decimal_average([31, 55, 177, 2300, 1.57], 9))


def split_list(grade):
    
    list_less_ar = []
    list_more_ar = []
    
    if grade:

        sum = 0

        for gr in grade:
            sum += gr

        arithmetic_mean = sum / len(grade)

        for gr in grade:
            if gr <= arithmetic_mean:
                list_less_ar.append(gr)
            else:
                list_more_ar.append(gr)        
    
    return list_less_ar, list_more_ar



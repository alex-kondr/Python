s = 'mi1powperet'

def solve_riddle(riddle, word_length, start_letter, reverse=False):

    len_str = len(riddle)

    for i in range(len_str):

        if reverse:

            str_temp = riddle[len_str-i-1:len_str-word_length-i-1:-1]
            if str_temp.startswith(start_letter):
                return str_temp

        else:

            str_temp = riddle[i:word_length+i]
            if str_temp.startswith(start_letter):
                return str_temp
    
    return ""


print(solve_riddle(s, 3, 'r', True))

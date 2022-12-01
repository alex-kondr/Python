import sys

def parse_args():

    result = ""

    if len(sys.argv) > 1:

        for i in range(1, len(sys.argv) - 1):        
            result += sys.argv[i] + " "

        result += sys.argv[len(sys.argv) - 1]

    return result


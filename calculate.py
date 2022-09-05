result = None
operand = None
operator = None
temp_operator = ("+", "-", "*", "/", "=")
wait_for_number = True

while True:
    if wait_for_number:
        temp_numberic = input("Enter your number: ") 
        try:
            if result:
                operand = int(temp_numberic)
            else: 
                result = int(temp_numberic)
        except:
            try:
                if result:
                    operand = float(temp_numberic)
                else:
                    result = float(temp_numberic)
            except:
                print("This is not a number")
                continue

        wait_for_number = False
    else:
        operator = input("Enter operator: ")
        if operator in temp_operator:
            if operator == "=":
                print(result)
                break
            wait_for_number = True
        else:
            print("This is not a operator")
            operator = None

    if (result or result == 0) and (operand or operand == 0) and operator:
        if operator == "-":
            result -= operand
        elif operator == "+":
            result += operand
        elif operator == "*":
            result *= operand
        elif operator == "/":
            result /= operand
        # elif operator == "=":
        #     print(result)
        #     break
        operand = None
        operator = None

    print(f"Result = {result}, operand = {operand}, operator = {operator}")

    # if opera